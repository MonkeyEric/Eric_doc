# pandas
> 前言
numpy能够帮助我们处理的是数值型数据，当然在数据分析中除了数值型的数据，还有好多其他类型的数据（字符串、时间序列），

# 什么是pandas？
首先来认识pandas中的两个常用的类：
* Series
* DataFrame
## 1. Series
Series(
    data=None,
    index=None,
    dtype: 'Dtype | None' = None,
    name=None,
    copy: 'bool' = False,
    fastpath: 'bool' = False,
)
* Series是一种类似与一维数组的对象，由下面两个部分组成：
    * values：一组数据（ndarray数据类型）
    * index：相关的数据索引标签 
* Series的创建
    * 由列表或numpy数组创建
    * 由字典创建
```python
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
s1 = Series(data=[1,2,3])
# 索引是0 1 2 的默认形式：隐式索引
s2 = Series(data=[1,2,3],index=('a','b','c'))
# a b c的索引，叫做显示索引，不会覆盖原有的隐士索引
# 显示索引可以增加数据的可读性
print(s1)
# 一个二维的数据源作为Series的数据源，查看是否可行——结果:不可行,必须是一维数组
# s = Series(data=np.random.randint(0,100,size=(3,4)))
# 将字典作为Series的数据源
dic = {
    "语文":100,
    "数学":120,
    "英语":120,
}
s = Series(data=dic) # 字典的key作为Series的显示索引 
# 索引
print(s[0])
print(s['语文'])
print(s.语文) # s.显示索引
print(s[['语文','数学']]) # 取多值


# 切片
print(s[0:2])
print(s['语文':'英语'])
```
### 1.1 Series常用属性
* shape
* size
* index
* value
```python
from pandas import Series,DataFrame
s1 = Series(data=[1,2,3])
print(s1.shape)
print(s1.size)
print(s1.value)
```


### 1.2 Series常用方法
* head(),tail()
* unique()
* isnull(),notnull()
* add() sub() mul() div()
```python
from pandas import Series,DataFrame
s1 = Series(data=[1,2,3,3,3,4,5,6,78,89,9,9,10])
print(s1.head(3))  # 查看前n个元素
print(s1.tail(3))  #　查看后ｎ个元素
print(s1.unique())  # 去重
print(s1.nunique())  # 返回去重后的元素个数
print(s1.isnull())  # 判断元素是否为空
print(s1.notnull()) # 判断元素是否为非空
```

### 1.3 Series的算数运算
* 法则：索引一致的元素进行算数运算否则补空
```python
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
s1 = Series(data=[1,2,3],index=['a','b','c'])
s2 = Series(data=[1,2,3],index=['a','d','c'])
print(s1+s2)
```


## 2.DataFrame(重点) 
* DataFrame是一个【表格型】的数据结构，DataFrame由按一定的顺序的多列数据组成，设计初衷是将Series的使用场景从一维拓展到多维。DataFrame既有行索引，也有列索引。
    * 行索引：index
    * 列索引：columns
    * 值：values
    
* DataFrame的创建
    * ndarray创建
    * 字典创建
    
```python
from pandas import Series,DataFrame
import numpy as np
DataFrame(data=[[1,2,3],[4,5,6]],index=['a','b'],columns=['A','B','C'])

df = DataFrame(data=np.random.randint(0,100,size=(6,8)))
print(df)
dic = {
    "漳卅":[110,110,110],
    "加急":[0,0,0]
}
df = DataFrame(data=dic,index=['语文','数学','英语'])
print(df)
```
### 2.1 DataFrame的属性
* values
* columns
* index
* shape
```python
from pandas import Series,DataFrame
import numpy as np
df = DataFrame(data=np.random.randint(0,100,size=(6,8)))
print(df.values)
print(df.columns)
print(df.index)
print(df.shape)
```

### 2.2 DataFrame的索引操作
* DataFrame的索引操作
    * 对行进行索引
    * 对列进行索引
    * 对元素进行索引
* iloc: 通过隐式索引取行
* loc：通过显示索引取行
```python
from pandas import Series,DataFrame
import numpy as np
DataFrame(data=[[1,2,3],[4,5,6]],index=['a','b'],columns=['A','B','C'])

df = DataFrame(data=np.random.randint(0,100,size=(5,4)),index=['a','b','c','d','e'],columns=['A','B','C','D'])
print(df)
# 索引去列，如果索引取列的时候，df有显示列索引，则下属方式的索引去列只可以使用显示索引
print(df['A'])
print(df[['A','B']])
# 索引去行
print(df.loc['a'])  # loc的作用是显式索引
print(df.iloc[0]) # iloc的作用是隐式索引 
print(df.loc[['a','d']])
print(df.iloc[[0,1]])

# 索引取元素
print(df.loc['b','A'])
print(df)
print(df.iloc[1,1])
```

### 2.3 DataFrame的切片操作
* 对行进行切片
* 对列进行切片
```python
from pandas import Series,DataFrame
import numpy as np
DataFrame(data=[[1,2,3],[4,5,6]],index=['a','b'],columns=['A','B','C'])

df = DataFrame(data=np.random.randint(0,100,size=(5,4)),index=['a','b','c','d','e'],columns=['A','B','C','D'])
print(df)
print(df.iloc[:,0:2])
print(df.loc[:,'A':'B'])
```

## 3. DataFrame的基础操作巩固-股票分析
### 3.1 需求：股票分析
* 使用tushare包获取某股票的历史行情数据
* 输出该股票所有收盘比开盘上涨3%以上的日期
* 输出该股票所有开盘比前日收盘跌幅超过20%的日期
* 假如我从2010年1月1日开始，每月第一个交易日买1手股票，每年最后一个交易日卖出所有股票，到今天为止，我的收益如何？
```shell
pip install tushare
```
> tushare：财经数据包，可以批量获取相关金融产品的历史数据

### 3.2 需求：双均线策略指定
* 使用tushare包获取股票的历史行情数据
```python
import tushare as ts
import pandas as pd
# ts.set_token('b233a50ee4b9f49801e659275b25a5a10d5ec8b9444efa78d79b1669')
# data = ts.get_k_data(code="600519",start='1900-01-01')
# data
# 对股票的数据进行基本操作
# 1. 将股票持久化存储  to_xxx()
# data.to_csv('./maotai.csv')
# 2. 将存储到本地的数据加载读取到df中
df = pd.read_csv('./maotai.csv')
# 3. 删除df中指定的列数据 axis 0表示行，1表示列 
df.drop(labels="Unnamed: 0",axis=1,inplace=True)
# 4. 查看df每一列的数据类型
# df['date'].dtype
# df.info()

# 5. 将date列的数据类型由字符串转换成时间序列
pd.to_datetime(df['date'])

# 6. 将date列作为源数据的行索引
df.set_index(df['date'],inplace=True)
```
> inplace的作用：
```
pandas中inplace参数在很多函数中都会有，它的作用是：是否在原对象基础上进行修改
* inplace = True：不创建新的对象，直接对原始对象进行修改；
* inplace = False：对数据进行修改，创建并返回新的对象承载其修结果。

其默认的数值是False，即创建新的对象进行修改，原对象不变，和深复制和浅复制有些类似。
```

#### 3.2.1 计算该股票历史数据的5日均线和30日均线
* 什么是均线？
    * 对于每一个交易日，都可以计算出前N天的平均值，然后把这些移动平均值连起来，成为一条线，就叫做N日移动平均线，移动平均线常有5天、10天、30天、60天、120和240天的指标。
    * 5天和10天的短线操作的参照目标，称作日均线指标
    * 30天和60天的是中期均线指标，称作季均线指标
    * 120天和240天的长期均线指标，称作年均线指标。
* 均线计算方法：MA=（C1+C2+C3+……+Cn）/n c:某日收盘价 N：移动平均周期天数
```python
df['close'].rolling(5)  # 以此将n个前5天的收盘价取出
# ma5 5日均值
ma5 = df['close'].rolling(5).mean()
# ma30 30日均值
ma30 = df['close'].rolling(30).mean()
print(ma30)
```
绘制双均线
```python
# 绘制双均线，双均线就是一条短期线和一条长期线
import matplotlib.pyplot as plt
plt.plot(ma5,label='ma5',c='red')
plt.plot(ma30,label='ma30',c='green')
plt.legend()
```
#### 3.2.2 分析输出所有金叉日期和死叉日期
* 股票分析技术中的金叉和死叉，可以简单解释为：
    * 分析指标中的两根线，一根为短时间内的指标线，另一根为较长时间的指标线
    * 如果短时间的指标线方向拐头向上，并且穿过了较长时间的指标线，这种状态叫：“金叉”
    * 如果短时间的指标线方向拐头向下，并且穿过了较长时间的指标线，这种状态叫：“死叉”
    * 一般情况下，出现金叉后，操作取向买入；死叉趋向卖出。当然，金叉和死叉只是分析指标之一，要和其他很多指标配合使用，才能增加操作的准确性
    

> 案例：如果我从2010年1月1日开始，初始资金为100000元，金叉尽量买入，死叉全部卖出，则到今天为止，我的炒股收益是如何？
> 
> 分析：
> * 买卖股票的单价使用开盘价
> * 买卖股票的时机
> * 最终手里会有剩余的股票没有卖出去
>   * 会有。如果最后一天为金叉，则买入股票。估量剩余股票的价值计算到总收益。
>   * 剩余股票的单价就是最后一天的收盘价

```python
# 切片是为了删除NaN的数据
ma5_ = ma5[29:]
ma30_ = ma30[29:]
df_ = df[29:]
s1 = ma5_ <ma30_
s2 = ma5_>=ma30_

# 死叉日期
dead_date = df_.loc[s1&s2.shift(1)].index

# 金叉日期
golden_date= df_.loc[~(s1|(s2.shift(1)))].index
from pandas import Series
# 创建一个series，sr1存储的Value值全部为1，索引为金叉日期
sr1 = Series(data=1,index=golden_date)
# sr2存储的value值全部为0，索引为死叉日期
sr2 = Series(data=0,index=dead_date)
# 将sr1和sr2这两个series整合到一起
s = sr1.append(sr2)
# 对s中的索引进行排序（时间）
s.sort_index(inplace=True)
s # 1表示金叉时间，0表示死叉时间
# 2010-2020年之间的金叉和死叉的时间
new_s = s['2010':'2022']
first_money = 100000 # 本金不可变
money = first_money  # 可变钱数，买卖股票从money中进行加减操作
# new_s中有多少个值为1则表示有多少个金叉，表示买入多少次股票
hold = 0 # 持有股票
for i in range(len(new_s)):
    # 单价,new_s.indexes[i]第一天所对应的事件,使用开盘价
    price =  df.loc[new_s.index[i]]['open']
    if new_s[i] == 1: # 金叉 买股票
        hold_moeny = price
        # 单价*100 就是手数需要多少钱，
        hand = money// (price*100)
        hold = hand *100 # 股票的古树
        money -= hold*price # 买股票花的钱从money中减去
        
    else: # 卖股票
        money+=(price*hold)
        hold = 0
# 股票最后手中是否有剩余
last_money = hold* df['open'][-1]
print('总收益',last_money+money-first_money)
```

### 3.3 工具：[聚宽的使用](https://www.joinquant.com/)


## 4. pandas的高级操作-替换操作
* 替换操作可以同于作用于Series和DataFrame中
* 单值替换
    * 普通替换：替换所有符合要求的元素:to_replace=15,value='e'
    * 按列指定单值替换：to_replace={列标签:替换值} value='value'
* 多值替换
    * 列表替换：to_replace=[],value=[]
    * 字典替换（推荐）： to_replace={to_replace:value,to_replace:value}
    
```jupyterpython
import pandas as pd
import numpy as np
from pandas import DataFrame
df = DataFrame(data=np.random.randint(0,100,size=(5,6)))
# 将8 替换成eight
df.replace(to_replace=2,value='two')
# 多值替换
df.replace(to_replace={2:'two',30:'thirty'})
# 指定列的替换
df.replace(to_replace={2:31},value='333111')

```
 
## 5. pandas的高级操作-映射操作
* 概念：创建一个映射关系列表，把values元素和一个特定的标签或者字符串绑定（给一个元素提供不同的表现形式）
* 创建一个df,两列分别是姓名和薪资，然后给其名字其对应的英文名
```jupyterpython
import pandas as pd
import numpy as np
from pandas import DataFrame
dic = {
    'name':['张三','李四','王五'],
    'salary':[15000,20000,15000]
}
df = DataFrame(data=dic)
# map是Series的方法，DataFrame用不了
df['name']
didc1 = {
    '张三':'Tom',
    '李四':'Jerry',
    '王五':'Alan'
}
df['e_name'] = df['name'].map(didc1)

# map还可以当作映射工具，
# 超过3000部分的钱缴纳50%的税，计算每个人的税后薪资
def after_sal(s):
    return s-(s-3000)*0.5
df['after_sal'] = df['salary'].map(after_sal)



# DataFrame中的apply的操作，对df的列或者行进行操作
df = DataFrame(data=np.random.randint(1,11,size=(5,3)))
def my_add(value):
    return value+10
df.apply(my_add,axis=1)



df.applymap(my_add) # 是针对df中的每个元素来进行操作，算法成本比较高，
```