#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: run_bbs_test.py
@time: 2018-4-01 20:56
@subject:创建红网论坛批量执行测试用例以及邮件发送
"""
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib
from HTMLTestRunner import HTMLTestRunner
import unittest
import time, os, sys

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_email(newfile):
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.126.com'
    # 输入Email地址和口令:
    from_addr = 'xxxxx@126.com'
    password = '密码'
    # 输入收件人地址:
    to_addr = 'xxxxx@163.com'
    with open(newfile,"rb") as f:
        mail_body=f.read()
    #定义邮件格式
    msg=MIMEText(mail_body,'html','utf-8')
    msg['From'] = Header('测试人员<%s>'% from_addr, 'utf-8')
    msg['To'] = to_addr
    msg['Subject']=Header('测试报告','utf-8')

    smtp=smtplib.SMTP(smtp_server,25)
    smtp.set_debuglevel(1)
    smtp.helo(smtp_server)
    smtp.ehlo(smtp_server)
    smtp.login(from_addr,password)

    smtp.sendmail(from_addr,to_addr,msg.as_string())
    smtp.quit()
    print('邮件已发送！')

def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(test_dir,lists[-1])
    return file_path

if __name__=="__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename='./bbs/report/'+now+'result.html'
    with open(filename,'wb') as f:
        runner = HTMLTestRunner(stream=f,title='红网论坛自动化测试报告',description='环境：windows10 浏览器：chrome')
        discover=unittest.defaultTestLoader.discover('./bbs/test_case',pattern='*_sta.py')
        runner.run(discover)
    file_path= new_file("./bbs/report/")
    send_email(file_path)
