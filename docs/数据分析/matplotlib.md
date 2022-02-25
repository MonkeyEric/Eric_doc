# plt.plot()绘制线性图
* 绘制单条线形图
* 绘制多条线形图
* 设置坐标系比例plt.figure(fgsize=(a,b))
* 设置图标Legend（）
* 设置轴的标识
* 图例保存
    * fig=plt.figure()
    * plt.plot(x,y)
    * figure.savefig()
* 曲线的样式和风格（自学）
```python
import matplotlib.pyplot as plt 
import numpy as np
# jupyter的魔法指令
# 如果绘制的图像不显示，则执行该操作
# %matplotlib inline  
x = np.linspace(-np.pi,np.pi,num=10)
y = x*2+3.1
x = x
y = x**2
plt.plot(x,y)
# 绘制多条支线
x = x
y =  1- x**2
x1 = x-1
y1 = y**2

# 设置坐标系的比例plt.figure(figsize=(a.b)) 等比例放大
# 将坐标系等比例放大或者缩小，刻度是不会改变
plt.figure(figsize=(5,10))
plt.plot(x,y,x1,y1)
# 设置图例 legend()
plt.plot(x,y,label='temp')
plt.plot(x+1,y+1,label='dist')
plt.xlabel('aaa')
plt.ylabel('city_dist')
plt.title('this is a title')
plt.legend()
# 图例保存
# 1. 实例化fig对象
# 2. 绘图
# 3. 保存
fig = plt.figure()
plt.plot(x,y)
fig.savefig('./1.png')
# 绘图风格，例如颜色、字体、线段样式
plt.plot(x,y,c='red',alpha=0.3,ls='dashed',marker='8')

```

# 柱状图：plt.bar()
* 参数：第一个参数式索引，第二个参数式数据值。第三个参数式条形的宽度
```python
# * 参数：第一个参数式索引，第二个参数式数据值。第三个参数式条形的宽度
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.bar(x,y)
```
# 饼图
* pie(),饼图也只有一个参数x
* 饼图适合展示各部分占总体的比例，条形图适合比较各部分的大小
```python
arr = [11,22,31,14]
plt.pie(arr,labels=['a','b','c','d'],labeldistance=0.3,autopct='%.6f%%',explode=[0.1,0.1,0.1,0.1])
```

# 直方图
* 是一个特殊的柱状图，又叫做密度图
* plt.hist()的参数
  * bins.可以是一个bin数量的整数值，也可以是表示bin的一个序列。默认值为10
  * normed：如果值为True，直方图的值将进行归一化处理，形成概率密度，默认值为False
  * color：指定直方图的颜色。可以是单一颜色值或颜色的序列。如果指定了多个数据集合，例如DataFrame对象，颜色序列将会设置为相同的顺序。如果未指定，将会使用一个默认的线条颜色
  * orientation：通过设置orientation为horizontal创建水平直方图。默认值为vertical

```python
x = [1,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,6,6,7,7,8,8,8,9]

plt.hist(x,bins=20) # 谁最高，密度最高
# 参数1：依次表示的是柱子的高度
# 参数2： 1到1.4的范围，又多少个，就多高
```
# 散点图 scatter()
* 因变量随字变量而变化的大致趋势
```python
x = np.random.randint(0,10,size=(20,))
y = np.random.randint(0,10,size=(20,))
y=x**2
plt.scatter(x,y)
```
> [seaborn](http://seaborn.pydata.org/) 可以让困难的东西更加简单,可以画出箱型图，多变量做图
