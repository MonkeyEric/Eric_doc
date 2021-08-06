# 博客网站的数据结构

## admin 用户

|字段|类型	|空	|默认	|注释|
|:---|:--------- |:--- |---|------|
|id	|integer	|否	|	|主键|
|role	|varchar(10)	|否	|	|普通用户、VIP用户、管理员、SVIP（1人）|
|email	|varchar(20)	|否	|	|邮件|
|password_hash|	varchar(130)|	否|	|	|密码|
|blog_title	|varchar(20)|	是	|	|博客标题|
|blog_sub_title|	varchar(20)|	否	|	|博客副标题|
|name	|varchar(20)|	否|	|	|昵称|
|about	|text|	是|	|	|关于（简介）|
|timestamp	|datetime|	否|	|	|插入数据库时间|
|last_login_time|	datetime	|否	|	|上次登录时间|
|avatar_path|	varchar(30)|	否|	|	头像存放路径|


## post 文章	
|字段|类型|空|默认|注释|
|:---|:--------- |:--- |---|------|
|id|integer|否| |	主键|
|title|	varchar（80）|否| |标题|
|body|text|否| |文章内容|
|timestamp|datetime|	否|		|文章发布时间|
|can_comment|boolean|	否	|TRUE	|是否可以评论|
|author_id|integer|	否	|	|作者id|
|category_id|integer|	否|	|	标签id|
|post_cover|varchar（30）|	否	|随机选择	|自己建立一个封面文件夹，然后随机获得封面|
|category|外键| |	|post的category|
|comments|外键|	|	|post的comments|

