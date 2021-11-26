# run_test.py，与test_register.py、register.py同一目录下
import unittest
import test_register
from HTMLTestRuner import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 通过模块加载测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))

# 创建测试运行程序启动器
runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个报告文件，将句柄传给stream
                        tester="miki",                    # 报告中显示的测试人员
                        description="注册接口测试报告",        # 报告中显示的描述信息
                        title="自动化测试报告",verbosity=2)                 # 报告的标题

# 使用启动器去执行测试套件里的用例
runner.run(suite)