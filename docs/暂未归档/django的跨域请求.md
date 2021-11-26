# Django 跨域请求

同源策略首先基于安全的原因，浏览器是存在同源策略这个机制的，同源策略阻止从一个源加载的文档或脚本获取或设置另一个源加载的文档的属性。
而我们要跳过策略，也就是非要跨域请求，那么久需要通过JSONP或者CORS来实现
## 什么是JSONP？

首先提一下json这个概念，json是一种轻量级的数据传输格式，被广泛应用于当前web应用中。JSON格式数据的编码和解析基本在所有主流语言中都被实现，所以现在大部分前后端分离的架构都以JSON格式进行数据的传输。

	那么什么是JSONP呢？

	在ajax中，不允许请求非同源的URL就可以来，比如www.a.com下的一个页面，其中的ajax请求是不允许访问www.b.com/c.js这样一个页面的。
	
	JSONP就是用来解决跨域请求问题的，那么具体是怎么实现的？
**JSONP原理**

ajax请求受同源策略影响，不允许进行跨域请求，而script标签src属性中的链接却可以访问跨域的js脚本，利用这个特性，服务端不再返回JSON格式的数据，而是返回一段调用某个函数的js代码，在src中进行了调用，这样实现了跨域。JSONP的具体实现
127.0.0.1:8000中的index.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>GoJSONP</title>
</head>
<body>
 $(".jsonp_test").click(function () {
    $.ajax({
        url:"http://127.0.0.1:8008/service/",
        type:"get",
        dataType:"jsonp",     // 伪造ajax  基于script
        jsonp: 'callbacks',
        //jsonpCallback:"alex",
        success:function (data) {
            console.log(data)
        }
    })
})
<button class='jsop_test'>测试</button>
</body> </html>
```
127.0.0.1:8080的views
```python
import json
def jsonp_test(request): 
    func=request.GET.get("callbacks") #获取请求的callbacks参数
    info={"name":"fuyong","age":18} #定义数据
    return HttpResponse(" ('%s')"%(func,json.dumps(info))) #传json对象总结
```
一句话就是利用script标签绕过同源策略，获得一个类似这样的数据。ajax里边的callback本质上是（伪装成scripy标签src属性发送请求的方式）发送一个回调方法，参数data就是想得到的json数据。
## corscors定义
**Cross-origin Resource Sharing(CORS)跨来源资源共享是一份浏览器技术的规范，提供了web服务从不同域传来沙盒脚本的方法，以避开浏览器的同源策略，是JSONP模式的现代版。与JSONP不同，CORS除了GET要求方法以外也支持其他的HTTP请求。用CORS可以让网页设计师用一般的XMLHttpRequest，这种方法的错误处理比JSONP要来的好。另一方面，JSONP可以在不支持CORS的老旧浏览器上运作，现代的浏览器都支持CORS。**
## cors和jsonp的对比
* JSONP只能实现GET请求，而CORS支持所有类型的HTTP请求
* 使用CORS，开发者可以使用普通的XMLHttpRequest发起请求和获得数据，比起JSONP有更好的错误处理
* JSONP主要被老的浏览器支持，它们往往不支持CORS，而绝大多数现代浏览器都已经支持了CORS。

## 简单请求和复杂请求
简单请求
1. http方法这三种方法之一：HEAD、GET、POST
2. HTTP头消息不超出以下字段：Accept、Accept-language、Content-Language、Last-Event-ID，且Content-Type只能为下列类型中的某一个:
	
	* application/x-www-from-urlencoded
	* multipart/form-data
	* text/plain.

任何不满足上述要求的请求，都会被认为是复杂请求。

复杂请求回先发出一个预请求—预检，OPTIONS请求。cors实现思路
cors背后的基本思想是使用自定义的http头部允许浏览器和服务器相互了解对方，从而决定请求或相应成功与否。

例如localhost:63343通过ajax请求http:192.16810.61:8080服务器资源时就会出现如下异常：

其实数据已经获取到了，但是由于同源策略的限制给禁止了，提示说header里没有access-Control-Allow-Origin，那么，我们在发送响应的时候只需要给header加上这个参数就可以了。通过中间件实现cors

第一步，准备中间件
```python
from django.utils.deprecation import MiddlewareMixin 
class MyCors(MiddlewareMixin): 
	def process_response(self, request, response): # 如下，等于'*'后，便可允许所有简单请求的跨域访问 response['Access-Control-Allow-Origin'] = '*' # 判断是否为复杂请求 if request.method == 'OPTIONS': response['Access-Control-Allow-Headers'] = 'Content-Type' response['Access-Control-Allow-Methods'] = 'PUT,PATCH,DELETE' return response
```
第二步 视图文件
```python
from django.http import HttpResponse from rest_framework.views import APIView 
class TestView(APIView): 
def get(self, request): 
	return HttpResponse("这是GET请求的数据") 
def post(self, request): 
	return HttpResponse("这是POST请求的数据") 
def put(self, request): 
	return HttpResponse("这是PUT请求的数")
settings.py

MIDDLEWARE = [
   .....
 
    'xxx.cors.CORSMiddleware',  # xxx为cors.py所在包的目录
]
```