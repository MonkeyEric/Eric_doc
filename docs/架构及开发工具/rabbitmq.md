# python之rabbitMq

## 1.简单模式
生产者:
* 链接rabbitmq
* 创建队列
* 向指定队列插入数据
```python
### 生产者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',duable=True)

channel.basic_publish(exchange='',
                      routing_key='hello', # 指定队列
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                          ))

print(" [x] Sent 'Hello World!'")

```
消费者
* 链接rabbitmq
* 监听模式
* 确定回调函数
```python
### 消费者

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello',duable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello',
                      auto_ack=True, # 默认应该
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```
### 1.1 修改为手动应答
将consumer.py中的callback 和basic_consume进行修改
> 优点：确保数据真正的被执行
> 
> 缺点：响应时间变慢
```python
def callback(ch, method, properties, body):
    
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
channel.basic_consume(queue='hello',
                      auto_ack=False, # 修改为手动应答
                      on_message_callback=callback)
```

### 1.2持久化响应
若是持久化，使用queue_declare,将durable=True，
在生产中的basic_publish修改为:
```python
channel.basic_publish(exchange='',
                      routing_key='hello2',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                          )
                      )
```
> 优点：生产者被down掉了，数据还在

### 1.3 分发参数
在consumer的callback中添加
```python
channel.basic_qos(prefetch_count=1)
```

## 2.交换机模式
### 发布订阅
```python
# 生产者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

# 消费者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare("",exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()
```
### 关键字
```python
# 生产者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs2',
                         exchange_type='direct')

message = "info: Hello Yuan!"
channel.basic_publish(exchange='logs2',
                      routing_key='info',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

# 消费者

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs2',
                         exchange_type='direct')

result = channel.queue_declare("",exclusive=True)
queue_name = result.method.queue


severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='logs2',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()
```
### 通配符
```python
# 生产者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs3',
                         exchange_type='topic')

message = "info: Hello ERU!"
channel.basic_publish(exchange='logs3',
                      routing_key='europe.weather',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

# 消费者

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs3',
                         exchange_type='topic')

result = channel.queue_declare("",exclusive=True)
queue_name = result.method.queue



channel.queue_bind(exchange='logs3',
                   queue=queue_name,
                   routing_key="#.news")

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()
```


[参考博客链接](https://www.cnblogs.com/pyedu/p/11866829.html)
[博客对应视频链接](https://www.bilibili.com/video/BV12A411q7dE?p=7&spm_id_from=pageDriver)
[centos安装rabbitMq链接](https://www.cnblogs.com/fengyumeng/p/11133924.html)
[windows安装rabbitMq链接](https://blog.csdn.net/xtjatswc/article/details/107294414)
[windows下载rabbitMq链接](https://www.jb51.net/softs/653521.html)
