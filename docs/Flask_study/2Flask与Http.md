[TOC]
常见的HTTP方法

| 方法 |说明  |方法  |说明  |
| --- | --- | --- | --- |
|GET  |获取资源  |DELETE  |删除资源  |
|POST  |传输数据  |HEAD  |获得报文首部  |
|PUT  |传输文件  |OPTIONS  |询问支持的方法  |

使用request属性获取请求URL

| 属性 |值  |属性  |值  |
| --- | --- | --- | --- |
|path  |u'/hello'|base_url  |http://helloflask.com/hello  |
|full_path  |u'/hello?name=Grey' |url  |http://helloflask.com/hello?name=Grey  |
|host  |u'helloflask.com' |url_root  |http://helloflask.com/  |
|host_url  |http://helloflask.com  |  |  |

request对象最常用的属性和方法

| 属性/方法 |说明  |
| --- | --- |
|agrs  |Werkzeug的ImmutableMultiDict对象。存储解析后的查询字符串，可通过字典方式获取键值。如果你想要获取未解析的原生查询字符串，可以使用query_string属性  |
|blueprint  |当前蓝本的抿成  |
|cookies  |一个包含所有随请求提交的cookies字典  |
|data  |包含字符串形式的请求数据  |
|endpoint  |与当前请求相匹配的端点值  |
|files  |Werkzeug的MultiDict对象，包含所有上传文件，可以使用字典的形式获取文件。使用的键未文件input标签中的name属性值，对应的值为Werkzeug的FileStorage对象，可以调用save()方法并传入保存路径来保存文件  |
|form  |Werkzeug的ImmutableMultiDict对象。包含解析后的表单数据，表单字段值通过input标签的name属性值作为键获取  |
|values  |Werkzeug的CombineMultiDict对象，结合了args和form属性的值  |
|get_data（cache=True,as_text=False,parse_from_data=False）  |获取请求中的数据，默认读取为字节字符串，将as_text设为True，则返回值将是解码后的unicode字符串  |
|get_json(self,force=False,silent=False,cache=True)  |作为Json解析并返回数据，如果MIME类型不是JSON，返回None（除非force设为True）；解析出错则抛出Werkzeug提供的Badrequest一场，如果slient设为True，则返回True；cache设置是否缓存解析后的Json数据|
|headers  |一个Werkzeug的EnvironHeaders对象，包含首部字段，可以以字典的形式操作  |
|is_json  |通过MIMIE类型判断是否为JSON数据，返回布尔值  |
|json  |包含解析后的JSON数据，内部调用get_json()，可通过字典的方式获取键值  |
|method  |请求的http方法  |
|referrer  |请求发起的源url，即referer  |
|scheme  |请求的URL模式，http或https  |
|user_agent  |用户代理，包含了用户的客户端类型，操作系统类型等信息  |

>Werkzeug的MutiDict类是字典的子类，它主要实现了同一个键对应多个值的情况。比如一个文件上传字段可能会接受多个文件。这时就可以通过getlist()方法来获取文件对象列表。而ImmutableMultiDict继承了MutilDict类，但其值不可更改。

**查看程序中定义的路由**
```
flask routes
```
在输出的文件中，我们可以看到每个路由对用的端点、http方法和url规则，其中static端点是flask添加的特殊路由，用来访问静态文件。

### 1.URL处理
Flask内置的URL变量转换器

| 转换器 |说明  |
| --- | --- |
|string  |不包含斜线的字符串（默认值）  |
|int  |整型  |
|float  |浮点型  |
|path  |包含斜线的字符串。static路由的URL规则中的filename变量就使用了这个转换器  |
|any  |匹配一系列给定值中的一个元素  |
|uuid  |UUID字符串  |
**实例**
```
@app . route (’ goback/<int :year> ’)
def go_back (year) :
    return ' <p>Welcome to d'</p> （2018- year)
```

### 2. 请求钩子
有时我们需要对请求进行预处理(preprocessing)和后处理(postprocessing)，这时可以使用Flask提供的一些请求钩子HOOK，他们可以用来注册在请求处理的不同阶段执行的处理函数（或称为回调函数）。这些请求钩子使用装饰器实现，通过程序实例app调用，用法很简单；以before_request钩子为例，当你对一个函数附加了app.before_request装饰器后，就会将这个函数注册为before_request处理函数，每次执行请求前都会触发所有before_request处理函数。
**请求钩子**


| 钩子 |说明  |
| --- | --- |
|before_first_request  |注册一个函数，在处理第一个请求前运行  |
|before_request  |注册一个函数，在处理每个请求前运行  |
|after_request  |注册一个函数，如果没有未处理的异常抛出，会在每个请求结束后运行  |
|teardown_request  |注册一个函数，即使有未处理的一场抛出，会在每个请求结束后运行。如果发生一场，会传入一场对象作为参数到注册的函数中。  |
|after_this_request  |在视图函数内注册一个函数，会在这个请求结束后运行  |

下面是请求钩子的一些常见应用场景：
* before_first_request
在玩具程序中，运行程序前我们需要进行一些程序的初始化操作，比如创建数据表，添加管理员用户。这些工作可以放到使用before_first_request装饰器注册的函数中。
* before_request:比如网站上要记录用户最后在线的世家，可以通过用户最后发送的请求时间来实现。为了避免每个视图函数都添加更新在线时间的代码，我们可以仅在使用before_request钩子注册的函数中调用这段代码。
* after_request：我们经常在视图函数中进行数据库擦欧总，比如更新、插入等，之后需要将更改提交到数据库中。提交更改的带啊吗就可以放到after_request钩子注册的函数中。

![972ac9017f6fa27cf4537c313f6fb582.png](en-resource://database/1878:0)

另一种常见的应用是建立数据库链接，通常会有多个视图函数需要建立和关闭数据库链接，这些操作基本相同。一个理想的解决方法是在请求之前before_request建立链接，在请求之后teardown_request关闭链接。通过在使用相应的请求钩子注册的函数中添加代码就可以实现。这很像单元测试中的setUp()和tearDown()方法。


### 3.HTTP响应
常见的HTTP状态码

| 类型 |状态码  |原因短语  |说明  |
| --- | --- | --- | --- |
|成功  |200  |ok  |请求被正常处理  |
|  |201  |created  |请求被处理，并创建了一个新资源  |
|  |204  |No Content  |请求处理成功，但无内容返回  |
|重定向  |301  |Moved Permanently  |永久重定向  |
|  |302  |Found  |临时性重定向  |
|  |304  |Not Modified  |请求的资源未被修改，重定向到缓存的资源  |
|客户端错误  |400  |Bad Request  |表示请求无效，即请求报文中存在错误  |
|  |401  |Unauthorized  |类似403，表示请求的资源需要获取授权信息，在浏览器中弹出认证弹窗  |
|  |403  |Forbidden  |表示请求的资源被服务器拒绝访问  |
|  |404  |Not Found  |表示服务器上无法找到请求的资源或URL无效  |
|服务器错误  |500  |Internal Server Error  |服务器内部发生错误  |

#### 3.1 在Flask中生成响应
响应在Flask中使用Response对象表示，响应报文的大部分内容由服务器处理，大多数情况下，我们只负责返回主体内容。
当请求的时候，Flask会先判断是否可以找到与请求URL相匹配的路由，如果，没有则返回404响应。如果找到，则调用对应的视图函数，视图函数的返回值构成了响应报文的主体内容。**Flask会调用make_response()方法将视图函数返回值转换为响应对象**
完整地说，视图函数可以返回最多由三个元素组成的元组：响应主体、状态码、首部字段。其中首部字段可以为字典，或是两元素元组组成的列表：
指定不同的状态码：
```
@app.route('/hello')
def hello():
    return '<h1>hello,flask</h1>',201
```
修改首部字段，例如重定向(也可以使用redirect)：
```
@app.route('/hello')
def hello():
    return '<h1>hello,flask</h1>',302,('Location','http:www.expample.com')
```
#### 3.2 响应格式
```
from flask import make_response
@app.route('/foo')
def foo():
    response = make_response('Hello,World!')
    response.mimetype = ''text/plain'
    return response
```

#### 3.2 cookie
>Cookie指Web服务器为了存储某些数据（比如用户信息）而保存在浏览器上的小型文本数据。浏览器会在一定时间内保存它，并在下一次向同一个服务器发送请求时附带这些数据。cookie通常被用来进行用户绘画管理，保存用户的个性化信息以及记录和收集用户浏览数据以用来分析用户行为等。

在Flask中，如果想要在响应中添加一个cookie，最方便的方法是使用Response类提供的set_cookie()方法。要使用这个方法，需要先使用make_response()方法手动生成一个响应的对象，传入响应主体作为参数。
**Response类的常用属性和方法**

| 方法/属性 |说明  |
| --- | --- |
|headers  |一个Werkzeug的Headers对象，表示响应首部，可以像字典一样操作  |
|status  |状态码，文本类型  |
|status_code  |状态码，整型  |
|mimetype  |MIME类型  |
|set_cookie()  |用来设置一个cookie  |

**set_cookie()方法的参数**

| 属性 |说明  |
| --- | --- |
|key  |cookie的键  |
|value  |cookie的值  |
|max_age  |cookie被保存的时间数，单位为秒；默认在用户会话结束时过期  |
|expires  |具体的过期时间，一个datetime对象或Unix时间戳  |
|path  |限制cookie只在给定的路径可用，默认为整个域名  |
|domain  |设置cookie可用的域名  |
|secure  |如果设置为True，只有通过https才可以使用  |
|httponly  |如果设为True，禁止客户端Javascript获取cookie  |
实例：
```
from flask import Flask,make_response
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name',name)
    return response
```

#### 3.3 session：安全的cookie
在浏览器中手动添加和修改cookie是很容易的事，仅仅通过浏览器插件就可以实现，为了避免恶意用户伪造cookie，我们需要对敏感的cookie内容进行加密。
>在编程中，session指用户会话，又称为对话，即服务器和客户端/浏览器之间或桌面程序和用户之间建立的交互活动。在Flask中，session对象用来加密cookie。默认情况下，它会把数据存储在浏览器上一个名为session的cookie里。

1. 设置程序密钥
session通过密钥对数据进行签名以加密数据，因此，我们得先设置一个密钥。这里的密钥就是一个具有一定复杂度和随机性的字符串。
程序的密钥可以通过Flask.sercet_key属性或配置变量SECRET_KEY设置，比如：
```
app.secret_key = 'secret string'
```
更安全的做法是把密钥写进系统环境变量，或是保存在.env文件中。
```
SECRET_KEY = secret string
import os
app.secret_key = os.getenv('SECRET_KEY','secret string')
```
2. 模拟用户认证
这个登录只是简化的实例，在实际的登录中，我们需要在页面上提供登录表单，供用户填写账户和密码，然后在登录视图里验证账户和密码的有效性。
```
from flask import redirect,session,url_for
@app.route('/login')
def login():
    session['logged_in'] = True  # 写入session
    return redirect(url_for('hello'))
```
当支持用户登录后，我们就可以根据用户的认证状态分别显示不同的内容。在login视图的最后，我们将程序重定向到hello视图：
```
from flask import request,session
@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    response = '<h1>hello ,%s</h1>'%name
    # 根据用户认证状态返回不同的内容
    if 'logged_in' in session:
        response+='[Authenticated]'
    else:
        response+= '[Not Authenticated]'
    return response
```
程序中的某些资源仅提供给登入的用户，比如管理后台，这时我们就可以通过判断session是否存在logged_in键来判断用户是否认证
```
from flask import session,abort
@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page'
```
logout视图
```
from flask import session
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))
```

### 4. Flask上下文
我们可以把编程中的上下文理解为当前环境的快照。Flask中有两种上下文，程序上下文和请求上下文。如果鱼想要存活，水是必不可少的元素。对于Flask程序来说，程序上下文就是我们的谁。水里包含了各种浮游生物以及微生物，正如程序上下文中存储了程序运行所必须的信息；要想健康地活下去，鱼还离不开阳关。射进鱼缸的阳光就是我们的程序接受的请求。当客户端发来请求时，请求上下文就登场了。请求上下文里包含了请求的各种信息，比如请求的URL，请求的HTTP方法等。

#### 4.1 Flask中的上下文全局变量

| 变量名 |上下文类别  |说明  |
| --- | --- | --- |
|current_app  |程序上下文  |指向处理请求的当前程序实例  |
|g  |程序上下文  |替代Python的全局变量用法，确保仅在当前亲亲贵中可以用。用于存储全局数据，每次请求都会重设  |
|request  |请求上下文  |封装客户端发出的请求报文数据  |
|session  |请求上下文  |用于记住请求之间的数据，通过签名的cookie实现  |

>为什么需要使用current_app？
在不同的视图函数中，request对象都表示和视图函数对应的请求，也就是当前请求。而程序也会有多个程序实例的情况，为了能获取对应的程序实例，而不是固定的某一个程序实例，我们就需要使用current_app变量，后面会详细介绍。

>flask中的g的介绍
因为g存储在程序上下文中，而程序上下文会随着每一个请求的进入而激活，随着每一个请求的处理完毕而销毁，所以每次请求都会重设这个值。
我们通常会使用它结合请求钩子来保存每个请求处理前所需要的全局变量，比如当前登入的用户对象，数据库链接。
在前面的示例中，我们在hello视图中从查询字符串获取name的值，如果每一个视图都需要这个值，那么就要在每个视图重复这行代码。**借助g我们可以将这个操作移动到before_request处理函数中执行，然后保存到g的任意属性上**
```
from flask import g
@app.before_request
def get_name():
    g.name = request.args.get('name')
```

#### 4.2 激活上下文
在下面这些情况下，Flask会自动帮我们激活程序上下文：

* 当我们使用flask run命令启动程序时
* 使用旧的app.run()方法启动程序时
* 执行使用@app.cli.command()装饰器注册的flask命令时
* 使用flask shell命令启动Python Shell时。

当请求上下文被激活时，程序上下文也被自动激活。当请求处理完毕后，请求上席文和程序上下文也会自动销毁。

如果你需要在没有激活上下文的情况下使用这些变量，可以手动激活上下文。
比如，下面是一个普通的Python shell，通过python命令打开。程序上下文对象使用app.app_context()获取，我们可以使用with语句执行上下文操作。
```
>>>from app import app
>>>from flask import current_app
>>>with app.app_context():
        current_app.name
 'app'
```
或是显式地使用push()方法推送（激活）上下文，在执行完相关操作时使用pop()方法销毁上下文：
```
>>> from app import app
>>> from flask import current_app
>>>app_ctx = app.app_context()
>>>app_ctx.push()
>>>current_app.name
'app'
>>>app_ctx.pop()
```
而请求上下文可以通过test_request_context()方法临时创建：
```
>>> from app import app
>>> from flask import request
>>> with app.test_request_context('/hello'):
        request.method
 'GET'
```

#### 4.3 上下文钩子
Flask为上下文提供了一个teardown_appcontext钩子，使用它注册的回调函数会在程序上下文被销毁时调用，而且通常也会在请求上下文被销毁时调用。比如，你需要在每个请求处理结束后销毁数据链接。
```
@app.teardown_appcontext
def teardown_db(exception):
    db.close()
```

### 5.HTTP进阶实践
#### 5.1 重定向回上一个页面
示例：三个视图函数，foo、bar、do_something。我们希望这个视图在执行完相关操作后能够重定向回上一个页面。
```
@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href ="%s">Do something</a>' % url_for('do_something')
    
 @app.route('/bar')
 def bar():
     return '<h1>Bar page</h1><a href ="%s">Do something</a>'%url_for('do_something')

@app.route('/do_something')
def do_something():
    return redirect(url_for('hello'))

```
1.获取上一个页面的URL
有两种方式获取：

* Http referer
这是一个用来记录请求发源地址的HTTP首部字段，即访问来源。
```
return redirect(request.referrer or url_for('hello'))
```
* 查询参数
在URL中手动加入包含当前页面URL的查询参数，这个查询参数一般名为next。
```
@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href ="%s">Do something and redirect</a>' % url_for('do_something',next=request.full_path)
    
 @app.route('/bar')
 def bar():
     return '<h1>Bar page</h1><a href ="%s">Do something and redirect</a>'%url_for('do_something',next=request.full_path)
```
这里使用request.full_path获取当前页面的完整路径。在do_something视图中，我们获取这个next值，然后重定向到对应的路径：
```
@app.route('/do_something')
def do_something():
    return redirect(request.args.get('next'))
```
2.对url进行安全验证
如果使用next，很容易被攻击者伪造，比如：http://exampleA.com/login?next=http://maliciousB.

**验证URL安全性**
```
from urlparse import urlparse,urljoin
from flask import request
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(reqeust.host_url,target))
    return test_url.scheme in ('http','https') and ref_url.netloc ==test_url.netloc
```
这个函数接受目标URL作为参数，并通过request.host_url获取程序内的主机URL，然后使用urljoin()函数将目标URL转换为绝对URL。接着，分别使用urlparse模块提供的urlparse()函数解析两个URL，最后对目标URL的URL模式和主机地址进行验证，确保只有属于程序内部的URL才会被返回。在执行重定向回上一个页面的redirect_back()函数中，我们使用is_safe_url()验证next和referer的值：
```
def redirect_back(default='hello',**kwagrs):
    for target in request.args.get('next'),request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default,**kwagrs))
```
#### 5.2 使用Ajax技术发送异步请求
ajax()函数支持的参数

| 参数 |参数值类型及默认值  |说明  |
| --- | --- | --- |
|url  |字符串；默认为当前页地址  |请求的地址  |
|type  |字符串；默认为GET  |HTTP方法，比如GET、POST、DELETE  |
|data  |字符串；无默认值  |发送到服务器的数据，会被Jquery自动转换为铲鲟字符串  |
|dataType  |字符串；默认由Jquery自动判断  |期待服务器返回的数据类型，可用的值如下："xml","html","script","json","jsonp","text"  |
|contentType  |字符串；  |发送请求时使用的内容类型，即请求首部的Content-Type字段内容  |
|complete  |函数  |请求完成后调用的回调函数  |
|success  |函数  |请求成功后调用的回调函数  |
|error  |函数  |请求失败后调用的回调函数  |

#### 5.3 Web安全防范
1. 注入攻击，主要防范方法

* 使用ORM可以一定程度上避免SQL注入问题
* 验证输入类型。比如某个视图函数接收整型id来查询，那么就在URL规则中限制URL变量为整型
* 参数化查询。在构造SQL语句时**避免使用拼接字符串或字符串格式化（使用百分号或format()方法）的方式创建SQL语句**，而要使用各类接口库提供的参数化查询方法，以内置的sqlite3库为例：
```
b . execute (’ SELECT * FROM students WHERE password＝？，password)

```
* 转义特殊字符，比如引号、分号和横向等。使用参数化查询时，各种接口库会为我们做转义工作。
2. XSS攻击，跨站脚本
* 攻击原理
XSS是注入攻击的一种，攻击者通过将代码注入被攻击者的网站中，用户一旦访问网页便会执行被注入的恶意脚本。XSS主要分为反射型XSS攻击和存储型攻击
* 防范措施
HTML转义
```
from jinjia2 import escape
@app.route('/hello')
def hello():
    name=request.args.get('name')
    response = '<h1>hello,%s</h1>'%escape(name)
```
验证用户输入
3. CSRF攻击
* 攻击原理
某用户登录了A网站，认证信息保存在cookie中。当用户访问攻击者创建的B网站时，攻击者通过在B网站发送一个伪造的请求提交到A网站服务器上，让A网站服务器误以为请求来自于自己的网站，于是执行相应的操作，该用户的信息便遭到了篡改。
* 防范措施
正确使用HTTP方法，CSRF令牌校验。