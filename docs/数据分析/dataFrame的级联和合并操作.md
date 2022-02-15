# 级联操作
* pd.concat,pd.append

pandas使用pd.concat函数，与np.concatenate函数类似，只是多了一些参数：
* objs
* axis=0
* keys
* join='outer'/'inner':表示的是级联的方式，outer会将所有的项进行级联（忽略匹配和不匹配），而inner只会将匹配的项级联到一起，不配的不级联
* ignore_index=False

## 1. 匹配级联
```python
import pandas as pd
import numpy as np
from pandas import DataFrame
df1 = DataFrame(data=np.random.randint(0,100,size=(5,3)),columns=['A','B','C'])
df2 = DataFrame(data=np.random.randint(0,100,size=(5,3)),columns=['A','D','C'])
print(pd.concat((df1,df1),axis=1))
```

## 2. 不匹配级联
* 不匹配指的是级联的维度的索引不一致，例如纵向级联时列索引不一致，横向级联时行索引不一致
* 有2中链接方式：
    * 外连接 how=outer：补NaN（默认模式）
    * 内链接 how=inner：指链接匹配的项
```python
print(pd.concat((df1,df2),axis=0,join='inner'))
```
> 如果想要保留数据的完整性必须使用outer(外连接)

## 3. append函数的使用
只可以列跟列级联
```python
df1.append(df1)
df1.append(df2)
```

# 合并操作
* merge与concat的区别在于，merge需要依据某一共同列来进行合并
* 使用pd.merge()合并时，会自动根据两者相同column名称的那一列，作为key来进行合并。
* 注意每一列元素的顺序不要求一致
## 1. 一对一合并 
```python
import pandas as pd
import numpy as np
from pandas import DataFrame

# 一对一合并
df1 = DataFrame({'employee':['Bob','Jake','Lisa'],'group':['Accounting','Engineering','Engineering'],})
df2 = DataFrame({'employee':['Lisa','Bob','Jake'],'hire_date':[2004,2008,2012],})
# pd.merge(df1,df2,on='employee')
df1
```

## 2. 一对多合并
```python
#  一对多合并
df3 = DataFrame({'employee':['Lisa','Jake'],'group':['Accounting','Engineering'],'hire_date':[2014,2016]})
df4 = DataFrame({'group':['HR','Engineering','Engineering'],'supervisor':['Carly','Guido','Steve']})
pd.merge(df3,df4) # on不写，默认的合并条件就是两张表中公有的列索引。 how 默认是inner
pd.merge(df1,df4,how='outer')
```

>key的规范化，即有多个列名称相同时，需要使用On来指定那一列作为key,配合suffixes指定冲突列名

```python
pd.merge(df1,df3)  # 默认会根据employee和group来当作key进行合并
pd.merge(df1,df3,on='group') # on指定列来进行合并

```
> 当两张表没有可进行链接的列时，可以使用Left_on和right_on手动指定Merge中左右两边的那一列作为连接的列。
```python

df5= DataFrame({'name':['Lisa','Bobs','Bill'],'hire_dates':[1998,2016,2007]})
pd.merge(df1,df5,left_on='employee',right_on='name') 
```
> 什么时候用级联，什么时候用合并？

如果大部分的列的索引都一样，就用级联，如果不一样，就用合并