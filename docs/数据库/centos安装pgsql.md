
> 注意：本环境是基于centos8，其他可能不适合，谨慎使用
## 一、安装流程
1. 列出可用的PostgreSQL模块流，请输入:
```shell
dnf module list postgresql
```
输出显示可用的postgresql.每个个都包含服务器喝客户端，postgresql10是默认设置。【可以通过stream数字后边如何包含d,就是默认设置】

2. 安装默选项的postgresql服务器版本10.0，直接如下安装命令:
```shell
sudo dnf install @postgresql:10
```
安装其他版本的，请输入:
```shell
sudo dnf install @postgresql:9.6
```
3. 你可能还需要安装contrib软件包，该软件包为postgreSQl数据库提供了一些附加的功能
```shell
sudo dnf install postgresql-contrib
```
4. 安装完成后，初始化PostgreSQL数据库:
```shell
sudo postgresql-setup initdb
```
输出
```shell
Initializing database ... OK
```
5. 启动PostgreSQL服务，并配置为其能够在系统启动时启动：
```shell
sudo systemctl enable --now postgresql
```
6. 验证是否安装成功，使用该psql工具通过连接到PostgreSQL数据库服务器来验证安装并打印其版本
```shell
sudo -u postgres psql -c "SELECT version();"
```
输出：
```shell
PostgreSQL 10.6 on x86_64-redhat-linux-gnu, compiled by gcc (GCC) 8.2.1 20180905 (Red Hat 8.2.1-3), 64-bit
```

## 二、角色和验证方法
PostgreSQL支持多种身份验证方法。最常用的方法是：

* 信任-只要符合定义的条件，角色就可以不使用密码进行连接pg_hba.conf。
* 密码-角色可以通过提供密码进行连接。密码可以存储为scram-sha-256，md5和password（明文）。
* 标识符-仅在TCP/IP连接上受支持。它通过获取客户端的操作系统用户名以及可选的用户名映射来工作。
* 对等-与Ident相同，但仅在本地连接上受支持。
访问配置文件路径:
```shell
/var/lib/pgsql/data/pg_hba.conf
```

PostgreSQL客户端身份验证在名为pg_hba.conf的配置文件中定义。默认情况下，对于本地连接，PostgreSQL设置为使用对等身份验证方法。

在你安装PostgreSQL服务器过程中postgres用户会被自动创建。该用户是PostgreSQL实例的超级用户，你可以看成等效于MySQL的root用户。

要以postgres用户身份登录到PostgreSQL服务器，需要首先切换到该用户，然后运行psql命令程序访问PostgreSQL提示符：

```shell
sudo su - postgres
psql
```
退出，输入q.
## 三、创建角色、数据库、设置密码
1. 进入到PostgreSQL shell
```shell
sudo -u postgres psql
```
2. 创建角色
```shell
create role john;
```
3. 创建数据库
```shell
create database johndb;
```
4. 将数据库授权用户：
```shell
grant all privileges on database johndb to john;
```
5. 给默认用户postsql添加密码
```shell
alter role postgres with password 'xiaosan121009';
```
6. 重启服务
```shell
sudo systemctl restart postgresql
或者
sudo systemctl reload postgresql
```

## 四、远程访问
系统配置文件路径:
```shell
/var/lib/pgsql/10/data/postgresql.conf
```
打开配置文件，进行如下修改:
```shell
listen_address='*'
```
重启服务:
```shell
sudo systemctl restart postgresql
```
使用ss实用程序验证更改：
```shell
ss -nlt | grep 5432
```
上面的输出显示PostgreSQL服务器正在所有接口（0.0.0.0）的默认端口上侦听。

最后一步是通过编辑/var/lib/pgsql/data/pg_hba.conf文件将服务器配置为接受远程连接。
以下是一些显示不同用例的示例：
```shell
# TYPE  DATABASE        USER            ADDRESS                 METHOD
 
# The user jane can access all databases from all locations using an md5 password
host    all             jane            0.0.0.0/0                md5
 
# The user jane can access only the janedb database from all locations using an md5 password
host    janedb          jane            0.0.0.0/0                md5
 
# The user jane can access all databases from a trusted location (192.168.1.134) without a password
host    all             jane            192.168.1.134            trust
```

## 五、感谢原本博主
[支持原创，点赞分享](https://blog.csdn.net/weixin_39983404/article/details/110571868)