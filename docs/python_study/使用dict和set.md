# 使用dict和set

## dict
* 使用key-value存储，具有极快的查找速度。
* 避免查询key不存在出现的错误，有两种方法
* 通过in判断key是否存在：
```python
>>>'Thmoas' in d
False
```
通过dict提供的get（）方法，如果key不存在，可以返回None，或者自己指定的Value。
```python
>>>d.get('Thomas')
>>>d.get('Thomas',-1)
```
删除一个key，key是不可变对象
```python
d.pop('Bob') #对应的value也会被删除掉
```
在python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key。
和list比较，dict有以下几个特点：
* 查找和插入的速度极快，不会随着key的增加而变慢
* 需要占用大量的内存，内存浪费多
而list相反
* 查找和插入的时间随着元素的增加而增加；
* 占用空间小，浪费内存很少。

## set的功能
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
重复元素在set中自动被过滤：
```python
>>>s=set([1,2,3,1,2,3,3])
>>>s
{1,2,3}
```
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
```python
s.add(4)
```
通过remove（key）方法可以删除元素：
```python
>>>s.remove(4)
>>>s
{1,2,3}
```
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
```python
>>>s1= set([1,2,3])
>>>s2=set([2,3,4])
>>>s1&s2
{2,3}
>>>s1 | s2
{1,2,3,4}
```
## 究竟什么叫做无序，什么叫做有序？
1. 列表list有序可变
2. 字典dict在python3.6之前是无序的，到了python3.7变成了有序，可变
3. 元组tuple不可变
4. 集合set无序可变(还有个不可变集合frozenset)
5. 数字number不可变
6. 字符串string不可变

**python 3.7之后的字典是有序的。**
**python3.7之前的字典结构，经典粗暴的hash表实现方式，这样的话每次hash表的扩容和缩容都可能导致hash值的改变。**

hash表容量更新的前后，它的键之间的相对顺序是会变化的，因此字典的元素是无序的。

新结构由 Indices(索引，数组实现) 和 Entries(实体，PyDictObject类型) 两种结构组成。

当插入一个数据时，先计算数据对应的hash值并映射成 Indices 数组的一个下标，没有冲突的话就将另一个值 Entries_index(暂时这么叫吧) 填入Indices数组中下标对应的位置。并在Entries后面追加一行记录，类似 hash值, key值, value值 。


set和dict的唯一区别仅在于没有存储对应的value。不可变对象
对于可变对象，比如list，对list进行操作哦，list内部的内容是回发生变化的，比如：
```python
>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
```
而对于不可变对象，比如str，对str进行操作：
```python
>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'
```
虽然字符串有个replace的方法，也确实变出了’Abc’，但变量最后仍是’abc’

## 可变的数据类型：
* list和dict
* 不可变的数据类型
* 整型int、浮点型float、字符串型string和元组tuple


