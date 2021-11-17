# 学生表  student
|字段|类型|空|默认|注释|
|:---    |:-------    |:--- |---|------      |
|_id    |varchar(50)     |否 |  |学号             |
|s_name |varchar(20) |否 |    |姓名  |
|s_ename |varchar(50) |否   |    |英文名    |
|s_sex     |varchar(5) |是   |    |性别 |
|s_age |int(11)     |否   | 0  |年纪  |
|s_grade | varchar(20)    |否   | 0  |年级  |
|s_major |varchar(50)     |否   | 0  |专业  |
|s_phone |varchar(20)     |否   | 0  |电话  |
|s_birth |date|否   | 0  |生日  |
|s_school |varchar(50)     |否   | 0  |学校  |
|s_campus|varchar(20)     |否   | 0  |校区id  |
|s_venus |int(2)     |否   | 0  |是否为启明星  |
|s_online |int(2)     |否   | 0  |线上or线下  |
|insert_time |date     |否   | 0  |录取信息时间  |
|s_qstar |int(2)     |否   | 0  |问卷星是否填写  |
|s_transfer |int(2)     |否   | 0  |是否转班  |


# 学校表 school
|字段|类型|空|默认|注释|
|:---    |:-------    |:--- |---|------      |
|_id    |varchar(50)     |否 |  |学校id             |
|name |varchar(20) |否 |    |学校姓名  |
|address |varchar(50) |否   |    |学校地址    |
|pici     |varchar(10) |是   |    |批次 |
|level |varchar(10)     |否   | 0  |特色  |
|type | varchar(20)    |否   | 0  |类型  |
|major |varchar(50)     |否   | 0  |专业  |
|tuition |int(15)     |否   | 0  |学费  |
|students |int(20)|否   | 0  |学生人数  |
|year |date     |否   | 0  |年份  |
|insert_time |date     |否   | 0  |插入时间  |


# 课程表 course
|字段|类型|空|默认|注释|
|:---    |:-------    |:--- |---|------      |
|_id    |varchar(50)     |否 |  |课程id             |
|name |varchar(20) |否 |    |级别名称  |
|short_name     |varchar(5) |是   |    |简称 |
|level |int(11)     |否   | 0  |特色  |
|period | varchar(20)    |否   | 0  |课时  |
|tuition |varchar(50)     |否   | 0  |学费  |
|discount_type |varchar(20)     |否   | 0  |折扣类型  |
|discount |varchar(20)     |否   | 0  |折扣数字（将来折扣要另外一张表）  |
|status |date|否   | 0  |状态  |
|insert_time |date     |否   | 0  |插入时间  |


# 市场  market
|字段|类型|空|默认|注释|
|:---    |:-------    |:--- |---|------      |
|s_no    |varchar(50)     |否 |  |学号             |
|investor |varchar(20) |否 |    |邀请人  |
|morning_teacher     |varchar(20) |是   |    |晨读讲师 |
|public_teacher |varchar(20)     |否   | 0  |公开课讲师  |
|consult_teacher | varchar(20)    |否   | 0  |咨询师  |
|method |varchar(50)     |否   | 0  |招生方式  |
|insert_time |date     |否   | 0  |插入时间  |


# 员工信息  stuff
|字段|类型|空|默认|注释|
|:---    |:-------    |:--- |---|------      |
|_id    |varchar(50)     |否 |  |员工id             |
|name |varchar(20) |否 |    |员工姓名  |
|entry_time     |date |是   |    |入职时间 |
|departure_time|date     |否   | 0  |离职时间  |
|department | varchar(20)    |否   | 0  |部门  |
|level |varchar(50)     |否   | 0  |所属级别  |
|account |varchar(50)     |否   | 0  |账号  |
|password |varchar(50)     |否   | 0  |密码  |
|sex |varchar(50)     |否   | 0  |性别  |
|phone |varchar(50)     |否   | 0  |联系电话  |
|birth |varchar(50)     |否   | 0  |出生日期  |
|sign_time |date     |否   | 0  |最近登录时间  |
|sign_count |varchar(50)     |否   | 0  |登录次数  |
|status |int(3)     |否   | 0  |状态（离职、入职）  |
|family_address |varchar(50)     |否   | 0  |家庭住址  |
|insert_time |date     |否   | 0  |插入时间  |


# 启明星  venus
|字段|类型|空|默认|注释|
|:---    |:-------    |:--- |---|------      |
|_id    |varchar(50)     |否 |  |学生id             |
|inter_job |varchar(20) |否 |    |实习职位  |
|start_time     |date |是   |    |入职时间 |
|departure_time|date     |否   | 0  |离职时间  |
|insert_time |date     |否   | 0  |插入时间  |


# 收支表  finance
|字段|类型|空|默认|注释|
|:---    |:-------    |:--- |---|------      |
|_id    |varchar(50)     |否 |  |学号             |
|tuition |int(20) |否 |    |学费  |
|pay_method     |date |是   |    |支付方式 |
|discount_method|date     |否   | 0  |优惠方式  |
|level_id|date     |否   | 0  |级别id  |
|campus_id|date     |否   | 0  |校区id  |
|note|date     |否   | 0  |备注  |
|pay_time |date     |否   | 0  |缴费时间  |
|cs_teacher |date     |否   | 0  |客服老师  |