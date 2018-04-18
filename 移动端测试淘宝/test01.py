from appium import webdriver
from time import sleep
#配置移动端
desired_caps = {}
#平台
desired_caps['platformName'] = 'Android'
#平台版本
desired_caps['platformVersion'] = '23'
#测试终端设备号
desired_caps['deviceName'] = 'LE67A06200259518'
#要测试的app的包名
desired_caps['appPackage'] = 'com.taobao.taobao'
#要测试的app的活动码
desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
#设置输出的内容为unicode编码
desired_caps['unicodeKeyboard']=True
#关闭输入法
desired_caps['resetKeyboard']=True
#连接appium服务端
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print('11111111111111111111111111111111111111')
sleep(3)
#定位操作
#点击搜索
driver.find_element_by_class_name('android.widget.LinearLayout').click()
sleep(6)
##driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
print('2222222222222222222222222222222222222222222')
sleep(3)
#跳转到搜索页面
driver.find_element_by_id("com.taobao.taobao:id/searchEdit")

driver.find_element_by_id("com.taobao.taobao:id/searchEdit").clear()
print('33333333333333333333333333333333333333333333')
search.send_keys("内存条")
sleep(3)
driver.find_element_by_id("com.taobao.taobao:id/searchbtn")
driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()
#driver.find_element_by_accessibility_id("天猫").click()
#driver.quit()
