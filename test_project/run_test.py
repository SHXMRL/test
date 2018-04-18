import unittest
from test_case import test_baidu
from test_case import test_youdao

#构造测试集
suite=unittest.TestSuite()
suite.addTest(test_baidu.BaidutbTest('test_baidu'))
suite.addTest(test_youdao.YoudaoTest('test_youdao'))

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)