## logging模块简介
logging模块是python内置的标准模块，主要用于输出运行日志，可以设置输出日志的你等级、日志保存路径、日志文件回滚等；相比print，具备以下优点：
* 可以通过设置不同的日志登记，在release版本中只输出重要信息，而不必显示大量的调试信息。
* print将所有信息都输出到标准输出中，严重影响到开发者从标准输出中查看其它数据，logging则可以由开发者决定将信息输出到什么地方，以及怎么输出；

## logging模块使用
### 基本使用
配置logging基本的设置，然后在控制台输出日志
```
# coding=utf-8
import logging
import sys
# 获取logger实例，如果参数为空，则返回root logger
logger=logging.getLogger("AppName")
# 指定logger输出格式
formatter=logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
# 文件日志
file_handler = logging.FileHandler('test.log')file_handler.setFormatter(formatter) #可以通过setFormatter制定输出格式

# 控制台日志
console_handler=logging.StreamHandler(sys.stdout)
console_handler.formatter=formatter #也可以直接给formatter赋值 

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认欸warn级别
logger.setLevel(logging.INFO)
# 输出不同级别的log
# logger.debug('this is debug info')
# logger.info('this is infomation')
# logger.warn('this is warning message')
# logger.fatal('this is fatal message , it is same as logger.critical')
# logger.critical('this is critical message')
# '''
# 最后的输出结果为；
# 2018-03-11 16:52:00,288 INFO : this is infomation
# 2018-03-11 16:52:00,289 WARNING : this is warning message
# 2018-03-11 16:52:00,289 CRITICAL: this is fatal message , it is same as logger.critical
# 2018-03-11 16:52:00,289 CRITICAL: this is critical message
## '''
# #移除一些日志处理器
# logger.removeHandler(file_handler)
#
# service_name='Booking'
# logger.error('%s service is down '%service_name) 
# 使用python自带的字符串格式化，不推荐
# logger.error('%s service is down ',service_name) 
# 使用logger的格式化，推荐
# logger.error('%s service is %s',service_name,'down') 
# 多参数格式化
# logger.error('{}service is {} '.format(service_name,'down')) 
# 使用format函数，推荐
# 记录异常信息
```
```
try:
    1/0
except :
   # 等同于error级别，但是额外记录当前抛出的一场堆栈信息
    logger.exception('this is an exception message')
    # 最后的结果为：
    018-03-11 17:01:09,874 
    ERROR : this is an exception messageTraceback (most recent call last):
    File "E:/Envs/articlespider/loggingtest.py", line 55, 
    in <module>1/0ZeroDivisionError: division by zero
```
## logging 配置要点
Getlogger()方法这是基本的入口，该方法参数可以为空，默认的logger名称是root，如果在同一个程序中一直都使用同名的logger，其实会拿到同一个实例，使用这个技巧可以跨模块调用同样的logger来记录日志。另外，你也可以通过日志名称来区分同一程序的不同模块，比如这个例子。
```
logger = logging.getLogger('App.UI')
logger = logging.getLogger('App.service')
```
## formatter日志格式
Formatter对象定义了log信息的结构和内容，构造时需要带两个参数：
* 一个时格式化的模板fmt，默认会包含最基本的level和message信息
* 一个时格式化的时间样式datefmt，默认为 2003-07-08   16：49：45，896（%Y-%m-%d-%H:%M:%S）    

fmt允许使用的变量可以参考下表。
* %（name）s logger的名字
* %（levelno）s数字形式的日志级别
* %（levelname）s 文本形式的日志级别
* %（pathname）s 调用日志输出函数的模块的完整路径名，可能没有
* %（filename）s 调用日志输出函数的模块的文件名
* %（module）s  调用日志输出函数的模块名
* %（funcName）s 调用日志输出函数的函数名
* %（lineno）d 调用日志输出函数的语句所在的代码行
* %（created）f 当前时间，用UNIX标准的表示时间的浮点数表示
* %（relativeCreated）d  输出日志信息时的，自logger创建以来的毫秒数
* %（asctime）s 字符串形式的当前时间。默认格式时“2003-07-08 16:49:45,896”。逗号后面的是毫秒
* %（thread）d 线程id。可能没有
* %(threadName)s 线程名。可能没有
* %（process）d 进程id。可能没有   
* %（message）s 用户输出的消息。     

## Setlevel日志级别
logging有如下级别： 
    DEBUG、INFO、WARNING、ERROR 、CRITICAL
    默认级别是WARRNING,logging模块只会输出指定level以上的log。这样的好处，就是在项目开发时debug用的log，在产品release阶段不用一一注释，只需要调整logger的级别就可以了，很方便

## Handler日志处理器
最常用的时StreHandler和FileHandler ，HanLer用于向不同的输出端打log。
logging包含很多Handler，可能用到的有下面几种：

	* StreamHandler instances send error messages to streams(file -like objects)
	* FileHandler  instances send error messsages to disk files
	* Rotating FileHangler instances send error messages to disk files,with support for maximum log file sizes  and log file rotation
	* TimeRoatingFileHandles=r instances send error messages to disk files, roating the log file at certain timed intervals
	* SocketHandler instances send error messages to TCP/IP sockets
	* DatagramHandler instances send error messages to UDP sockets
	* SMTPHandler instances send error messages to a designated email address.        

## Configuration配置方法
logging的配置大致有下面几种方式
1. 通过代码进行完整配置，参考开头的例子，主要时通过getLogger方法实现 
2. 通过代码进行简单配置，下面有例子，主要是通过bassicConfig方法实现。
3. 通过配置文件，下面有例子，主要是通过logging.config.fileconfig(filepath)
   logging.basicConfigbasicConfig()
   提供了非常便捷的方式让你配置logging模块并马上开始使用，可以参考一下下面的例子。
   
    ```
    import logging
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.debug('This message should go to the log file') 
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.debug('This message should appear on the console') 
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('is when this event was logged.')
    ```
## 通过文件配置logging
如果你希望通过配置文件来管理logging，可以参考这个官方文档
