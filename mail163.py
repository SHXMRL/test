from selenium import webdriver
import time,sys
url = 'http://mail.163.com'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)
#----------------------元素定位-----------------------------
browser.find_element_by_id("lbNormal").click()
time.sleep(5)
browser.switch_to.frame('x-URS-iframe')
#sys.exit()
print(223)
time.sleep(3)
browser.find_element_by_name('email').send_keys('xxxxx@163.com')

browser.find_element_by_name('password').send_keys('密码')
time.sleep(3)
browser.find_element_by_id('dologin').click()
time.sleep(3)

#----------------------查看是否登录成功---------------------
# 退出iframe
browser.switch_to_default_content()
#判断登录是否成功
name = browser.find_element_by_id("spnUid").text
print(name)
if name == 'xxxxx@163.com':
    print('登录成功')
else:
    print('登录失败')
com
