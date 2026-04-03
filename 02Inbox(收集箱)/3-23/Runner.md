## 报告 1：OpenCompass Runner 模块分析

### 第一步：模块文件和功能概览

|文件名|代码行数|主要功能|核心类|
|---|---|---|---|
|`base.py`|85|定义Runner基类接口|`BaseRunner`|
|`local.py`|249|本地多进程任务调度器|`LocalRunner`|
|`local_api.py`|250|本地API模式任务调度（带并发控制）|`LocalAPIRunner`|
|`slurm.py`|163|SLURM集群任务调度|`SlurmRunner`|
|`slurm_sequential.py`|-|SLURM顺序执行模式|`SlurmSequentialRunner`|
|`dlc.py`|359|阿里云DLC分布式调度|`DLCRunner`|
|`rjob.py`|-|其他集群调度|`RJobRunner`|
|`volc.py`|-|火山引擎调度|`VolcRunner`|

**文件路径：** `d:\project\opencompass_inner\opencompass\runners\`

---

### 第二步：详细分析各类和方法

#### 1. BaseRunner 基类

**文件：** `d:\project\opencompass_inner\opencompass\runners\base.py` (行 10-85)

##### 类定义和初始化

python

`   ``` class BaseRunner:     """Base class for all runners. A runner is responsible for launching     multiple tasks.     """ ```   `

**初始化参数表：**

|参数名|类型|默认值|作用|
|---|---|---|---|
|`task`|ConfigDict|必需|任务类型配置（指定runner实例执行的task类型）|
|`debug`|bool|False|调试模式标志（控制是否打印详细日志）|
|`lark_bot_url`|str|None|飞书/Lark机器人URL（任务完成时通知）|

##### 核心方法详解

**方法1：`__call__(tasks)` - 行 31-40**

python

`   ``` def __call__(self, tasks: List[Dict[str, Any]]):     """Launch multiple tasks and summarize the results."""     status = self.launch(tasks)     status_list = list(status)     self.summarize(status_list) ```   `

|参数|类型|作用|
|---|---|---|
|`tasks`|List[Dict]|Partitioner生成的任务配置列表|

**返回值：** None（但会调用 launch 和 summarize）

**逻辑流程：**

1. 调用 `launch()` 启动所有任务
2. 将迭代器转换为列表格式
3. 调用 `summarize()` 汇总结果

**方法2：`launch(tasks)` - 行 42-52 (抽象方法)**

python

`   ``` @abstractmethod def launch(self, tasks: List[Dict[str, Any]]) -> List[Tuple[str, int]]:     """Launch multiple tasks.""" ```   `

|参数|类型|作用|
|---|---|---|
|`tasks`|List[Dict]|任务列表|

**返回值：** `List[Tuple[str, int]]`

- 元素为 `(task_name, exit_code)` 的列表
- exit_code: 0 表示成功，非0表示失败

**方法3：`summarize(status)` - 行 54-84**

python

`   ``` def summarize(self, status: List[Tuple[str, int]]) -> None:     """Summarize the results of the tasks.""" ```   `

|参数|类型|作用|
|---|---|---|
|`status`|List[Tuple[str, int]]|launch() 返回的状态列表|

**关键逻辑（行 61-84）：**

python

`   ``` for _task, code in status:     if code != 0:         get_logger().error(f'{_task} failed with code {code}')         failed_logs.append(_task)  if self.lark_reporter:     num_succeeded = len(status) - len(failed_logs)     if len(failed_logs) > 0:         # 发送失败通知：包含失败任务列表         self.lark_reporter.post(             title=f'Bad news: {len(failed_logs)} failed.',             content=...)     else:         # 发送成功通知         self.lark_reporter.post(             title='Great news: all tasks finished!',             content=...) ```   `

---

#### 2. LocalRunner 本地调度器

**文件：** `d:\project\opencompass_inner\opencompass\runners\local.py` (行 40-249)

##### 初始化配置

**参数表：**

|参数名|类型|默认值|作用|
|---|---|---|---|
|`task`|ConfigDict|必需|任务类型配置|
|`max_num_workers`|int|16|最大并发工作线程数|
|`max_workers_per_gpu`|int|1|每个GPU最多分配的工作线程数|
|`debug`|bool|False|调试模式|
|`keep_tmp_file`|bool|False|是否保留临时参数文件|
|`lark_bot_url`|str|None|Lark通知URL|

##### GPU 分配策略详解（行 69-196）

**核心数据结构：**

python

`   ``` gpus = np.zeros(max(all_gpu_ids) + 1, dtype=np.uint) gpus[all_gpu_ids] = self.max_workers_per_gpu ```   `

- `gpus` 是长度为 `max_gpu_id + 1` 的数组
- `gpus[i]` 表示 GPU i 还可分配的工作线程数
- 初始值为 `max_workers_per_gpu`

**GPU获取流程（行 168-176）：**

python

`   ``` while True:     lock.acquire()     if sum(gpus > 0) >= num_gpus:  # 检查可用GPU数         gpu_ids = np.where(gpus)[0][:num_gpus]  # 获取前num_gpus个可用GPU         gpus[gpu_ids] -= 1  # 递减计数         lock.release()         break     lock.release()     time.sleep(1)  # 轮询等待 ```   `

**关键特点：**

- 使用 `threading.Lock()` 保证线程安全
- 轮询机制（每秒检查一次）等待可用GPU
- 支持多个任务共享同一GPU

##### 命令生成（行 24-36）

python

`   ``` def get_command_template(gpu_ids: List[int]) -> str:     """Format command template given available gpu ids."""     if is_npu_available():         tmpl = 'ASCEND_RT_VISIBLE_DEVICES=' + ','.join(...)     elif sys.platform == 'win32':         tmpl = 'set CUDA_VISIBLE_DEVICES=' + ','.join(...) + ' & {task_cmd}'     else:         tmpl = 'CUDA_VISIBLE_DEVICES=' + ','.join(...) + ' {task_cmd}'     return tmpl ```   `

**支持的平台：**

- NPU (昇腾芯片) - 使用 ASCEND_RT_VISIBLE_DEVICES
- Windows - 使用 `set` 命令和 `&` 分隔符
- Linux/Unix - 使用环境变量导出和空格分隔

##### 调试模式 vs 正常模式（行 97-196）

**调试模式逻辑（行 97-152）：**

1. **串行执行**：任务一个接一个运行
2. **模型复用**（仅infer任务）：
    
    python
    
    `   ``` if 'infer' in self.task_cfg.type.lower():     task.run(cur_model=getattr(self, 'cur_model', None),              cur_model_abbr=getattr(self, 'cur_model_abbr', None))     self.cur_model = task.model     self.cur_model_abbr = model_abbr_from_cfg(task.model_cfg) ```   `
    

3. **直接调用vs子进程**：
    
    - 如果命令包含 'python3' 或 'python'，直接调用 `task.run()`
    - 否则通过 subprocess 执行，日志保存到 `tmp/{os.getpid()}_debug.log`
    
    **正常模式逻辑（行 153-196）：**
    

4. **ThreadPoolExecutor 并行执行**（最多 max_num_workers 个线程）
5. **submit() 函数处理单个任务提交**（行 163-190）：
    - 等待GPU可用（带锁的轮询）
    - 递减GPU计数
    - 调用 `_launch()` 执行任务
    - 执行完后递增GPU计数（释放GPU）
6. **进度条跟踪**（tqdm）

##### _launch() 方法 - 行 198-248_

**流程：**

python

`   ``` def _launch(self, task, gpu_ids, index):     task_name = task.name     pwd = os.getcwd()          # 1. 生成UUID避免文件冲突     uuid_str = str(uuid.uuid4())     param_file = f'{pwd}/tmp/{uuid_str}_params.py'          try:         # 2. 配置文件序列化         task.cfg.dump(param_file)                  # 3. 生成命令         tmpl = get_command_template(gpu_ids)         get_cmd = partial(task.get_command,                           cfg_path=param_file,                           template=tmpl)         cmd = get_cmd()                  # 4. 执行命令，输出到日志         out_path = task.get_log_path(file_extension='out')         with open(out_path, 'w', encoding='utf-8') as stdout:             result = subprocess.run(cmd, shell=True, text=True,                                     stdout=stdout, stderr=stdout)                  if result.returncode != 0:             logger.error(f'task {task_name} fail, see\n{out_path}')     finally:         # 5. 清理临时文件         if not self.keep_tmp_file:             os.remove(param_file)          return task_name, result.returncode ```   `

**关键参数表：**

|参数|类型|作用|
|---|---|---|
|`task`|BaseTask|已构建的任务实例|
|`gpu_ids`|array|分配给此任务的GPU ID|
|`index`|int|任务索引|

**返回值：** `Tuple[str, int]` - (任务名, 退出码)

---

#### 3. SlurmRunner SLURM集群调度器

**文件：** `d:\project\opencompass_inner\opencompass\runners\slurm.py` (行 20-163)

##### 初始化参数

|参数名|类型|默认值|作用|
|---|---|---|---|
|`task`|ConfigDict|必需|任务类型配置|
|`max_num_workers`|int|32|SLURM最大并行任务数|
|`retry`|int|2|任务失败重试次数|
|`partition`|str|None|SLURM分区名 (-p)|
|`quotatype`|str|None|SLURM配额类型|
|`qos`|str|None|SLURM服务质量等级|
|`extra_command`|List[str]|None|额外SLURM命令（如 ['-c 12', '-w node1']）|

##### launch() 方法 - 行 59-77

python

`   ``` def launch(self, tasks: List[Dict[str, Any]]) -> List[Tuple[str, int]]:     if not self.debug:         status = track_parallel_progress(             self._launch,             tasks,             nproc=self.max_num_workers,             keep_order=False)     else:         status = [self._launch(task, random_sleep=False) for task in tasks]     return status ```   `

- **正常模式**：使用mmengine的 `track_parallel_progress` 并行执行
- **调试模式**：串行执行，禁用随机延迟

##### _launch() 方法 - 行 79-158_

**SLURM命令构建（行 101-117）：**

python

`   ``` tmpl = 'srun' if self.partition:     tmpl += f' -p {self.partition}' if self.quotatype:     tmpl += f' --quotatype={self.quotatype}' if self.qos:     tmpl += f' --qos={self.qos}' if num_gpus > 0:     tmpl += f' --gres=gpu:{num_gpus}' for extra_cmd in self.extra_command:     tmpl += f' {extra_cmd}' tmpl += f" -N1 -u -J '{task_name[:512]}'" + ' {task_cmd}' ```   `

**SLURM参数含义：**

|参数|含义|
|---|---|
|`srun`|SLURM任务运行命令|
|`-p partition`|指定计算分区|
|`--quotatype=...`|配额类型（SLURM扩展）|
|`--qos=...`|服务质量等级|
|`--gres=gpu:N`|请求N个GPU|
|`-N1`|单节点执行|
|`-u`|立即启动（不缓冲）|
|`-J 'name'`|任务名（最多512字符）|

**失败重试机制（行 138-151）：**

python

`   ``` result = subprocess.run(cmd, ...)  retry = self.retry output_paths = task.get_output_paths() while self._job_failed(result.returncode, output_paths) and retry > 0:     retry -= 1     if random_sleep:         time.sleep(random.randint(0, 10))     cmd = get_cmd()  # 重新生成命令以刷新端口号     result = subprocess.run(cmd, ...) ```   `

**_job_failed() 判断逻辑（行 160-162）：**

python

`   ``` def _job_failed(self, return_code: int, output_paths: List[str]) -> bool:     return return_code != 0 or not all(         osp.exists(output_path) for output_path in output_paths) ```   `

- **失败条件**：返回码非0 **或** 输出文件不存在
- **这样设计的原因**：某些SLURM环境可能返回码为0但文件未生成

---

#### 4. DLCRunner 阿里云DLC调度器

**文件：** `d:\project\opencompass_inner\opencompass\runners\dlc.py` (行 23-359)

##### 初始化参数

|参数名|类型|默认值|作用|
|---|---|---|---|
|`task`|ConfigDict|必需|任务类型配置|
|`aliyun_cfg`|ConfigDict|必需|阿里云配置（workspace_id、resource_id等）|
|`max_num_workers`|int|32|最大并行任务数|
|`eval_with_gpu`|list|['plugin_eval']|哪些eval任务需要GPU|
|`retry`|int|2|重试次数|
|`preemptible`|bool|False|是否允许抢占式任务|
|`keep_tmp_file`|bool|True|是否保留临时文件|

##### 环境变量配置（行 128-175）

**三种环境激活方式：**

1. **用户自定义Conda环境**（行 128-135）：
    
    python
    
    `   ``` if bashrc_path and conda_env_name:     shell_cmd = (f'source {bashrc_path}; '                  f'conda activate {conda_env_name}; ') ```   `
    

2. **公共Conda环境**（行 137-143）：
    
    python
    
    `   ``` elif python_env_path:     shell_cmd = (f'export PATH={python_env_path}/bin:$PATH; '                  f'export PYTHONPATH={pwd}:$PYTHONPATH; ') ```   `
    

3. **系统Python**（行 144-146）：
    
    python
    
    `   ``` else:     shell_cmd = '' ```   `
    

**缓存和代理配置（行 148-175）：**

python

`   ``` # HuggingFace缓存 shell_cmd += f'export HF_HUB_CACHE={huggingface_cache}; ' shell_cmd += f'export HUGGINGFACE_HUB_CACHE={huggingface_cache}; '  # Torch缓存 shell_cmd += f'export TORCH_HOME={torch_cache}; '  # 离线模式 if hf_offline:     shell_cmd += 'export HF_DATASETS_OFFLINE=1; ...'  # 代理设置 if http_proxy:     shell_cmd += f'export http_proxy={http_proxy}; export https_proxy={http_proxy}; '  # HuggingFace API端点 if hf_endpoint:     shell_cmd += f'export HF_ENDPOINT={hf_endpoint}; '  # 自定义环境变量 for extra_env in extra_envs:     shell_cmd += f'export {extra_env}; ' ```   `

##### DLC命令构建（行 189-215）

python

`   ``` if dlc_job_cmd == 'create':     dlc_job_cmd = 'create job --kind PyTorchJob'     worker_cmd = ' --worker_count 1' else:     dlc_job_cmd = 'submit pytorchjob'     worker_cmd = ' --workers 1'  tmpl = (f'dlc {dlc_job_cmd}'         f''' --command '{shell_cmd}' '''         f' --name {task_name[:512]}'         f' --workspace_id {workspace_id}'         f' --resource_id={resource_id}'         f' --priority {task_priority}'         f'{worker_cmd}'         f' --worker_cpu {max(num_gpus * 8, worker_cpu)}'         f' --worker_gpu {num_gpus}'         f' --worker_memory {max(num_gpus * 128, worker_memory)}Gi'         f''' --worker_image {worker_image}'''         f''' --data_sources={','.join(data_sources)}'''         f''' --enable_priority_preemption={preemptible}''') ```   `

**资源计算逻辑：**

- **CPU**：至少 `num_gpus * 8`，默认12核
- **内存**：至少 `num_gpus * 128`GB，默认192GB
- **GPU**：直接使用 `num_gpus`

##### 作业监控机制（行 241-334）

**关键变量：**

|变量|作用|
|---|---|
|`pod_create_time`|Pod创建时间（用于日志查询）|
|`pri_time`|上一次查询的时间戳|
|`initial_time`|本地初始时间（用于时间同步）|

**监控循环（line 273-333）：**

python

`   ``` while True:     time.sleep(dlc_sleep_time)  # 避免频繁请求          # 1. 获取作业信息     job_info = json.loads(subprocess.getoutput(f'dlc get job {job_id}'))     status = job_info['Status']          # 2. 检查终止条件     if status == 'Failed' or status == 'Stopped':         return -1     elif status == 'Succeeded':         return 0     elif status != 'Running':         continue          # 3. 计算Pod时间（处理时间差）     if pod_create_time is None:         pod_create_time = datetime.datetime.strptime(             job_info['GmtCreateTime'], '%Y-%m-%dT%H:%M:%SZ')     elapsed_time = datetime.datetime.now() - initial_time     cur_time = (pod_create_time + elapsed_time).strftime(...)          # 4. 获取日志     logs_cmd = f'dlc logs {job_id} {job_id}-master-0 ...'     log_output = subprocess.getoutput(logs_cmd)     if logs found:         stdout.write(log_output) ```   `

**设计要点：**

- 处理Pod时间与本地时间不一致问题
- 增量日志拉取（基于 `pri_time` 和 `cur_time`）
- 避免重复输出

##### GPU分配（行 111-116）

python

`   ``` is_eval_task = 'OpenICLEval' in task_name if is_eval_task and num_gpus == 0:     for check_name in self.eval_with_gpu:         if check_name in task_name:             num_gpus = 1             break ```   `

特殊处理：如果是 eval 任务且 num_gpus=0，检查是否需要强制分配1个GPU

---

#### 5. LocalAPIRunner API模式调度器

**文件：** `d:\project\opencompass_inner\opencompass\runners\local_api.py` (行 148-250)

##### 主要特性

- **目标**：用于有并发限制的API模型（如Qwen、GPT等）
- **并发控制**：通过信号量限制同时请求数
- **支持多进程**：使用 `multiprocessing.Pool`

##### 初始化参数

|参数名|类型|默认值|作用|
|---|---|---|---|
|`task`|ConfigDict|必需|任务类型配置|
|`concurrent_users`|int|必需|信号量大小（最大并发请求数）|
|`max_num_workers`|int|16|进程池大小|
|`debug`|bool|False|调试模式|

##### launch() 方法 - 行 180-249

**调试模式**（行 191-210）：

- 回退到 LocalRunner 的子进程模式
- 生成配置文件并通过subprocess运行

**正常模式**（行 211-248）：

python

`   ``` with Manager() as manager:     tokens = manager.Semaphore(self.concurrent_users)  # 创建信号量     pbar_counter = manager.Value('i', 0)          with Pool(processes=self.max_num_workers) as pool:         for task in tasks:             pool.apply_async(                 submit,                 (task, self.task_cfg['type'], tokens),                 callback=update)                  # 更新进度条         while True:             cur_count = pbar_counter.value             if cur_count > pbar.n:                 pbar.update(cur_count - pbar.n)             if cur_count >= pbar.total:                 break             time.sleep(1) ```   `

##### 猴子补丁 monkey_run（行 26-52）

替换 `OpenICLInferTask.run()` 方法，添加令牌信号量：

python

`   ``` def monkey_run(self, tokens: SyncManager.Semaphore):     """Hack for infer task run, add tokens for multiprocess."""     for model_cfg, dataset_cfgs in zip(self.model_cfgs, self.dataset_cfgs):         self.model = build_model_from_cfg(model_cfg)         assert self.model.is_api, 'Only API model is supported.'         self.model.tokens = tokens  # 注入令牌                  for dataset_cfg in dataset_cfgs:             self._inference() ```   `

**关键特点：**

- 将信号量对象注入到API模型的 `tokens` 属性
- 模型推理时使用该信号量进行请求并发控制

---

### 第三步：模块内部调用关系和数据流

#### 执行流图

plaintext

`   ``` Runner.__call__(tasks)     │     ├─> launch(tasks)  [抽象方法，各Runner实现不同]     │   │     │   ├─ LocalRunner:     │   │  │     │   │  ├─ Debug模式: 逐个任务串行执行     │   │  │  └─ task.run()     │   │  │     │   │  └─ Normal模式: ThreadPoolExecutor并行     │   │     ├─ submit(task) [Lambda函数]     │   │     │  ├─ [等待GPU可用，轮询]     │   │     │  └─ _launch(task, gpu_ids)     │   │     │     ├─ task.cfg.dump(param_file)     │   │     │     ├─ task.get_command()     │   │     │     └─ subprocess.run(cmd)     │   │     └─ [进度条更新]     │   │     │   ├─ SlurmRunner:     │   │  └─ track_parallel_progress(_launch, max_workers=32)     │   │     └─ _launch(task)     │   │        ├─ task.cfg.dump(param_file)     │   │        ├─ [构建srun命令]     │   │        ├─ subprocess.run(cmd)     │   │        └─ [重试循环: 检查返回码和输出文件]     │   │     │   ├─ DLCRunner:     │   │  └─ track_parallel_progress(_launch, max_workers=32)     │   │     └─ _launch(task)     │   │        ├─ [构建环境变量]     │   │        ├─ task.cfg.dump(param_file)     │   │        ├─ [构建dlc命令]     │   │        ├─ subprocess.getoutput() [获取job_id]     │   │        └─ [监控循环: dlc get job && dlc logs]     │   │     │   └─ LocalAPIRunner:     │      └─ Manager().Semaphore(concurrent_users)     │         └─ Pool(max_workers).apply_async()     │            └─ launch(task, tokens)     │               ├─ [重定向stdout/stderr]     │               ├─ OpenICLInferTask.run(monkey_patched)     │               │  └─ [注入tokens到model]     │               └─ [重置stdout/stderr]     │     └─> summarize(status)         ├─ [遍历status列表，统计失败任务]         ├─ [通过Lark发送通知]         └─ [打印日志] ```   `

#### 数据结构流

plaintext

`   ``` Input:  tasks: List[Dict[ConfigDict]]         ├─ models: List[ModelConfig]         ├─ datasets: List[DatasetConfig]         ├─ work_dir: str         └─ [其他配置]  ↓ [每个Runner的launch()]  GPU分配 (LocalRunner only):     gpus: np.array  [GPU可用计数]     gpu_ids: np.array  [分配给任务的GPU ID]  任务执行:     task.cfg → [dump] → param_file.py     ↓     task.get_command(param_file, template) → cmd     ↓     subprocess.run(cmd) → result.returncode  Output: status: List[Tuple[str, int]]         ├─ [0]: task.name         └─ [1]: exit_code (0 or non-zero)  Post-processing:     [统计失败数量]     ↓     [发送Lark通知] (可选) ```   `

#### 关键调用链

plaintext

`   ``` Partitioner.divide() → tasks_list     ↓ Runner.__call__(tasks_list)     ├─ launch(tasks_list)     │  └─ [多种实现]     │     ├─ 构建Task实例: TASKS.build({'cfg': task, 'type': task_cfg.type})     │     ├─ 获取GPU数: task.num_gpus     │     ├─ 获取输出路径: task.get_output_paths()     │     ├─ 生成命令: task.get_command(param_file, template)     │     └─ 执行命令: subprocess.run(cmd)     │     └─ summarize(status)        └─ [LarkReporter.post()] (可选) ```   `

---

### 第四步：错误处理和重试机制

#### LocalRunner

- **无重试机制**
- **错误标识**：返回码非0
- **日志记录**：stdout/stderr 保存到 `{out_path}`

#### SlurmRunner

**重试条件（行 140-151）：**

python

`   ``` while self._job_failed(return_code, output_paths) and retry > 0:     retry -= 1     # 刷新端口号以避免SLURM冲突     cmd = get_cmd()     result = subprocess.run(cmd, ...) ```   `

**_job_failed() 判断：**

python

`   ``` return return_code != 0 or not all(osp.exists(p) for p in output_paths) ```   `

**重试策略：**

- 失败时自动重新生成命令（可能端口号不同）
- 最多重试 `self.retry` 次（默认2次）

#### DLCRunner

**类似SLURM的重试机制：**

python

`   ``` return_code = _run_within_retry() retry = self.retry while self._job_failed(return_code, output_paths) and retry > 0:     retry -= 1     cmd = get_cmd()     return_code = _run_within_retry() ```   `

**额外的启动重试（行 244-256）：**

python

`   ``` num_retry_to_start = 5 index_to_start = 0 while index_to_start < num_retry_to_start:     try:         output = subprocess.getoutput(cmd)         match = re.search(r'\|\s+(dlc[0-9a-z]+)\s+\|', output)         if match:             job_id = match.group(1)             break     except BlockingIOError:         pass     index_to_start += 1 ```   `

如果无法解析job_id，最多重试5次

#### LocalAPIRunner

**错误处理（行 126-132）：**

python

`   ``` except Exception:     traceback.print_exc()     reset_std()     logger.error(f'task {task_name} fail, see\n{out_path}')     returncode = 1 ```   `

所有异常导致 returncode=1

---

## 报告 2：OpenCompass Task 模块分析

### 第一步：Task模块文件和功能概览

|文件名|代码行数|主要功能|核心类|
|---|---|---|---|
|`base.py`|120|Task基类定义|`BaseTask`|
|`openicl_infer.py`|180|推理任务实现|`OpenICLInferTask`|
|`openicl_eval.py`|570|评估任务实现|`OpenICLEvalTask`|
|`llm_eval.py`|92|LLM评估器|`ModelEvaluator`|
|`subjective_eval.py`|468|主观评估任务|`SubjectiveEvalTask`|
|`openicl_attack.py`|208|攻击任务（鲁棒性）|`OpenICLAttackTask`|
|`outer_eval/`|-|外部评估模块|-|

**文件路径：** `d:\project\opencompass_inner\opencompass\tasks\`

---

### 第二步：详细分析各类和方法

#### 1. BaseTask 基类

**文件：** `d:\project\opencompass_inner\opencompass\tasks\base.py` (行 43-120)

##### 类定义和属性

python

`   ``` class BaseTask:     """Base class for all tasks. Two execution modes:     1. Direct: task.run()     2. Subprocess: task.get_command() → shell     """          # 类属性     name_prefix: str = None     log_subdir: str = None     output_subdir: str = None ```   `

**属性说明：**

|属性|类型|作用|示例|
|---|---|---|---|
|`name_prefix`|str|任务名前缀|'OpenICLInfer'、'OpenICLEval'|
|`log_subdir`|str|日志文件子目录|'logs/infer'、'logs/eval'|
|`output_subdir`|str|输出文件子目录|'predictions'、'results'|

##### 初始化（行 60-65）

python

`   ``` def __init__(self, cfg: ConfigDict):     cfg = copy.deepcopy(cfg)     self.cfg = cfg     self.model_cfgs = cfg['models']     self.dataset_cfgs = cfg['datasets']     self.work_dir = cfg['work_dir'] ```   `

**参数表：**

|参数|类型|来源|作用|
|---|---|---|---|
|`cfg`|ConfigDict|Partitioner生成|完整任务配置|

**深拷贝的原因**：避免修改原始配置

##### 抽象方法

**方法1：run() - 行 67-69**

python

`   ``` @abstractmethod def run(self):     """Run the task.""" ```   `

**子类实现差异：**

- `OpenICLInferTask.run()`：执行模型推理
- `OpenICLEvalTask.run()`：评估模型预测
- `SubjectiveEvalTask.run()`：主观评估

**方法2：get_command() - 行 71-79**

python

`   ``` @abstractmethod def get_command(self, cfg_path, template) -> str:     """Get the command template for the task.          Args:         cfg_path (str): Path to config file         template (str): Template with '{task_cmd}' placeholder          Returns:         str: Full command to execute in shell     """ ```   `

**参数说明：**

|参数|类型|作用|
|---|---|---|
|`cfg_path`|str|序列化的ConfigDict文件路径（.py格式）|
|`template`|str|命令模板（由Runner提供），如 `'CUDA_VISIBLE_DEVICES=0 {task_cmd}'`|

**返回值**：完整shell命令

##### 属性方法

**方法：name - 行 81-87**

python

`   ``` @property def name(self) -> str:     return self.name_prefix + task_abbr_from_cfg({         'models': self.model_cfgs,         'datasets': self.dataset_cfgs     }) ```   `

**示例输出：**

- 'OpenICLInferqwen_plus_chat_7bmmlu'
- 'OpenICLEvalqwen_plus_chat_7bmmlu'

**方法：get_log_path() - 行 92-101**

python

`   ``` def get_log_path(self, file_extension: str = 'json') -> str:     return get_infer_output_path(         self.model_cfgs[0],          self.dataset_cfgs[0][0],         os.path.join(self.work_dir, self.log_subdir),         file_extension) ```   `

**参数表：**

|参数|类型|默认值|作用|
|---|---|---|---|
|`file_extension`|str|'json'|日志文件扩展名|

**返回格式：**

plaintext

`   ``` {work_dir}/logs/{task_type}/{model_abbr}/{dataset_abbr}.{ext} ```   `

**方法：get_output_paths() - 行 103-119**

python

`   ``` def get_output_paths(self, file_extension: str = 'json') -> List[str]:     """Get paths to output files. All should exist if task succeeds."""     output_paths = []     for model, datasets in zip(self.model_cfgs, self.dataset_cfgs):         for dataset in datasets:             output_paths.append(                 get_infer_output_path(                     model, dataset,                     os.path.join(self.work_dir, self.output_subdir),                     file_extension))     return output_paths ```   `

**返回值：** 所有输出文件路径列表

- 用于Runner验证任务成功（检查文件存在性）
- 长度 = len(models) × sum(len(datasets_per_model))

##### 辅助函数：extract_role_pred() - 行 12-40

python

`   ``` def extract_role_pred(s: str, begin_str: Optional[str],                        end_str: Optional[str]) -> str:     """Extract substring between begin_str and end_str."""     start = 0     end = len(s)          if begin_str and re.match(r'\s*', begin_str) is None:         begin_idx = s.find(begin_str)         if begin_idx != -1:             start = begin_idx + len(begin_str)          if end_str and re.match(r'\s*', end_str) is None:         end_idx = s.find(end_str, start)         if end_idx != -1:             end = end_idx          return s[start:end] ```   `

**用途**：从模型输出中提取特定角色的回复

---

#### 2. OpenICLInferTask 推理任务

**文件：** `d:\project\opencompass_inner\opencompass\tasks\openicl_infer.py` (行 21-180)

##### 类属性（行 27-29）

python

`   ``` name_prefix = 'OpenICLInfer' log_subdir = 'logs/infer' output_subdir = 'predictions' ```   `

##### 初始化（行 31-38）

python

`   ``` def __init__(self, cfg: ConfigDict):     super().__init__(cfg)     run_cfg = self.model_cfgs[0].get('run_cfg', {})     self.num_gpus = run_cfg.get('num_gpus', 0)     self.num_procs = run_cfg.get('num_procs', 1)     self.logger = get_logger()     self.dump_res_length = cfg.get('dump_res_length', False)     self.dump_only_message_path = cfg.get('dump_only_message_path', None) ```   `

**关键属性：**

|属性|类型|默认值|作用|
|---|---|---|---|
|`num_gpus`|int|0|任务所需GPU数|
|`num_procs`|int|1|分布式进程数|
|`dump_res_length`|bool|False|是否输出结果长度信息|
|`dump_only_message_path`|str|None|仅保存消息的路径|

##### get_command() - 行 40-65

python

`   ``` def get_command(self, cfg_path, template):     script_path = __file__     backend_keys = ['VLLM', 'Lmdeploy']     use_backend = any(         key in str(self.model_cfgs[0].get('type', ''))         or key in str(self.model_cfgs[0].get('llm', {}).get('type', ''))         for key in backend_keys)     python = sys.executable          if self.num_gpus > 1 and not use_backend:         # 多GPU分布式模式         port = random.randint(12000, 32000)         command = (             f'{python} -m torch.distributed.run --master_port={port} '             f'--nproc_per_node {self.num_procs} '             f'{script_path} {cfg_path}')     else:         # 单进程模式         command = f'{python} {script_path} {cfg_path}'          return template.format(task_cmd=command) ```   `

**逻辑决策树：**

plaintext

`   ``` num_gpus > 1 and not use_backend? ├─ YES → torch.distributed.run (--nproc_per_node {num_procs}) └─ NO  → 直接执行 python {script_path}  use_backend 检查: ├─ VLLM 后端 → 用官方启动器，无需torchrun └─ Lmdeploy 后端 → 用官方启动器，无需torchrun ```   `

##### run() 方法 - 行 67-103

**流程图：**

plaintext

`   ``` run(cur_model=None, cur_model_abbr=None)     │     └─ for model_cfg, dataset_cfgs in zip(models, datasets):        │        ├─ [跳过已存在结果]        │        ├─ if cur_model_abbr == model_abbr:        │  └─ 复用已加载模型        │ else:        │  └─ build_model_from_cfg(model_cfg)        │        └─ for dataset_cfg in dataset_cfgs:           │           ├─ build_dataset_from_cfg(dataset_cfg)           │           ├─ [检查输出文件是否存在]           │  └─ continue if exists           │           └─ _inference() ```   `

**参数表：**

|参数|类型|默认值|作用|
|---|---|---|---|
|`cur_model`|BaseModel|None|当前已加载模型（LocalRunner debug模式）|
|`cur_model_abbr`|str|None|当前模型简称|

**关键代码（行 67-89）：**

python

`   ``` def run(self, cur_model=None, cur_model_abbr=None):     self.logger.info(f'Task {task_abbr_from_cfg(self.cfg)}')     model_index, dataset_index = 0, 0          for model_cfg, dataset_cfgs in zip(self.model_cfgs, self.dataset_cfgs):         model_index += 1         self.max_out_len = model_cfg.get('max_out_len', None)         self.batch_size = model_cfg.get('batch_size', None)         self.min_out_len = model_cfg.get('min_out_len', None)                  # 模型复用逻辑         if cur_model and cur_model_abbr == model_abbr_from_cfg(model_cfg):             self.model = cur_model         else:             self.model = build_model_from_cfg(model_cfg) ```   `

**模型复用优化：**

- LocalRunner debug模式下，如果模型未变化，复用已加载实例
- 避免重复初始化大模型（节省内存和时间）
- 特别有用于多个数据集评估同一模型的场景

##### _inference() 方法 - 行 105-158_

**完整执行流程：**

python

`   ``` def _inference(self):     self.logger.info(f'Start inferencing {task_abbr_from_cfg(self.sub_cfg)}')          # 1. 构建提示模板     assert hasattr(self.infer_cfg, 'ice_template') or             hasattr(self.infer_cfg, 'prompt_template'), \         'Both cannot be None'          if hasattr(self.infer_cfg, 'ice_template'):         ice_template = ICL_PROMPT_TEMPLATES.build(             self.infer_cfg['ice_template'])          if hasattr(self.infer_cfg, 'prompt_template'):         prompt_template = ICL_PROMPT_TEMPLATES.build(             self.infer_cfg['prompt_template'])          # 2. 构建检索器     retriever_cfg = self.infer_cfg['retriever'].copy()     retriever_cfg['dataset'] = self.dataset     retriever = ICL_RETRIEVERS.build(retriever_cfg)          # 3. 构建推理器     inferencer_cfg = self.infer_cfg['inferencer']     inferencer_cfg['model'] = self.model          # 3.1 设置默认参数     self._set_default_value(inferencer_cfg, 'max_out_len', self.max_out_len)     self._set_default_value(inferencer_cfg, 'min_out_len', self.min_out_len)     self._set_default_value(inferencer_cfg, 'batch_size', self.batch_size)     inferencer_cfg['max_seq_len'] = self.model_cfg.get('max_seq_len')     inferencer_cfg['dump_res_length'] = self.dump_res_length     inferencer_cfg['dump_only_message_path'] = self.dump_only_message_path          inferencer = ICL_INFERENCERS.build(inferencer_cfg)          # 4. 执行推理     out_path = get_infer_output_path(...)     out_dir, out_file = osp.split(out_path)     mkdir_or_exist(out_dir)          # 4.1 根据配置调用不同的inference方法     if hasattr(self.infer_cfg, 'prompt_template') and \        hasattr(self.infer_cfg, 'ice_template'):         inferencer.inference(retriever,                            ice_template=ice_template,                            prompt_template=prompt_template,                            output_json_filepath=out_dir,                            output_json_filename=out_file)     elif hasattr(self.infer_cfg, 'prompt_template'):         inferencer.inference(retriever,                            prompt_template=prompt_template,                            output_json_filepath=out_dir,                            output_json_filename=out_file)     else:         inferencer.inference(retriever,                            ice_template=ice_template,                            output_json_filepath=out_dir,                            output_json_filename=out_file) ```   `

**推理管线架构：**

plaintext

`   ``` Dataset     ↓ Retriever (ICL_RETRIEVERS) ├─ 根据infer_cfg['retriever']配置 └─ 从dataset中检索上下文示例  PromptTemplate (ICL_PROMPT_TEMPLATES) ├─ ice_template: 示例模板 └─ prompt_template: 测试样本模板  Inferencer (ICL_INFERENCERS) ├─ 接收Model和PromptTemplate ├─ 合并检索结果和提示 └─ 调用model.generate()  Output: JSON文件 ├─ 文件位置: {work_dir}/predictions/{model}/{dataset}.json └─ 格式: {"0": {...}, "1": {...}, ...} ```   `

**_set_default_value() - 行 160-162**

python

`   ``` def _set_default_value(self, cfg: ConfigDict, key: str, value: Any):     if key not in cfg:         cfg[key] = value ```   `

**设计原则：** 配置文件的值优先于model_cfg的值

---

#### 3. OpenICLEvalTask 评估任务

**文件：** `d:\project\opencompass_inner\opencompass\tasks\openicl_eval.py` (行 28-433)

##### 类属性（行 36-38）

python

`   ``` name_prefix = 'OpenICLEval' log_subdir = 'logs/eval' output_subdir = 'results' ```   `

##### 初始化（行 40-64）

python

`   ``` def __init__(self, cfg: ConfigDict):     super().__init__(cfg)     self.logger = get_logger()          # 计算所需GPU数（取最大值）     self.num_gpus = max(         max(             c.get('eval_cfg', {}).get('num_gpus', 0),             c.get('eval_cfg', {}).get('evaluator', {}).get(                 'judge_cfg', {}).get('run_cfg', {}).get('num_gpus', 0),             c.get('eval_cfg', {}).get('evaluator', {}).get(                 'llm_evaluator', {}).get('judge_cfg', {}).get(                     'run_cfg', {}).get('num_gpus', 0),             next(iter(c.get('eval_cfg', {}).get('evaluator', {}).get(                 'judge_cfg', {}).get('judgers', [])), {}).get(                     'run_cfg', {}).get('num_gpus', 0))         for c in sum(self.dataset_cfgs, []))          self.num_procs = max(...)  # 类似逻辑     self.dump_details = cfg.get('eval', {}).get('runner', {}).get(...)     self.cal_extract_rate = cfg.get('eval', {}).get('runner', {}).get(...) ```   `

**GPU数计算策略：** 取所有eval_cfg中的最大值

- `eval_cfg.num_gpus`
- `evaluator.judge_cfg.run_cfg.num_gpus`
- `evaluator.llm_evaluator.judge_cfg.run_cfg.num_gpus`
- `judge_cfg.judgers[*].run_cfg.num_gpus`

##### run() 方法 - 行 80-98

python

`   ``` def run(self):     for model_cfg, dataset_cfgs in zip(self.model_cfgs, self.dataset_cfgs):         for dataset_cfg in dataset_cfgs:             self.model_cfg = model_cfg             self.dataset_cfg = dataset_cfg                          # 加载eval配置             self.eval_cfg = copy.deepcopy(dataset_cfg.get('eval_cfg'))             self.output_column = copy.deepcopy(                 dataset_cfg['reader_cfg']['output_column'])                          # 检查输出文件是否存在             out_path = get_infer_output_path(...)             if osp.exists(out_path):                 continue                          self._score() ```   `

##### _score() 方法 - 行 100-131_

**完整评估流程：**

python

`   ``` def _score(self):     # 1. 加载测试数据     test_set = self._load_and_preprocess_test_data()          # 2. 加载预测结果     pred_dicts, pred_strs = self._load_predictions()          # 3. 检查是否为rollout评估     if all(isinstance(item, dict) and 'rollout' in item for item in pred_strs):         # Rollout模式（用于强化学习）         result = self._sum_rollout(pred_strs, test_set, pred_dicts)     else:         # 标准评估模式         pred_strs = self._process_predictions(pred_strs)         result = self._evaluate_predictions(pred_strs, test_set, pred_dicts)          # 4. 保存结果     self._save_results(result) ```   `

**子方法详解：**

##### _load_and_preprocess_test_data() - 行 133-150

python

`   ``` def _load_and_preprocess_test_data(self):     """Load test dataset and apply postprocessing if needed."""     test_set = build_dataset_from_cfg(self.dataset_cfg).test          # 数据集级别后处理     if 'dataset_postprocessor' in self.eval_cfg:         kwargs = copy.deepcopy(self.eval_cfg['dataset_postprocessor'])         proc = kwargs.pop('type')         if isinstance(proc, str):             proc = TEXT_POSTPROCESSORS.get(proc)                  def postprocess(sample):             s = sample[self.output_column]             sample[self.output_column] = proc(s, **kwargs)             return sample                  test_set = test_set.map(postprocess)          return test_set ```   `

**后处理流程：**

plaintext

`   ``` 原始数据集     ↓ [可选] dataset_postprocessor     ├─ 从registry获取处理器     ├─ 对输出列应用处理     └─ 返回修改后的数据集 ```   `

##### _load_predictions() - 行 152-193

python

`   ``` def _load_predictions(self):     """Load model predictions from files."""     filename = get_infer_output_path(...)          # 处理分割文件（大数据集推理可能被分割）     root, ext = osp.splitext(filename)     partial_filename = root + '_0' + ext          if osp.exists(filename):         preds = mmengine.load(filename)         preds = [preds[str(i)] for i in range(len(preds))]     else:         # 加载多个分割文件         preds = []         i = 1         filename = partial_filename         while osp.exists(filename):             sub_preds = mmengine.load(filename)             preds.extend([sub_preds[str(i)] for i in range(len(sub_preds))])             filename = root + f'_{i}' + ext             i += 1          pred_dicts = copy.deepcopy(preds)          # 重新组织为字典格式     preds = {k: [pred.get(k) for pred in preds] for k in preds[0]}     pred_strs = preds.pop('prediction', None)          return pred_dicts, pred_strs ```   `

**文件格式：**

plaintext

`   ``` 单文件模式: {work_dir}/predictions/model/dataset.json     格式: {"0": {...}, "1": {...}, ...}  分割文件模式: {work_dir}/predictions/model/dataset_0.json, _1.json, ...     原因: 大数据集推理时分批保存     加载时: 合并所有分割文件 ```   `

**返回值转换：**

plaintext

`   ``` Input:  [{"prediction": "A", "gold": ["A"]},           {"prediction": "B", "gold": ["B"]}, ...]  ↓ [重新组织]  Output: pred_dicts: 原始列表         pred_strs: [pred["prediction"] for pred in preds]                  = ["A", "B", ...] ```   `

##### _process_predictions() - 行 195-252

**多步处理流程：**

plaintext

`   ``` 1. 角色提取 (如果需要)    ├─ 解析model_cfg.meta_template    ├─ 使用extract_role_pred()提取指定角色的输出    └─ 例如: "Assistant: A" → "A"  2. 模型级别后处理    ├─ 使用model_cfg['pred_postprocessor']    ├─ 例如: 去除尾部空白    └─ 支持pred_list_flag（多选题的多个预测）  3. 数据集级别后处理    ├─ 使用eval_cfg['pred_postprocessor']    └─ 例如: 文本规范化 ```   `

**关键代码（行 202-224）：**

python

`   ``` if 'pred_role' in self.eval_cfg and 'meta_template' in self.model_cfg:     parser = LMTemplateParser(self.model_cfg['meta_template'])     role = parser.roles[self.eval_cfg['pred_role']]          if pred_list_flag:         pred_strs = [[             extract_role_pred(                 _pred,                 role.get('begin', None),                 role.get('end', None),             ) for _pred in pred         ] for pred in pred_strs]     else:         pred_strs = [             extract_role_pred(                 pred,                 role.get('begin', None),                 role.get('end', None),             ) for pred in pred_strs         ] ```   `

##### _evaluate_predictions() - 行 254-346

**完整评估流程：**

python

`   ``` def _evaluate_predictions(self, pred_strs, test_set, pred_dicts):     # 1. 获取参考答案     references = (None if self.output_column is None else                   [sample[self.output_column] for sample in test_set])          # 2. 获取评估器     evaluator_cfg = self.eval_cfg.get('evaluator', {})     evaluator_type = evaluator_cfg.get('type')     if isinstance(evaluator_type, str):         evaluator_type = ICL_EVALUATORS.get(evaluator_type)          # 3. 初始化评估器     evaluator_cfg_copy = copy.deepcopy(evaluator_cfg)     evaluator_cfg_copy.pop('type', None)     sig = signature(evaluator_type)     if 'predictions' in sig.parameters and 'references' in sig.parameters:         evaluator = evaluator_type(             predictions=pred_strs,             references=references,             **evaluator_cfg_copy,         )     else:         evaluator = evaluator_type(**evaluator_cfg_copy)          # 4. 设置输出目录     out_path = get_infer_output_path(...)     evaluator._out_dir = osp.splitext(out_path)[0]          # 5. 准备评估参数     if pred_dicts:         preds = {k: [pred.get(k) for pred in pred_dicts]                  for k in pred_dicts[0]}          preds['predictions'] = pred_strs     preds['references'] = test_set[self.output_column] if self.output_column else None     preds['test_set'] = test_set     if 'origin_prompt' not in preds:         try:             preds['origin_prompt'] = [None for _ in range(len(pred_strs))]         except TypeError:             preds['origin_prompt'] = None          # 过滤参数：只传递evaluator.score()需要的参数     preds = {k: preds[k] for k in signature(evaluator.score).parameters}          # 6. 调用评估     k = self.dataset_cfg.get('k', 1)     n = self.dataset_cfg.get('n', 1)     result = evaluator.evaluate(k, n, copy.deepcopy(test_set), **preds)          # 7. 详细结果处理     if self.dump_details:         details = result.get('details', None)         if details is None:             result['details'] = self.format_details(...)             if self.cal ```   `