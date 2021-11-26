### 前言
如果我们要把程序部署到其他地方的服务器上，供更多人访问，可能会出现失去的问题，所以可以使用flask-moment来解决。

首先使用pipenv 安装
```
pipenv install flask-moment
```

然后我们实例化扩展提供的Moment类，并传入程序实例app，以完成扩展的初始化；
```
from flask_moment import Moment
app = Flask(__name__)
moment = Moment(app)
```

**Flask-Moment默认以英文显示时间，我们可以传入区域字符串到locale()方法来更改显示语言**
```
{{ moment.locale('zh-cn')}}
```
**更合理的方式是根据用户浏览器或计算机的语言来设置语言**
```
{{ moment.locale(auto_detect=True)}}
```

### 渲染时间日期
**format()方法接受特定的格式字符串来渲染时间格式**，比如：
```
{{ moment(timestamp).format('格式字符串') }}
```


| 格式字符串 | 输出示例 |
| --- | --- |
|L  |2017-07-26  |
|LL  |2017年7月26日  |
|LLL  |2017年7月26日早上8点00分  |
|LLLL  |2017年7月26日星期三早上8点00分  |
|LT  |早上8点00分  |
|LTS  |早上8点0分0秒  |
|lll  |2017年8月10日 03:23  |
|llll  |2017年8月10日 星期四03:23  |

**支持输出相对时间**。比如相对于当前时间的”三分钟前“等。
```
<small>{{ moment(moment.timestamp).fromNow(refresh=True) }}</small>
```
**当鼠标悬停再问候消息的时间日期上时，希望能够显示一个包含具体的绝对时间的弹出窗口**
```
<small data-toggle="tooltip” data- placement= "top " data delay=” 500 ”data- timestamp= ” {{ message timestamp strftime dT sz ’） ｝｝
{ { moment (message . times tamp) . fromNow (refresh=True) } }
</small>
```
我们js中将时间日期对应元素的tooltip内容设置为渲染后的时间日期：
```
$(function(){
    function render_time() {
    return moment($(this).data('timestamp').format('lll'))
    }
    $('[data-toggle="tooltip"]').tooltip)
    {title:render_time});
});

```
