---
title: 如何操作文本数据 — pandas 3.0.2 文档
source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html#min-tut-10-text
author:
published:
created: 2026-04-11
description:
tags:
  - clippings
---
```
In [1]: import pandas as pd
```

- 泰坦尼克号数据
	本教程使用泰坦尼克号数据集，该数据集以 CSV 格式存储。数据包含以下列：
	- PassengerId：每位乘客的ID。
	- 幸存情况：指示乘客是否幸存。 `0` 否表示幸存， `1` 是表示幸存。
	- Pclass：三种票级之一：Class 1 `1` 、Class 2 `2` 和 Class 3 `3` 。
	- 姓名：乘客姓名。
	- 性别：乘客的性别。
	- 年龄：乘客的年龄（以岁为单位）。
	- SibSp：船上兄弟姐妹或配偶的数量。
	- 乘客人数：船上家长或儿童的人数。
	- 车票：乘客的车票号码。
	- 票价：表示票价。
	- 舱位：乘客的舱位编号。
	- 登船：登船港。
	```
	In [2]: titanic = pd.read_csv("data/titanic.csv")
	In [3]: titanic.head()
	Out[3]: 
	   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
	0            1         0       3  ...   7.2500   NaN         S
	1            2         1       1  ...  71.2833   C85         C
	2            3         1       3  ...   7.9250   NaN         S
	3            4         1       1  ...  53.1000  C123         S
	4            5         0       3  ...   8.0500   NaN         S
	[5 rows x 12 columns]
	```

## 如何处理文本数据

- 将所有名称字符改为小写。
	```
	In [4]: titanic["Name"].str.lower()
	Out[4]: 
	0                                braund, mr. owen harris
	1      cumings, mrs. john bradley (florence briggs th...
	2                                  heikkinen, miss laina
	3           futrelle, mrs. jacques heath (lily may peel)
	4                               allen, mr. william henry
	                             ...                        
	886                                montvila, rev. juozas
	887                          graham, miss margaret edith
	888              johnston, miss catherine helen "carrie"
	889                                behr, mr. karl howell
	890                                  dooley, mr. patrick
	Name: Name, Length: 891, dtype: str
	```
	要将列中的每个字符串转换 `Name` 为小写，请选择该 `Name` 列（参见 [数据选择教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset) ），添加 `str` 访问器并应用该 `lower` 方法。这样，每个字符串都会逐个元素进行转换。

[与时间序列教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html#min-tut-09-timeseries) 中日期时间对象 具有访问器 类似 `dt` ，使用该访问器时可以使用一些专门的字符串方法。这些方法通常与用于单个元素的等效内置字符串方法名称相同，但它们是逐元素地应用于 列的每个值 `str` （还记得 [逐元素计算吗？）。](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html#min-tut-05-columns)

- 创建一个新列 `Surname` ，其中包含乘客的姓氏，方法是提取逗号之前的部分。
	```
	In [5]: titanic["Name"].str.split(",")
	Out[5]: 
	0                             [Braund,  Mr. Owen Harris]
	1      [Cumings,  Mrs. John Bradley (Florence Briggs ...
	2                               [Heikkinen,  Miss Laina]
	3        [Futrelle,  Mrs. Jacques Heath (Lily May Peel)]
	4                            [Allen,  Mr. William Henry]
	                             ...                        
	886                             [Montvila,  Rev. Juozas]
	887                       [Graham,  Miss Margaret Edith]
	888           [Johnston,  Miss Catherine Helen "Carrie"]
	889                             [Behr,  Mr. Karl Howell]
	890                               [Dooley,  Mr. Patrick]
	Name: Name, Length: 891, dtype: object
	```
	使用该 [`Series.str.split()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html#pandas.Series.str.split "pandas.Series.str.split") 方法，每个值都会返回一个包含两个元素的列表。第一个元素是逗号之前的部分，第二个元素是逗号之后的部分。
	```
	In [6]: titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
	In [7]: titanic["Surname"]
	Out[7]: 
	0         Braund
	1        Cumings
	2      Heikkinen
	3       Futrelle
	4          Allen
	         ...    
	886     Montvila
	887       Graham
	888     Johnston
	889         Behr
	890       Dooley
	Name: Surname, Length: 891, dtype: object
	```
	由于我们只对代表姓氏的第一部分（元素 0）感兴趣，我们可以再次使用 `str` 访问器并应用 [`Series.str.get()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html#pandas.Series.str.get "pandas.Series.str.get") 来提取相关部分。实际上，这些字符串函数可以连接起来，一次性组合多个函数！

用户指南

有关提取字符串部分的更多信息，请参阅用户指南中关于 [拆分和替换字符串的部分](https://pandas.pydata.org/docs/user_guide/text.html#text-split) 。

- 提取泰坦尼克号上伯爵夫人的乘客数据。
	```
	In [8]: titanic["Name"].str.contains("Countess")
	Out[8]: 
	0      False
	1      False
	2      False
	3      False
	4      False
	       ...  
	886    False
	887    False
	888    False
	889    False
	890    False
	Name: Name, Length: 891, dtype: bool
	```
	```
	In [9]: titanic[titanic["Name"].str.contains("Countess")]
	Out[9]: 
	     PassengerId  Survived  Pclass  ... Cabin Embarked  Surname
	759          760         1       1  ...   B77        S   Rothes
	[1 rows x 13 columns]
	```
	（ *对她的故事感兴趣？请看* [维基百科](https://en.wikipedia.org/wiki/No%C3%ABl_Leslie,_Countess_of_Rothes) *！* ）
	字符串方法 [`Series.str.contains()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains "pandas.Series.str.contains") 会检查列中的每个值 `Name` 是否包含该单词 `Countess` ，并为每个值返回 `True` “ `Countess` 是”或 `False` “ `Countess` 不是”。此输出可用于使用条件（布尔）索引对数据进行子集选择，该索引在 [数据子集教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset) 中已介绍。由于泰坦尼克号上只有一位伯爵夫人，因此我们得到一行结果。

> [!note] 笔记
> 支持对字符串进行更强大的提取，因为 [`Series.str.contains()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains "pandas.Series.str.contains") and [`Series.str.extract()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract "pandas.Series.str.extract") 方法接受 [正则表达式](https://docs.python.org/3/library/re.html) ，但这超出了本教程的范围。

用户指南

有关提取字符串部分的更多信息，请参阅用户指南中的 [字符串匹配和提取部分](https://pandas.pydata.org/docs/user_guide/text.html#text-extract) 。

- 泰坦尼克号上哪位乘客的名字最长？
	```
	In [10]: titanic["Name"].str.len()
	Out[10]: 
	0      23
	1      51
	2      21
	3      44
	4      24
	       ..
	886    21
	887    27
	888    39
	889    21
	890    19
	Name: Name, Length: 891, dtype: int64
	```
	为了获取最长名称，我们首先需要获取列中每个名称的长度 `Name` 。通过使用 pandas 字符串方法，该 [`Series.str.len()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#pandas.Series.str.len "pandas.Series.str.len") 函数会逐个（逐元素地）应用于每个名称。
	```
	In [11]: titanic["Name"].str.len().idxmax()
	Out[11]: 307
	```
	接下来，我们需要获取表中名称长度最长的对应位置，最好是索引标签。该 [`idxmax()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "pandas.Series.idxmax") 方法正是用于此目的。它不是字符串方法，而是应用于整数，因此无需 `str` 使用任何参数。
	```
	In [12]: titanic.loc[titanic["Name"].str.len().idxmax(), "Name"]
	Out[12]: 'Penasco y Castellana, Mrs. Victor de Satode (Maria Josefa Perez de Soto y Vallejo)'
	```
	根据行（ `307` ）和列（ ）的索引名称，我们可以使用 [子集教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset) 中介绍的运算符 `Name` 进行选择 。 `loc`
- 在“性别”列中，将“男性”的值替换为“M”，将“女性”的值替换为“F”。
	```
	In [13]: titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
	In [14]: titanic["Sex_short"]
	Out[14]: 
	0      M
	1      F
	2      F
	3      F
	4      M
	      ..
	886    M
	887    F
	888    F
	889    M
	890    M
	Name: Sex_short, Length: 891, dtype: str
	```
	虽然 [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace "pandas.Series.replace") 它不是一个字符串方法，但它提供了一种便捷的方式来使用映射或词汇表来转换某些值。它需要一个 `dictionary` 来定义映射 。 `{from: to}`

> [!warning] 警告
> 此外，还有一种 [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html#pandas.Series.str.replace "pandas.Series.str.replace") 方法可以用来替换特定的字符集。但是，当映射多个值时，这种方法会变成：
> 
> ```
> titanic["Sex_short"] = titanic["Sex"].str.replace("female", "F")
> titanic["Sex_short"] = titanic["Sex_short"].str.replace("male", "M")
> ```
> 
> 这样做会变得很麻烦，而且很容易出错。想想看（或者自己试一试），如果把这两个陈述的顺序颠倒过来会发生什么……

#### 记住

- 可以使用 `str` 访问器访问字符串方法。
- 字符串方法逐元素操作，可用于条件索引。
- 该 `replace` 方法是一种根据给定字典转换值的便捷方法。

用户指南

用户指南页面中提供了关于 [处理文本数据的](https://pandas.pydata.org/docs/user_guide/text.html#text) 完整概述。