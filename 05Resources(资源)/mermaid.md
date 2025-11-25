---
日期: 2025-06-24
tags:
  - "#markdown"
  - "#mermaid"
url: http://mermaid.js.org/intro/
---


# 概述
## Mermaid：将文本被转化为图表的利器
Mermaid，作为一个强大的 JavaScript 图表库，正在彻底改变开发者、文档撰写者和项目经理创建和维护图表的方式。它以其 “代码即图表” (diagrams as code) 的理念，允许用户使用类似 Markdown 的简单文本语法，轻松生成各种复杂的图表和可视化内容。从流程图、序列图到甘特图和状态图，Mermaid 都能将纯文本描述渲染成清晰、美观的矢量图形。

# 分类
| 图表类型                   | 英文名称                        | 描述                           |
| :--------------------- | :-------------------------- | :--------------------------- |
| [流程图](mermaid.md#流程图)     | Flowchart                   | 用于表示工作流程、算法或决策过程。            |
| [序列图](mermaid.md#序列图)     | Sequence Diagram            | 展示对象之间交互的时间顺序。               |
| [甘特图](mermaid.md#甘特图)     | Gantt Chart                 | 用于项目管理，展示任务的排期和进度。           |
| [类图](mermaid.md#类图)       | Class Diagram               | 在面向对象设计中，描述类的结构和关系。          |
| [状态图](mermaid.md#状态图)     | State Diagram               | 描述对象在其生命周期内所经历的各种状态以及状态间的转换。 |
| [饼图](mermaid.md#饼图)       | Pie Chart                   | 用于展示各部分占整体的比例。               |
| [用户旅程图](mermaid.md#用户旅程图) | User Journey Diagram        | 描绘用户在使用产品或服务过程中的体验和步骤。       |
| [实体关系图](mermaid.md#实体关系图) | Entity Relationship Diagram | 用于数据库设计，展示实体、属性以及它们之间的关系。    |
| [象限图](mermaid.md#象限图)     | Quadrant chart              |                              |
|                        |                             |                              |
## 图表类型
### 流程图
- 流程图用于展示一个过程或工作流。这个例子描绘了一个简单的用户登录验证流程。
```mermaid
graph LR
    A[用户打开登录页面] --> B{输入用户名和密码};
    B --> C[点击登录按钮];
    C --> D{后台验证};
    D -- 验证成功 --> E[跳转到用户主页];
    D -- 验证失败 --> F[提示登录失败];
    F --> B;
```
### 序列图
- 序列图用于展示对象之间按时间顺序的交互。这个例子展示了学生向图书馆借书的过程。
```mermaid
sequenceDiagram
    participant 学生
    participant 图书馆系统
    participant 数据库

    学生->>图书馆系统: 查询《Mermaid入门》
    activate 图书馆系统
    图书馆系统->>数据库: 检索书籍库存
    activate 数据库
    数据库-->>图书馆系统: 返回库存信息 (有库存)
    deactivate 数据库
    图书馆系统-->>学生: 显示书籍可借阅
    deactivate 图书馆系统

    学生->>图书馆系统: 确认借阅
    activate 图书馆系统
    图书馆系统->>数据库: 更新书籍状态为“已借出”
    activate 数据库
    数据库-->>图书馆系统: 更新成功
    deactivate 数据库
    图书馆系统-->>学生: 借阅成功，请取书
    deactivate 图书馆系统
```
### 甘特图
- 甘特图是项目管理的常用工具，用于展示任务的时间安排。
```mermaid
gantt
    title 网站开发项目计划
    dateFormat YYYY-MM-DD
    excludes weekends

    section 规划阶段
    市场调研     :done,    task1, 2025-06-23, 5d
    需求规格书   :active,  task2, after task1, 7d

    section 开发阶段
    前端开发     :         task3, after task2, 20d
    后端开发     :         task4, after task2, 25d

    section 测试与上线
    集成测试     :         task5, after task4, 5d
    用户验收测试 :         task6, after task5, 3d
    正式上线     :         crit, task7, after task6, 1d
```
### 类图
- 类图用于描述系统的静态结构，包括类、属性、方法以及它们之间的关系。
```mermaid
classDiagram
    class Animal {
      -String name
      +eat()
      +sleep()
      +makeSound()
    }

    class Dog {
      +bark()
    }

    class Cat {
      +meow()
    }

    class Duck {
      +quack()
    }

    Animal <|-- Dog
    Animal <|-- Cat
    Animal <|-- Duck

    class Zoo {
        -List<Animal> animals
        +addAnimal(Animal animal)
    }

    Zoo o-- Animal : houses
```
### 状态图
- 状态图用于描述一个对象在其生命周期内所经历的状态以及触发状态转换的事件。
```mermaid
stateDiagram-v2
    [*] --> Off : Power Off

    state On {
        [*] --> Idle
        Idle --> Playing : play_button_pressed
        Playing --> Paused : pause_button_pressed
        Paused --> Playing : play_button_pressed
    }

    On --> Off : power_button_pressed
```
### 饼图
- 饼图用于直观地展示各部分占整体的比例。
```mermaid
pie
    title 移动操作系统市场份额 (2025)
    "Android" : 70.5
    "iOS" : 28.5
    "其他" : 1.0
```
### 用户旅行图
- 用户旅程图描绘了用户为实现某个目标而与产品或服务进行交互的完整过程。
```mermaid
journey
    title 我的在线购物之旅
    section 发现与选购
      浏览商品: 5: 我, 小红书推荐
      进入App搜索: 4: 我
      比较商品: 5: 我, 家人
    section 下单与支付
      加入购物车: 5: 我
      选择支付方式: 3: 我, 支付系统
      完成支付: 5: 我
    section 等待与收货
      等待快递: 3: 我
      收到包裹: 5: 我, 快递员
```
### 实体关系图
- 实体关系图（ERD）用于数据库设计，展示实体、属性以及它们之间的关系。
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER {
        string name
        string email
        string address
    }
    ORDER {
        int orderId
        string orderDate
        string deliveryAddress
    }
    LINE-ITEM {
        string productCode
        int quantity
        float price
    }
```
### 象限图
```mermaid
    quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    Campaign A: [0.3, 0.6]
    Campaign B: [0.45, 0.23]
    Campaign C: [0.57, 0.69]
    Campaign D: [0.78, 0.34]
    Campaign E: [0.40, 0.34]
    Campaign F: [0.35, 0.78]
```
