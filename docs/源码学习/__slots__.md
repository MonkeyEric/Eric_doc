# __all__的使用
python模块中的__all__，用于模块导入限制，如：from module import *
此时被导入模块若定义了__all__属性，则只有__all__内指定的属性、方法、类可被导入；若没定义，则导入模块内的所有公有属性（不包含__开头的），方法和类

**bb.py**
```python
class A():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class B():
    def __init__(self,name,id):
        self.name=name
        self.id=id
def fun():
    print "func() is run!"
def fun1():
    print "func1() is run!"
```

**test_bb.py**
```python
from bb import *
a=A('zhansan','18')
print a.name,a.age
b=B("lisi",1001)
print b.name,b.id
fun()
fun1()

运行结果：
zhansan 18
lisi 1001
func() is run!
func1() is run!
```
> 由于bb.py中没有定义__all__属性，所以导入了bb.py中所有的公有属性（不包括__开头的私有属性）

**bb2.py**
```python
__all__=('A','func')
class A():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class B():
    def __init__(self,name,id):
        self.name=name
        self.id=id
def func():
    print "func() is run!"
def func1():
    print "func1() is run!"
```
**test_bb2.py**
```python
from bb import *
a=A('zhansan','18')
print a.name,a.age
func()
```
> 由于bb.py中使用了__all__=('A','func')，所以在别的模块导入该模块时，只能导入__all__中的变量、方法、类


# __slots__的使用
## 摘要
当一个类需要创建大量实例时，可以通过__slots__声明实例所需要的属性
例如：class Foo(obejct):__slots__= ['foo']。这样可以带来以下优点：
* 更快的属性访问速度
* 较少内存消耗

## slots的实现
我们首先来看看纯python是如何实现__slots__：
```python
# coding:utf-8
class Member(object):
    # 定义描述器实现slots属性的查找
    def __init__(self, i):
        self.i = i

    def __get__(self, obj, type=None):
        return obj._slotvalues[self.i]

    def __set__(self, obj, value):
        obj._values[self.i] = value


class Type(type):
    # 使用元类实现slots
    def __new__(self, name, bases, namespaces):
        slots = namespaces.get('_slots_')
        if slots:
            for i, slot in enumerate(slots):
                namespaces[slot] = Member(i)
            original_init = namespaces.get('__init__')

            def __init__(self, *args, **kwargs):
                # 创建_slotvalues列表和调用原来的__init__
                self._slotvalues = [None] * len(slots)
                if original_init(self, *args, **kwargs):
                    original_init(self, *args, **kwargs)

            namespaces['__init__'] = __init__
        return type.__new__(self, name, bases, namespaces)


try:
    class Object(object):
        __metaclass__ = Type
except:
    class Object(metaclass=Type):
        pass


class A(Object):
    _slots_ = 'x', 'y'


a = A()
a.x = 10
print(a.x)		
```
在Cpython中，当一个A类定义了_slots_ = {'x','y'},A.x就是一个有__get__和__set__方法的member_descriptor,并且在每个实例中可以通过直接访问内存获得。
在上面的例子中，我们用纯Python实现了一个等价的slots。当一个元类看到_slots_定义了x和y，它会创建两个的类变量，x = Member(0)和y=member(1)。然后，装饰__init__方法让新的实例创建一个_slotvalues列表。


例子中的实现和Cpython不同的是：
* 例子中，_slotvalues是一个存储在类对象外部的列表，而在Cpython中它与实例对象存储在一起，可以通过直接访问内存获得。相应地，member decriptor也不是存在外部列表中，而同样可以通过直接访问内存获得。
*　默认情况下，__new__方法会为每个实例创建一个字典__dict__来存储实例的属性。但如果定义了__slots__，__new__方法就不会再创建这个字典。
* 由于不存在__dict__来存储新的属性，所以使用一个不在__slots__中的属性时，程序会报错。

## 关于slots的继承问题
为了正确使用__slots__，最好直接继承object。如有需要用到其他父类，则父类和子类都要定义slots，还要记得子类的slots会覆盖父类的slots。
除非所有父类的slots都为空，否则不要使用多继承。

## namedtuple
利用内置的namedtuple不可变的特性，结合slots，能创建出一个轻量不可变的实例。(约等于一个元组的大小)
```python
>>> from collections import namedtuple
>>> class MyNt(namedtupele('MyNt', 'bar baz')): __slots__ = ()
>>> nt = MyNt('r', 'z')
>>> nt.bar
'r'
>>> nt.baz
'z'
```