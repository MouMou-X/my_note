---
title: "入门指南 — pandas 3.0.2 文档"
source: "https://pandas.pydata.org/docs/getting_started/index.html#getting-started"
author:
published:
created: 2026-04-11
description:
tags:
  - "clippings"
---
## 入门

## 安装

```bash
conda install -c conda-forge pandas
```

更喜欢点对点吗？

```bash
pip install pandas
```

详细说明？

## pandas入门

处理表格数据（例如存储在电子表格或数据库中的数据）时，pandas 是您的理想工具。pandas 可以帮助您探索、清理和处理数据。在 pandas 中，数据表被称为 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 。

![../_images/01_table_dataframe.svg](https://pandas.pydata.org/docs/_images/01_table_dataframe.svg)

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#min-tut-01-tableoriented)

[用户指南](https://pandas.pydata.org/docs/user_guide/dsintro.html#dsintro)

pandas 开箱即用地支持多种文件格式或数据源（csv、excel、sql、json、parquet 等）。使用带有 \`import\` 前缀的函数可以从这些数据源导入数据 `read_*` 。类似地， `to_*` 使用 \`store\` 方法可以存储数据。

![../_images/02_io_readwrite.svg](https://pandas.pydata.org/docs/_images/02_io_readwrite.svg)

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write)

[用户指南](https://pandas.pydata.org/docs/user_guide/io.html#io)

需要选择或筛选特定行和/或列？需要根据特定条件筛选数据？pandas 提供了用于切片、选择和提取所需数据的方法。

![../_images/03_subset_columns_rows.svg](https://pandas.pydata.org/docs/_images/03_subset_columns_rows.svg)

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset)

[用户指南](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)

pandas 利用 Matplotlib 的强大功能，开箱即用地提供数据绘图功能。只需选择与数据对应的图表类型（散点图、柱状图、箱线图等）即可。

![../_images/04_plot_overview.svg](https://pandas.pydata.org/docs/_images/04_plot_overview.svg)

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html#min-tut-04-plotting)

[用户指南](https://pandas.pydata.org/docs/user_guide/visualization.html#visualization)

无需遍历数据表的所有行来进行计算。在 pandas 中，列数据操作是逐元素进行的。 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 根据其他列中的现有数据添加新列非常简单。

![../_images/05_newcolumn_2.svg](https://pandas.pydata.org/docs/_images/05_newcolumn_2.svg)

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html#min-tut-05-columns)

[用户指南](https://pandas.pydata.org/docs/user_guide/dsintro.html#basics-dataframe-sel-add-del)

基本统计量（均值、中位数、最小值、最大值、计数等）可以轻松跨数据框计算。这些统计量，甚至自定义聚合，都可以应用于整个数据集、数据的滑动窗口，或按类别分组。后者也称为拆分-应用-合并方法。

![../_images/06_groupby.svg](https://pandas.pydata.org/docs/_images/06_groupby.svg)

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html#min-tut-06-stats)

[用户指南](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)

您可以通过多种方式更改数据表的结构。您可以 [`melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "熊猫融化") 将数据从宽格式转换为整齐的长格式。使用 [`pivot()`](https://pandas.pydata.org/docs/reference/api/pandas.pivot.html#pandas.pivot "pandas.pivot")

将长格式转换为宽格式。借助内置的聚合功能，只需一条命令即可创建透视表。

![../_images/07_melt.svg](https://pandas.pydata.org/docs/_images/07_melt.svg)

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html#min-tut-07-reshape)

[用户指南](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping)

使用 pandas 的数据库式连接和合并操作，可以按列或按行连接多个表。

![../_images/08_concat_row.svg](https://pandas.pydata.org/docs/_images/08_concat_row.svg)

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html#min-tut-08-combine)

[用户指南](https://pandas.pydata.org/docs/user_guide/merging.html#merging)

pandas 对时间序列有很强的支持，并且提供了一套丰富的工具来处理日期、时间和时间索引数据。

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html#min-tut-09-timeseries)

[用户指南](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries)

数据集通常包含的不仅仅是数值数据。pandas 提供了一系列函数来清理文本数据并从中提取有用信息。

[入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html#min-tut-10-text)

[用户指南](https://pandas.pydata.org/docs/user_guide/text.html#text)

## 来自……

您是否熟悉其他用于处理表格数据的软件？了解 pandas 中与您已了解的软件对应的操作：

![](https://pandas.pydata.org/docs/_images/logo_r.svg) ![](https://pandas.pydata.org/docs/_images/logo_sql.svg) ![](https://pandas.pydata.org/docs/_images/logo_stata.svg) ![](https://pandas.pydata.org/docs/_images/logo_excel.svg) ![](https://pandas.pydata.org/docs/_images/logo_sas.svg)

## 教程

如需快速了解 pandas 的功能，请参阅 [《10 分钟了解 pandas》](https://pandas.pydata.org/docs/user_guide/10min.html#min) 。

您还可以参考 pandas [速查表](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) ，获取使用 pandas 操作数据的简明指南。

社区制作了种类繁多的在线教程。部分资料已收录在“社区贡献 [教程”](https://pandas.pydata.org/docs/getting_started/tutorials.html#communitytutorials) 中。