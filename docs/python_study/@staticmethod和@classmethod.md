# python中的@staticmethod和@classmethod

在函数前面加上 @staticmethod

在函数前面加上 @classmethod

今天在别人的代码中看到了有在函数前面加上 @staticmethod 和 @classmethod 的情况，查阅相关资料，现把它的用法记录下来。
## 在函数前面加上 @staticmethod
```python

class C(object):
    @staticmethod # 声明一个静态方法, static:静态的
    def f(): # 里面没有self
        print("123")
C.f() #f()已经声明好了它是一个静态的方法,故无需将类实例化后在调用

co = C()
co.f() # 将类实例化后在调用,结果一样;
```
123
123

## 在函数前面加上 @classmethod
@classmethod修饰符对应的函数不需要实例化，不需要self参数，但是第一个参数需要是cls参数，可以来调用类的属性，类的方法，实例化对象。
```python

class A(object):
    bar = 1
    def func1(self):
        print("func1")
    @classmethod # 函数的修饰符
    def func2(cls): # 第一个参数不是self, 是cls
        print("func2")
        print(cls.bar)
        cls().func1()
        
A.func2() # 不需要实例化

func2
1
func1
1
2
3
```


