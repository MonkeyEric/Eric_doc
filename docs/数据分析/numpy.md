
# 0.环境准备
* [python3安装步骤](https://www.cnblogs.com/temari/p/13044416.html)
* [anaconda安装步骤](https://www.likecs.com/default/index/show?id=72014)
* [jupyter的安装步骤](https://www.cnblogs.com/Zzbj/p/10384122.html)
* [jupyter快捷键](https://www.cnblogs.com/clschao/articles/10906415.html)


# 1.数据分析
## 1.1 什么是数据分析？
是把隐藏在一些看似杂乱无章的数据背后的信息提炼出来，总结出所研究对象的内在规律。
* 使得数据的价值最大化
  * 分析用户的消费行为
    
        1. 制定促销的活动的方案
        2. 指定促销时间和粒度
        3. 计算用户的活跃度
        4. 分析产品的回购力度
  
  * 分析广告点击率
    
        1. 决定投放时间
        2. 指定广告定向人群方案
        3. 决定相关平台的投放
  

* 数据分析是用适当的方法对收集来的大量数据进行分析，帮助人们做出判断，以便采取适当的行动
  * 保险公司从大量赔付申请数据中判断哪些行为为骗保的可能
  * 支付宝通过从大量的用户消费记录和行为自动调整花呗的额度
  * 短视频平台通过用户的点击和观看行为数据针对性的给用户推送喜欢的视频
 
 
## 1.2 为什么学习数据分析？
* 有岗位的需求
  * 数据竞赛平台
* 是Python数据科学的基础
* 是机器学习课程的基础

## 1.3 数据分析实现流程
* 提出问题
* 准备数据
* 分析数据
* 获得结论
* 成果可视化

## 1.4 数据分析三大工具
* numpy,主要处理数值型数据
* pandas，主要处理非数值型数据
* matplotlib, 用来画图


# 2. numpy
## 2.1 numpy模块
Numpy(Numerical Python)是Python语言中做科学计算的基础库。重在于数值计算，也是大部分Python科学计算库的基础，多用于在大型、多维数组上执行的数据运算

**注意**
> 一维数组、二维数组、三维数组…… 你可以将一维数组理解为每页数的一行字，那么每页就是二维数组，一本书就是三维数组……。【这里的*维数组，是基于书本中的每行字来做参照物】

> 以下环境是在jupyter中进行的操作
## 2.2 numpy的创建
### 2.2.1 使用np.array()创建
#### 1. 创建数组 
array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
> * object：必选参数，数组或嵌套的数列
> * dtype：数据类型,int32 int64,float等等
> * copy：对象是否需要复制，可选
> * order：创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
> * subok：默认返回一个与基类类型一致的数组
> * ndmin：秩，即轴的数量或维度的数量，指定结果数组应具有的最小维数
> * like
> * 返回:ndarray

使用array()创建一个一维数组
```python
import numpy as np
# 创建一个一维数组
np.array([1,2,3,3,4,5])
```  
使用array()创建一个多维数组
 ```python
np.array([[1,2,3,4,5],[6,7,8,9,10]])
``` 

**列表和数组的区别是什么？**
* 数组中存储的数据元素类型必须是统一类型
* 优先级： 字符串>浮点型>整数
```python
>>>np.array([1,'2',2.31])
array(['1', '2', '2.31'], dtype='<U32')
```
#### 2. ones、zero、eye的用法   *使用np的routines函数创建*
shape表示数组的形状
```python
import numpy as np
np.ones(shape=[2,3]) # 构建2行3列的，元素都是1.
np.zeros(shape=[2,3]) # 构建2行3列的，元素都是0.
# numpy.eye（N，M =无，k = 0，dtype = <class’flove’>，order =‘C’ ） N表示行数，M表示列数，k对角线的索引，0指的是主对角线，负值指的是下对角线
np.eye(3) # 返回一个3行3列，对角线为1
```
#### 3.linespace
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
在start和stop之间产生num个线性向量，每个向量之间的距离是相同的
* start：样本数据开始点
* stop：样本数据结束点
* num：生成的样本数量，默认为50
* endpoint：默认为True，包含stop,若为False则不包含stop
* restep：默认为False。若为True，则结果会给出数据间隔，array([])变成了(array([]),step)，其中sample的数据类型是numpy.ndarray，step的数据类型是float
* axis：默认为0。可以选择-1
* dtype：
* 返回：一个一维等差数组
```python
import numpy as np
np.linspace(0,100,num=20)
# 输出结果
array([  0.        ,   5.26315789,  10.52631579,  15.78947368,
        21.05263158,  26.31578947,  31.57894737,  36.84210526,
        42.10526316,  47.36842105,  52.63157895,  57.89473684,
        63.15789474,  68.42105263,  73.68421053,  78.94736842,
        84.21052632,  89.47368421,  94.73684211, 100.        ])
```
#### 4. arange()
arange([start,] stop[, step,], dtype=None, *, like=None)
* start：
* stop：
* step：相差多少
* 返回一个一维的等差数组
```python
import numpy as np
np.arange(1,10,step=3)
# array([1, 4, 7])
```
#### 5. random.randint()
randint(low, high=None, size=None, dtype=int)
```python
import numpy as np
np.random.randint(1,30,size=2)
# array([19,  6])
np.random.randint(1,30,size=(2,4))
# array([[26, 15, 25, 10],[25,  7, 20,  1]])
```
#### 6. numpy的常用属性
* shape：返回数组的形状。 arr.shape
* ndim: 返回数组的维度。 arr.ndim
* size：返回数组的元素个数。 arr.size
* dtype：返回数组的元素类型。 arr.dtype
* type：返回数组的类型。 type(arr)


#### 7. numpy的大数据类型
* array(dtype=?) ：可以设定数据类型，在旧数组操作
* arr.dtype-?：可以修改数据类型，在旧数组操作
* arr.astype(？)：返回新的数组



#### 8. 索引操作和列表同理
```python
import numpy as np
arr = np.random.randint(0,100,size=(5,6))
arr[0][1]
```
#### 9. 切片操作
```python
import numpy as np
arr = np.random.randint(0,100,size=(5,6))
# 切除前两列数据 arr[行切片，列切片]
print(arr[,0:2])  
# 切除前两行的数据
print(arr[0:2])
# 切除前两行的前两列的数据
print(arr[0:2,0:2])
# 数组数据反转
print(arr[::-1]) # 行倒置
print(arr[:,::-1]) # 列倒置
print(arr[::-1,::-1]) # 所有倒置
# 练习：将一张图片上下左右进行翻转操作
# 练习：将图片进行指定区域裁剪


```
#### 10. 变形
```python
import numpy as np
arr = np.random.randint(0,100,size=(3,4))
# 将二维变成一维
arr.reshape((12,))
# 将一维变成二维
arr.reshape((2,-1)) #-1 自动计算

```
#### 11. 级联操作
将多个numpy数组进行横向或者纵向的拼接
* axis轴向的理解
  * 0:列
  * 1：行
* 问题：
  * 级联的两个数组维度一样，但是行列个数不一样回如何？

级联的两个数组维度一样，但是行列个数不一致回如何？
行数不一致只可以进行纵向级联，否则进行横向级联
```python
import numpy as np
arr = np.random.randint(0,100,size=(3,4))
np.concatenate((arr,arr),axis=0)
```
实现一个图片的九宫格
```python
import numpy as np
import matplotlib.pyplot as plt
img_arr = plt.imread('./lufei.jpeg') # 将图片数据读取到数组中
img_3 = np.concatenate((img_arr,img_arr,img_arr),axis=1)
img_9 = np.concatenate((img_3,img_3,img_3),axis=0)
print(plt.imshow(img_9)) 
```

#### 12. 常见的聚合操作
```python
# sum,max,min,mean. mean是平均值的意思
import numpy as np
arr = np.random.randint(1,30,size=(2,4))
print(arr.sum(axis=0)) # 列的总和
print(arr.sum(axis=1)) # 行的总和
print(arr.sum()) # 元素总和
```

#### 13. 常用的数学函数
* numpy提供了标准的三角函数：sin(),cos(),tan()
* numpy.around(a,decimals)函数返回指定数字的四舍五入值
  * 参数说明：
    * a：数组
    * decimals：舍入的小数位数。默认值为0。如果为负，整数将四舍五入到小数点左侧的位置
```python
import numpy as np
arr = np.random.randint(1,30,size=(2,4))
np.sin(arr) # 对每个元素进行计算sin,返回数组

print(np.around(arr))
```
#### 14. 常用统计函数
* numpy.amin()和numpy.amax()，用英语计算数组中的元素沿指定轴的最小、最大值
* numpy.ptp()：计算数组中元素最大值与最小值的差（最大值-最小值）
* numpy.median()函数用于计算数组a中元素的中位数（中值）
* 标准差std():标准差是一组数据平均值分散程度的一种度量。
  * 公式：std = sqrt(mean((x-x.mean())**2))
  * 如果数组是[1,2,3,4]，则其平均值为2.5。因此，差的平方是[2.25,0.25,0.25,2.25]，并且其平均值的平方根除以4，即sqrt(5/4)，结果为：1.11180339887498949
* 方差var()：统计中的防擦好（样本方差）是每个样本值与全体样本值的平均数只差的平方值的平均数，即mean((x-x.mean())**2)。换句话说，标准差是方差的平方根
```python
import numpy as np
a  = np.array([3,8,5,7,6])
print(a.std())
print(a.var())
```


#### 15. 矩阵相关
```python
# 转置矩阵
import numpy as np
arr = np.random.randint(1,30,size=(2,4))
print(arr.T)  # 将行变成列，列变成行
# 矩阵相乘
# numpy.dot(a,b,out=None) a：一个数组，b：一个数组
```

### 2.2.2 使用plt创建
将外部的一张图片读取加载到numpy数组中，然后尝试改变数组元素的数值，查看对原始图片的影响。
```python
import matplotlib.pyplot as plt
img_arr = plt.imread('./lufei.jpeg') # 将图片数据读取到数组中
print(img_arr) # 三维数组，分别是 长、宽、颜色
# 通过数组，将图片显示出来
plt.imshow(img_arr) 
# 修改图片的原始数据，将每一个数组元素减去100 
plt.imshow(img_arr-100)

```
> python文件环境中，如何显示图片？
```python 
# coding:utf-8
import matplotlib.pyplot as plt
import pylab
img_arr = plt.imread('./lufei.jpeg') # 将图片数据读取到数组中
print(img_arr) # 三维数组，分别是 长、宽、颜色
# 通过数组，将图片显示出来
plt.imshow(img_arr)
pylab.show()
```






