# 安装virtualenv环境

安装之前最好安装pip或者pip3(安装pip1.3以后或者更高),如果没有安装请移步安装pip 同时也可以查看pip官方文档说明
如果已经安装好pip,那么执行命令安装virtualenv环境
```python
[sudo] pip install virtualenv 或者
[sudo] pip3 install virtualenv [sudo]可用可不用
```
Snip20171116_57.png
安装完成检测版本是否安装成功
```python
virtualenv --version创建整个大虚拟环境
```

## 第一步 
cd 到你要创建虚拟环境的目录
创建虚拟环境目录文件夹
```python
virtualenv test_env01(环境名称，文件夹名称)
```
虚拟环境会默认装上Python setuptools, pip, wheel激活虚拟环境
source test_env01/bin/activate(activate路径)
虚拟环境操作：

1. 退出虚拟环境： deactivate
2. 创建虚拟环境： virtualenv --no-site-packages --python=3.6 env #注释： --no-site-packages 不包括系统包 --python=3.6版本 env 虚拟环境名称
3. 激活虚拟环境：source test_env01/bin/activate(activate路径)

安装好大的虚拟环境之后，一般在使用虚拟环境的时候会使用命令行封装工具VirtualEnvWrapper，举个例子，我新建一个子虚拟环境，就是一个文件夹，一般就会安装一次VirtualEnvWrapper

virtualenvwrapper是virtualenv的扩展包，可以更方便的新增、删除、复制、切换虚拟环境。安装 virtualenvwrapper
命令行输入,不需要sudo, 因为虚拟环境不用管理权限
```python
pip3 install virtualenvwrapper // 第一步安装
```
一般在虚拟环境安装不会出现问题，安装如果出现问题，请参考安装问题解决
配置virtualenvwrapper：
```python
export WORKON_HOME='~/.virtualenvs' //子虚拟环境输入路径
source /usr/local/bin/virtualenvwrapper.sh // 执行命令封装包
```
注意在配置完环境变量以后执行一下source ~/.bash_profile命令，不然不生效
```python
source ~/.bash_profile
```
使用virtualenvwrapper创建子虚拟环境

创建子虚拟环境(注意这些操作都是安装virtualenvwrapper之后)的
```bash
mkvirtualenv env01 (环境名)
mkvirtualenv -p python3 py3env01 (python3条件下环境名为py3env01的子虚拟环境)
```
默认创建的文件路径在 之前配置的路径下exportWORKON_HOME='~/.virtualenvs' 子虚拟环境输入路径
查询子虚拟环境列表
```bash
lsvirtualenv -b
```
查看当前环境已经安装的Python安装包
```bash
lssitepackages
```
输出结果
 
切换子虚拟环境文件
```bash
workon env02 （需要切换的目的环境）
```
移除子虚拟环境文件
```bash
rmvirtualenv env01
```

在子虚拟环境中安装Python 的包
比如在env02 环境中安装Pillow
如果没有在env02环境中，就切换到env02的环境中,并执行
```bash
pip install Pillow
```
执行结果
 
退出子虚拟环境，重新进入
```bash
workon env02
```
完全退出整个虚拟环境在重新进入需要激活整个大环境在安装virtualenvwrapper
```bash
source test_env01/bin/activate(activate路径) 激活大环境

重复安装virtualenvwrapper步骤
workon env02 进入环境
其他常用的virtualenvwrapper 命令

退出环境 deactivate
其他命令可以查看virtualenvwrapper --help
```

