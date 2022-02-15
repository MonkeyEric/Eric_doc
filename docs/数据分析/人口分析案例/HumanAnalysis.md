# 基于pandas的人口分析案例
**题目需求**
* 导入文件，查看原始数据
* 将人口数据和各州简称数据进行合并
* 将合并的数据中重复的abbreviation列进行删除
* 查看存在缺失数据的列
* 找到有哪些state/region使得state的值为NaN，进行去重操作
* 为找到的这些state/region的state项上补上正确的值，从而去除掉state这一列的所有NaN
* 合并各州面积数据areas
* 我们会发现area(sq.mi)这一列有缺失数据，找出是那些行
* 去除含有缺失数据的行
* 找出2010年的全民人口数据
* 计算各州的人口密度
* 排序，并找出人口密度最高的州

```jupyterpython
import pandas as pd
import numpy as np
from pandas import DataFrame

# 导入文件，查看原始数据
abb = pd.read_csv('./state-abbrevs.csv') # state州的全程，abbreviation州的简称
pop = pd.read_csv('./state-population.csv')  # state/region 州的简称，age年龄层次，year年份，population 人口数量
area = pd.read_csv('./state-areas.csv') # state 州的简称， area(sq.mi)州的面积
pop.head()




# 将人口数据和各州简称数据进行合并
# how==outer ，可以保证数据的完整性
abb_pop = pd.merge(pop,abb,left_on='state/region',right_on='abbreviation',how='outer')
abb_pop.drop(labels='abbreviation',axis=1,inplace=True)
abb_pop.head()



# 查看缺失数据列
abb_pop.isnull().any(axis=0)
# 找到有哪些state/region使得state的值为NaN，进行去重操作 
# 第一步 找到state为空的index
abb_pop.loc[abb_pop['state'].isnull()]
# 第二步 将state对应的简称找到
abb_pop.loc[abb_pop['state'].isnull()]['state/region']
# 第三步 将找到的state/regioin 进行去重
abb_pop.loc[abb_pop['state'].isnull()]['state/region'].unique()


# 为找到的这些state/region的state项上补上正确的值，从而去除掉state这一列的所有NaN
# 1. 根据简称对应的全称空值找到
abb_pop.loc[abb_pop['state/region'] == 'PR']  # pr对应的行数据
# indexes 保存的行索引就是pr对应的行数据的索引
indexes = abb_pop.loc[abb_pop['state/region'] == 'PR'].index
# 2. 将找到的空值填充对应简称的全称即可
abb_pop.loc[indexes,'state']='pppprr'

indexes2 = abb_pop.loc[abb_pop['state/region'] == 'USA'].index 
abb_pop.loc[indexes2,'state'] = 'The United States'
abb_pop.loc[abb_pop['state/region'] == 'USA']


# 合并各州面积数据areas
abb_pop_area= pd.merge(abb_pop,area,on='state',how='outer')
indexes = abb_pop_area.loc[abb_pop_area['area (sq. mi)'].isnull()].index
# 去除含有缺失数据的行
abb_pop_area.drop(labels=indexes,axis=0,inplace=True)



# 找出2010年的全民人口数据  条件查询
abb_pop_area.query('ages=="total" & year==2010')

# 计算各州的人口密度=人口/面积
# 将人口密度数据添加到原来的
abb_pop_area['midu'] = abb_pop_area['population']/abb_pop_area['area (sq. mi)']

# 排序，并找出人口密度最高的州
abb_pop_area.sort_values(by='midu',axis=0,ascending=False).iloc[0]['state']
```