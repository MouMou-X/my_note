让我查看代码中如何解析这个输出格式并生成问题：
现在让我为你详细解释整个解析和问题生成的流程：

---

## 从LLM输出提取信息并生成问题的完整逻辑

### 1. LLM原始输出格式

```
Character 1
Name: Sarah
Role: The Barista
Motivation: Sarah wants to make Luis an almond milk coffee.

Character 2
Name: Luis
Role: A customer
Motivation: Luis is having a rough week...

Character 3
Name: John
Role: A cafe worker
Motivation: John is having his first day...

Story outline:
Luis was having a super hard week...

Moves:

Move 1 - Luis moves the almond milk from the fridge to the back shelves.
Mover: Luis
Item: almond milk
From: fridge
To: back shelves
Reason - Luis is cleaning the fridge...

Move 2 - ...
Move 3 - ...
```

---

### 2. 解析代码逻辑 (L290-343)

```python
# 初始化数据容器
items = []           # 物品列表
people = []          # 人物列表
people_data = []     # 人物详细信息
moves = []           # 移动数据
move_strs = []       # 移动描述字符串
locations = []       # 位置列表
world_state = []     # 物品初始位置

# 按空行分割输出
lines = output.split('\n\n')
```

#### 2.1 解析角色信息 (L302-309)

```python
# lines[0:3] 是三个角色段落
for c in lines[0:3]:
    info = c.split('\n')
    # info = ['Character 1', 'Name: Sarah', 'Role: The Barista', 'Motivation: ...']
    
    people_data.append({
        'name': info[1].replace('Name: ', ''),        # 'Sarah'
        'role': info[2].replace('Role: ', ''),        # 'The Barista'
        'motivation': info[3].replace('Motivation: ', '')  # '...'
    })
    people.append(info[1].replace('Name: ', ''))  # ['Sarah', 'Luis', 'John']
```

**抽象出的数据结构：**
```python
people_data = [
    {'name': 'Sarah', 'role': 'The Barista', 'motivation': '...'},
    {'name': 'Luis', 'role': 'A customer', 'motivation': '...'},
    {'name': 'John', 'role': 'A cafe worker', 'motivation': '...'}
]
people = ['Sarah', 'Luis', 'John']
```

#### 2.2 解析故事大纲 (L311)

```python
story_desc = lines[3].replace('Story outline:\n','').replace('Story Outline:\n','')
# story_desc = "Luis was having a super hard week..."
```

#### 2.3 解析移动信息 (L313-339)

```python
# lines[5:] 是移动段落
for move_info in lines[5:]:
    m = move_info.split('\n')
    # m = ['Move 1 - ...', 'Mover: Luis', 'Item: almond milk', 'From: fridge', 'To: back shelves', 'Reason - ...']
    
    move_data = {
        'mover': m[1].replace('Mover: ', ''),           # 'Luis'
        'item': m[2].replace('Item: ', ''),             # 'almond milk'
        'from': m[3].replace('From: ', ''),             # 'fridge'
        'to': m[4].replace('To: ', ''),                 # 'back shelves'
        'justification': m[5].replace('Reason - ', '') # '...'
    }
    
    moves.append(move_data)
    locations.extend([move_data['from'], move_data['to']])
    items.append(move_data['item'])
    
    # 记录物品初始位置
    if move_data['item'] not in [x[0] for x in world_state]:
        world_state.append([move_data['item'], move_data['from']])
```

**抽象出的数据结构：**
```python
moves = [
    {'mover': 'Luis', 'item': 'almond milk', 'from': 'fridge', 'to': 'back shelves', 'justification': '...'},
    {'mover': 'Sarah', 'item': 'coffee bag', 'from': 'back shelves', 'to': 'front counter', 'justification': '...'},
    {'mover': 'Sarah', 'item': 'almond milk', 'from': 'back shelves', 'to': 'fridge', 'justification': '...'}
]

items = ['almond milk', 'coffee bag']  # 去重排序后
locations = ['back shelves', 'fridge', 'front counter']  # 去重排序后
world_state = [['almond milk', 'fridge'], ['coffee bag', 'back shelves']]  # 初始位置
```

---

### 3. 生成信念状态 - create_sequence_v2 (L364-366)
[[MuSR物品放置函数模拟整个移动过程]]
```python
events, beliefs, actual_locs, event_structure = creator.create_sequence_v2(
    items, locations, people,
    max_sequence_length=3,
    chance_subject_sees=0.33,  # 33%概率看到
    initial_starting_positions=world_state
)
```

这个函数模拟整个移动过程，追踪：

```python
# beliefs 结构 - 每个时间点每个人对每个物品的认知
beliefs = [
    # 时间0: 初始状态，所有人都知道
    {'Sarah': {'almond milk': 'fridge', 'coffee bag': 'back shelves'},
     'Luis': {'almond milk': 'fridge', 'coffee bag': 'back shelves'},
     'John': {'almond milk': 'fridge', 'coffee bag': 'back shelves'}},
    
    # 时间1: Luis移动了almond milk
    # 假设Sarah没看到，John看到了
    {'Sarah': {'almond milk': 'fridge', 'coffee bag': 'back shelves'},  # Sarah还认为在fridge!
     'Luis': {'almond milk': 'back shelves', 'coffee bag': 'back shelves'},
     'John': {'almond milk': 'back shelves', 'coffee bag': 'back shelves'}},
    
    # 时间2: ...
    # 时间3: ...
]

# event_structure - 记录每个事件的观察状态
event_structure = [
    {'event': 'opening scene', 
     'immutable_sequence': ['Sarah sees the almond milk at the fridge.', ...],
     'sequence': []},
    {'event': 'Luis moves the almond milk to the back shelves.',
     'immutable_sequence': [],
     'sequence': ['Sarah did not see the almond milk move...', 'John saw the almond milk move...']}
]
```

---

### 4. 问题生成 - generate_end_questions (L381-383)

```python
question, answers = creator.generate_end_questions(
    ending_beliefs=beliefs[-1],  # 最终信念状态
    people=people,
    items=items,
    locations=locations,
    event_structure=event_structure
)
```

**生成逻辑 (L208-252)：**

```python
def generate_end_questions(ending_beliefs, people, items, locations, event_structure):
    
    # 步骤1: 找出每个物品的最后移动者（他们肯定知道位置，不用问）
    last_moves = []
    for item in items:
        for event in reversed(event_structure):
            if item.lower() in event['event'].lower():
                for person in people:
                    if person.lower() in event['event'].lower().split(' ')[0]:
                        last_moves.append([person, item])
                        break
                break
    # last_moves = [['Sarah', 'almond milk'], ['Sarah', 'coffee bag']]
    # (Sarah最后移动了两个物品)
    
    # 步骤2: 为每个"非最后移动者"生成问题
    questions = []
    answers = []
    for person in people:
        for item in items:
            if [person, item] in last_moves:
                continue  # 跳过：Sarah不会被问almond milk和coffee bag
            
            # 生成问题
            q = f'Which location is the most likely place {person} would look to find the {item.lower()} given the story?'
            questions.append(q)
            
            # 答案：该角色的信念状态中物品的位置
            answers.append(locations.index(ending_beliefs[person][item]))
    
    return questions, answers
```

---

### 5. 完整数据流图

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        LLM生成的原始文本                                  │
│  (角色1-3, 故事大纲, 移动1-3)                                             │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ split('\n\n')
┌─────────────────────────────────────────────────────────────────────────┐
│                          字符串解析                                       │
├─────────────────────────────────────────────────────────────────────────┤
│  people_data: [{name, role, motivation}, ...]                          │
│  people: ['Sarah', 'Luis', 'John']                                     │
│  items: ['almond milk', 'coffee bag']                                  │
│  locations: ['back shelves', 'fridge', 'front counter']                │
│  moves: [{mover, item, from, to, justification}, ...]                  │
│  world_state: [[item, initial_location], ...]                          │
│  story_desc: "Luis was having a super hard week..."                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ create_sequence_v2()
┌─────────────────────────────────────────────────────────────────────────┐
│                        模拟移动 + 追踪信念                                │
├─────────────────────────────────────────────────────────────────────────┤
│  对于每次移动:                                                           │
│    1. 移动者更新信念 (知道新位置)                                         │
│    2. 其他人按33%概率决定是否看到                                         │
│    3. 看到 → 更新信念，没看到 → 保持旧信念                                │
├─────────────────────────────────────────────────────────────────────────┤
│  输出:                                                                  │
│    events: 每个时间点的事件列表                                           │
│    beliefs: 每个时间点每人对每物品的位置认知                               │
│    actual_locs: 每个时间点物品的实际位置                                  │
│    event_structure: 结构化的事件+观察状态                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ generate_end_questions()
┌─────────────────────────────────────────────────────────────────────────┐
│                          问题生成                                        │
├─────────────────────────────────────────────────────────────────────────┤
│  1. 找出每个物品的最后移动者 → 排除在问题之外                              │
│  2. 遍历 (人, 物品) 组合                                                 │
│  3. 问题: "X最可能去哪里找Y?"                                            │
│  4. 答案: beliefs[-1][X][Y] 的索引                                      │
├─────────────────────────────────────────────────────────────────────────┤
│  示例输出:                                                               │
│  questions = [                                                          │
│    "Which location is the most likely place Luis would look to find     │
│     the almond milk given the story?",                                  │
│    "Which location is the most likely place John would look to find     │
│     the coffee bag given the story?",                                   │
│    ...                                                                  │
│  ]                                                                      │
│  answers = [1, 0, ...]  # locations列表中的索引                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 6. 问题生成的核心逻辑

| 条件 | 结果 |
|------|------|
| 某人是某物品的**最后移动者** | **不生成问题**（他肯定知道在哪） |
| 某人**看到了**物品移动 | 答案 = 物品的**新位置** |
| 某人**没看到**物品移动 | 答案 = 该人**以为**的位置（可能是旧位置） |

**示例：**
- Sarah最后移动了almond milk → 不问Sarah关于almond milk
- Luis没看到Sarah移动almond milk回fridge → 问Luis，答案是"back shelves"（他以为的位置）
- John看到了 → 问John，答案是"fridge"（实际位置）