# A Tool for Discourse Analysis--面向会话分析的筛选与检索工具
> 软件作者：杨潇然

## 1. 设计目的:

* 本程序是为《大数据视角下基于多语体、多维度语料库的会话结构研究》项目中的会话分析实验所设计的筛选与检索工具
* 本程序使用`Corpus`中的语料数据作为数据来源

## 2. 开发环境:

* 系统环境：Windows 10
* 编程语言：Python 3.7
* 主要加载了numpy（数据处理模块）, re（正则模块）, csv（csv文件操作模块）和os（系统操作模块）等第三方库

## 3. 代码详解：
### 3.1 库载入：
```python
import re
import os
import csv
import numpy as np
```
### 3.2 字典设置：
```python
header=['<DPP>','<MPP>','<DRT>','<IDT>','<DLT>','<DKH>','<EDU>','<LAW>','<MED>','<SSP>','<DSP>','<SSX>','<DSX>','<TME>','<NME>','<TBW>','<PAS>','<ITR>','<HSP>','<ESP>','<LSP>','<MLE>','<FLE>','<MIM>','<MIF>','<FIM>','<FIF>']
num_sys=re.compile('<\d+>')
```
* 此处设置字典是为之后统计并输出标签个数所用
* 标签字典`header`共包含27个标签，涵盖了标签体系中的会话层和词语层

### 3.3 文件路径与目录载入：
```python
path = r".\美剧会话语料库" #设置文件夹路径
files= os.listdir(path) #得到文件夹下的所有文件名称
```
* 将本程序与语料库文件放置在同一文件夹下可使用相对路径，外置语料库则需要填写绝对路径
* 本程序会读取指定文件夹下的所有文件，并记录文件名作为区分

### 3.4 开放csv文件写入功能：
```python
with open("./输出数据.csv",'a',newline='',encoding='utf-8') as w:
    writer = csv.DictWriter(w,fieldnames=header)
    writer.writeheader()  # 写入列名
```
* 本程序产出的数据文件将以csv文件形式储存

### 3.5 读取语料数据：
```python
for file in files: #遍历文件夹
        position = path+'\\'+ file #构造绝对路径，"\\"，其中一个'\'为转义符         
        with open(position,'r',encoding='utf8') as f:
            cont = True
            li = []
```
* `cont`为语句迭代器，负责按行读取语料文件中的文本数据
* `li`为语句累加器，负责储存当前语块的所有文本数据

### 3.6 标签筛选：
```python
if cont =='\n':# 读取到空行时，则对此空行到上一空行之间的文本进行提取分析
                    match_tag = re.findall(r"\<ITR\>", str(li)) # 搜索包含ITR的对话块
                    if(len(match_tag)>= 1):
                        match_result={}
                        first_tag = re.findall(r"\<.*?\>", str(li)) # 如果对话块中ITR的个数大于1，则提取该块中所有包含在<>中的内容
                        for key in first_tag:
                            if re.match(num_sys,key) == None:
                                match_result[key] = match_result.get(key, 0) + 1
                        writer.writerow(match_result)
                    li = []
```
* 本语料库的语块划分逻辑是`遇到一次空行 -> li停止累加数据 -> 提取li中的数据为待分析语料数据`
* `match_tag`变量负责记录预设的正则表达式，并此预设作为筛选条件
* `first_tag`变量负责提取所有符合筛选条件的标签
* `key`变量负责读取header中的索引作为统计标签出现次数的条件
* 对经过处理过后的`li`变量进行初始化，送入下一个循坏继续累加语料

## 4. 附加功能：

```python
w.write(position+'\n')
w.write(str(li)+'\n')
```
* 通过以上指令修改文件写入的规则，还可以输出符合条件的语料作为进一步研究与整理数据提供便利
  
## 5. 输出数据示例：

* 输出文件如下：
    result_dataline.txt：txt格式文件，含有文件信息、tag出现次数
    result_text.txt：txt格式文件，含有文件信息、对应语段文本
    result_data.csv：csv格式文件，含有结构化后的tag出现次数，用于数据分析

![image](https://github.com/Golden-Arc/Discourse_Analysis_Tool/blob/main/Image/sample1.PNG)

> 上图所示数据是研究打断现象所需的语料进行筛选、统计后的结构化数据
> 筛选条件为**所有包含`<ITR>`标签的语块**

![image](https://github.com/Golden-Arc/Discourse_Analysis_Tool/blob/main/Image/sample2.PNG)
> 上图所示数据是所有包含`<ITR>`标签的语料数据，每一行代表一个语块

## 6. 后续改进：

* 此程序为该工具的1.0版本，之后将继续迭代，增强交互性与自动化程度
* 在之后的版本中本项目组计划搭建线上标注平台，其中此模块将作为主要的筛选模块继续进行维护

> 本项目中所有文件均遵循*MIT开源协议*。转载请注明出处。
> 