jenkins其实自带分布式特性，是Master/Slave模型。在Master上分配任务，然后在slave或者Master完成。这个特性带来两个好处：
* 能够有效分担主节点的压力，加速构建速度
* 能够指定特定的任务在特定的主机上进行

# 使用场景
1. 如果项目需要定期集成，同时每次集成都需要较长时间。如果都运行在master服务器上，会消耗过多资源，这时就需要在建立多台设备，并配置为slave机器来为master提供负载服务
2. 需要不同的环境集成。如一个项目，包含Web端，包含Android端，包含IOS端，不同的测试需要的环境都不同，此时可以为每个环境配置一个slave测试。
3. 一个slave是一台为主的jenkins机器建立一个负载build项目的电脑，一旦建立这个分布式任务是完全自动化的。每个slave运行一个单独的程序，不需要再一个slave安装全部的jenkins


Master的职责：
负责调度任务和发送请求
Slave的职责：
多个Salve可以并发的执行并构建任务，或者用于分布式的自动化测试，当自动化测试代码非常多或者而是需要在多个浏览器上并行的时候，可以把测试代码分到不同节点上运行，从而加速自动化测试的运行。

流程：
1. Master——Slave（管理节点，分配任务）
2. Salve(向master注册，反馈状态：空闲/忙碌,反馈任务进度，反馈任务结果)


Jenkins分布式环境搭建步骤如下：
1. master节点上安装和配置jenkins
2. master节点上新增Salve节点配置，生成master-slave通讯文件SlaveAgent
3. Slave节点上运行SlaveAgent，通过SlaveAgent实现和Master节点的通讯
4. Master节点上管理Jenkins项目，指定Salve调度策略，实现Slave节点的任务分配和结果搜集
5. Master节点上安装和配置Jenkins