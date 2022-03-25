
Flask（瓶子，烧瓶）是使用Python编写的Web为框架，Web框架可以让我们不用关心底层的请求相应处理，更方便高效地编写Web程序。
因为Flask核心简单且已于扩展，所以被称作为框架。
Flask有2个主要依赖，一个是WSGI（Web Segver Gateway Inteface，Web服务器网关接口）工具集——Werkzeug。另一个是Jinjia2模板引擎
> WSGI是Python中用来规定Web服务器如何与PythonWeb程序进行沟通的标准。


## 1. 搭建开发环境
### 1.1 pipenv 工作流
pipenv是基于pip的python包管理工具，它和pip的用法非常相似，可以看作pip的加强版，它的出现解决了旧的pip+virtualenv+requirement.txt的工作方式的弊端。具体来说，它是pip、pipfile和virutalenv的结合体，它让包安装、包依赖管理和虚拟环境管理更加方便，使用它可以实现更高效的python项目开发工作流。
使用pip安装pipenv
```
pip install pipenv
```
##### 1.创建虚拟环境
使用pipenv install 命令为当前的项目创建虚拟环境。如果项目根目录下灭有Pipfile文件，就会创建Pipfile和Pipfile.lock文件，前者用来记录项目依赖包列表，后者记录了固定版本的详细依赖包列表。当我们使用Pipenv安装/删除/更新依赖包时，Pipfile和Pipfile.lock会自动更新：
```
pipenv nstall
```
>这会为当前项目创建一个文件夹，其中包含隔离的Python解释器环境，并且安装pip、wheel、setuptools等基本的包。
>默认情况下，Pipenv会同意管理所有虚拟环境，在Windows系统中，虚拟环境文件夹会在C:\Users\Administrator\.virtualenvs\目录下创建，而Linux或MacOS会在~/.local/share/virtualenvs/目录下创建。如果你想在项目目录内创建虚拟环境文件夹，可以设置环境变量PIPENV_VENV_IN_PROJECT,这时名为.vev的虚拟环境文件夹将在项目根目录创建。
```
export PIPENV_VENV_IN_PROJECT=1
```
>可以通过--three和--two选项来声明虚拟环境中使用的Python版本，或是使用--python选项指定具体的版本号。

在Pipenv中，可以使用pipenv shell命令显示地激活虚拟环境。退出使用exit：
```
pipenv shell
```
当执行pipenv shell 或pipenv run命令时，pipenv会自动从项目目录下的.env文件中加载环境变量。
除了显示地激活虚拟环境，pipenv还提供了一个pipenv run命令，这个命令允许你不显示地激活虚拟环境即可在当前项目的虚拟环境中执行命令，比如：
```
pipenv run python hello.py
```
##### 2.创建程序实例
```
from flask import Flask
app= FLask(__name__)
```
##### 3.注册路由
```
@app.route('/greet',defaults={'name':'Product'})   # 默认值
@app .route (’ / hi/<name> ' )  # 动态url
@app . route ( ' / hello ’)
def say hello () :
    return hl>Hello  Flask ' </hl> '
```

## 2. 启动开发服务器
```
flask run
```
### 2.1 自动发现程序实例
一般来说，在执行flask run命令运行程序前，我们需要提供程序实例所在模块的位置。我们在上面可以直接运行程序，是因为Flask会自动探测程序实例，自动探测存在下面这些规则：

* 从当前目录寻找app.py和wsgi.py模块，并从中寻找名为app或application的程序实例。
* 从环境变量Flask_APP对应的值寻找名为app或application的程序实例。
因为我们的程序主模块命名为app.py，所以flask run命令会自动在其中寻找程序实例。如果你的程序主模块是其他名称，比如hello.py，那么需要设置变量FlASK_APP，将包含程序实例的模块名赋值给这个变量。
Linux或macOS使用export命令：
```
export FLASK_APP = hello
```
在windows系统中使用set命令：
```
set FLASK_APP =hello
```
### 2.2管理环境变量
Flask的自动发现程序实例机制还有第三条规则：如果安装了pythonn-dotenv，那么在使用flask run或其他命令时会是使用它自动从.flaskenv文件和.env文件中加载环境变量。
>当安装了python-dotenv时，Flask在加载环境变量的优先级是：手动设置的环境变量>.env中设置的环境变量>.flaskenv设置的环境变量

我们在项目根目录下分别创建两个我呢见：.env和.flaskenv。.flaskenv用来存储和Flask相关的公开环境变量，比如FLASK_APP；而.env用来存储包含敏感信息的环境便令，比如我们会用来配置Email服务器的账户名和密码。在.flaskenv或.env文件中，环境变量使用键值对的形式定义，每行一个，以#开头的为注释，如下所示：
```
SOME_VAR=1
# 这是注释
FOO="BAR"
```
### 2.3 设置运行环境
开发环境和生产环境是我们后面会频繁接触到的概念。开发环境是指我们在本地编写和测试程序时的计算机环境，而生产环境与开发环境相对，它指的是网站部署上线用户访问的服务器环境。
根据运行环境的不同，Flask程序、扩展以及其他程序会改变相应的行为和设置。
我们将把环境变量FLASK_ENV的值写入.flaskenv文件中。
```
FLASK_ENV=development
```
>如果你想单独控制调试模式的开关，可以通过FLASK_DEBUG环境变量设置，设为1，则开启，设为0，则关闭。不过通常不推荐手动设置这个值。

**重载器**
默认会使用Werkzeug内置的stat重载器，它的缺点是耗电较验证，而且准确性一般。为了获得更优秀的体验，我们可以安装另一个用于监测文件变动的Python库Watchdog，安装后Werkzeug会自动使用它来监测文件变动：
```
pipenv install watchdog --dev
```
因为这个包只在开发时才会用到，所以我们在安装命令后添加了一个 --dev选项，这用来把这个包声明为开发依赖。在Pipefile文件中，这个包会被添加到dev-packages部分。
不过，如果项目中使用了单独的css或JS文件时候，那么浏览器可能会缓存这些文件，从而导致对文件做出的修改不能立刻生效。在浏览器中，我们可以按下Crtl+F5执行硬重载，即忽略缓存并重载（刷新）页面。

## 3. Flask扩展

以某扩展实现了 Foo 功能为例，这个扩展的名称将是 Flask Foo Foo-Flask ；程序包或模块的命名使用小写加下划线，即 flask foo 即导人时的名称 ；用于初始化的类一般为 Foo ，实例化的类实 般使用小 ，即 foo 初始化这个假想中的 ask Foo 扩展的示例如下所示：
```
from flask import Flask
from flask_foo impor Foo
app =Flask( __name__ )
foo =Foo (app)
```
## 4. 项目配置
在一个项目中，你会用到许多配置：Flask提供的配置，扩展提供的配置，还有程序特定的配置。和平时使用变量不同，这些配置变量都通过Flask对象的app.config属性作为统一的接口来设置和获取，它指向的Config类实际上是字典的子类，所以你可以像操作其他字典一样操作它。
```
app.config['ADMIN_NAME']= 'Peter'
```
使用update()方法则可以一次加载多个值：
```
app.config.update(
TESTTING=True,SECRET_KEY='_sadkowpqk_'
)
```
## 5. URL与端点
为了解决修改路由的问题，使用FLask提供的url_for()函数获取url，当路中定义的URL规则被修改时候，这个函数总会返回争取的URL。
```
@app .route (’ / ’ )
def index() :
    return ’ Hello Flask l ’
调用url_for（'index'）即可获取对应的URL，即'/'
```
## 6. Flask命令
通过创建任意一个函数，并为其添加app.cli.command()装饰器，我们就可以注册一个flask命令。
```
@app.cli.command()
def hello():
    click.echo(’hello ,Human‘)
```
在命令行下执行flask hello 就会出发这个hello()函数:
```
$flask hello
hello,Human
```
## 7. 模板与静态文件
默认情况下，模板文件存放在项目根目录中的templates文件中，静态文件放在static文件下。这两个文件需要和包含程序实例的模块处于同一个目录下，对应的项目结构示例如下所示：
>hello/
>   templates/
>   static/
>   app.py

## 8. Flask与MVC架构
术语views用来表示MVC（Model-View-Controller,模型-视图-控制器）架构中的View。
在MVC架构中，程序被分为三个组件：数据处理(Model)、用户界面（view）、交互逻辑（controller）。
严格来说，Flask并不是MVC架构的框架，因为它没有内置数据模型支持。为了方便描述，使用了app.route()装饰器的函数仍被称为书体函数，同时会使用<函数名>视图的形式来代指某个视图函数。
粗略归类，如果想要使用Flask编写一个MVC架构的程序，那么视图函数可以作为控制器，视图则是使用Jinja2渲染的HTML模板，而模型Model可以使用其他库来实现。

