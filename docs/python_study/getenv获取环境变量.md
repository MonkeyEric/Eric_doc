# os中getenv如何获取变量？
变量在函数中经常会提到，而且也是通过函数才对变量进行更改的。那么python3

os中有没有变量需要通过函数去改变呢？小编翻了一些网页后，还真的就找到了。这个是python3 

os中其他的接口模块的内容，可能小伙伴们学习的时候没有留意过，接下来我们就一起看看怎么改变环境变量吧。
```python
getenv(key, default=None)
```
获取环境变量。
```python
os.getenv("PATH")
'/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'

get_exec_path(env=None)
```

**返回用于搜索可执行文件的目录列表。看以看作是 PATH 环境变量的列表形式。**

```python
os.get_exec_path()
['/usr/local/bin',
 '/usr/bin',
 '/bin',
 '/usr/sbin',
 '/sbin']
 ```

拓展： system(command)
在当前进程中，启动子进程，执行命令 command（字符串），主进程会阻塞，直到子进程执行完成。这是通过调用标准C函数 system() 来实现的，并且具有相同的限制。
```python
if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"
 
os.system(command)
```




