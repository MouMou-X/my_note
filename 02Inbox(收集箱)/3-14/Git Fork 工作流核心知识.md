# Git Fork 工作流核心知识

#git #github #版本控制

---

## 远程仓库别名

- `origin` — clone 时 Git **自动**创建，指向你有写权限的仓库（通常是你的 fork）
- `upstream` — 需**手动添加**，约定俗成地指向原始上游仓库
- 别名只是 URL 的快捷方式，名字可任意取，`upstream` 只是惯例

```bash
git remote add upstream https://github.com/原作者/仓库.git
git remote -v   # 查看所有远程及其 fetch/push 地址
```

---

## fork vs branch

|概念|位置|本质|
|---|---|---|
|fork|GitHub 账号下|独立的仓库副本，有自己的 URL|
|branch|某个仓库内部|同一仓库内的开发线|

> fork 不是分支。fork 之后才 clone，clone 之后才建分支。

---

## `git fetch` 的边界

- **只下载**远程最新信息到本地，**不修改**任何工作文件
- 更新的是 **remote-tracking branches**（远程跟踪分支），如 `upstream/main`
- 这些跟踪分支是"远程状态的本地快照"，不是你的工作分支

```bash
git fetch upstream
# 此时 upstream/main 已更新，但你本地 main 分支未动
```

---

## remote-tracking branches

- 形如 `upstream/main`、`origin/dev`
- 只读引用，像书签，记录"上次联系远程时，那边各分支在哪"
- 不能直接在上面提交，需 merge 或 checkout 到本地分支

---

## `fetch` vs `merge` vs `pull`

|命令|作用|
|---|---|
|`git fetch`|下载远程数据，不合并|
|`git merge upstream/main`|将跟踪分支合并进当前分支|
|`git pull`|`fetch` + `merge` 的合并操作|

---

## push 的方向

- 只能向有写权限的仓库 push → 通常只能 push 到 `origin`（自己的 fork）
- **不能** push 到 `upstream`（没有写权限）
- 想把改动提交给官方 → 在 GitHub 上发起 **Pull Request**

---

## `git clone` 做了什么

1. 把远程仓库完整复制到本地
2. 自动将该远程地址命名为 `origin`
3. 自动 checkout 默认分支（通常是 `main`）

---

## 同步 fork 与上游的标准操作

```bash
git checkout main
git fetch upstream          # 下载官方最新
git merge upstream/main     # 合并到本地 main
git push origin main        # 推回自己的 fork
```

---

## 相关命令速查

```bash
git remote add <name> <url>   # 新增远程别名
git remote -v                 # 查看所有远程
git remote remove <name>      # 删除别名
git fetch <remote>            # 从指定远程下载
git branch -r                 # 查看所有远程跟踪分支
```

---

## 关联笔记

- [[Git 基础操作]]
- [[GitHub Pull Request 流程]]
- [[分支管理策略]]