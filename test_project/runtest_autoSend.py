# -*- coding:utf8 -*-
"""
@author: MJ
@file: runtest_autoSend.py
@time: 2017-10-19 0:12
Project:整合自动发邮件功能，执行测试用例生成最新测试报告，取最新的测试报告，发送最新测试报告
问题，
"""
import unittest
from HTMLTestRunner import HTMLTestRunner
import time,os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
#2.定义：取最新测试报告
def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(test_dir,lists[-1])
    return file_path

#3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    # 输入Email地址和口令:
    from_addr = '1454504@qq.com'
    password='afiuqnfsflnibiha'
    #password = 'afiuqnfsflnibiha'
    # 输入收件人地址:
    #多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver=['benq81@vip.qq.com','majie@3gosc.com']
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'
    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr("张磊<%s>" % from_addr)
    #msg['From'] = Header('Python爱好者 <%s>' % from_addr,'utf-8')
    msg['To'] = Header(";".join(receiver)).encode()
    #msg['To'] = Header(";".join(receiver)).encode()
    #msg['To']=Header('管理员 <%s>' % to_addr,'utf-8')
    msg['Subject'] = Header('自动定时发送报告-'+time.strftime('%Y-%m-%d_%H_%M_%S'), 'utf-8').encode()
    # 邮件正文是MIMEText:
    msg.attach(MIMEText('最新内容报告', 'plain', 'utf-8'))
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(newfile, 'r',encoding='utf-8') as f:
        msg_html = MIMEText(f.read(),'html','utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.helo(smtp_server)
    server.ehlo(smtp_server)
    server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, receiver, msg.as_string())

    server.quit()

if __name__=='__main__':
    print('=====测试开始======')
    #1.执行测试用例，生成最新的测试用例
    case_path = os.path.join(os.getcwd(), "test_case")
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), "report")
    discover=unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')
    now=time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = report_path+'\\'+ now + 'result.html'
    fp=open(filename ,'w',encoding="utf8")

    runner = HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
    runner.run(discover)
    fp.close()

    #2.取最新测试报告
    new_report=new_file(report_path)
#调试用的
#    print new_report

    #3.发送邮件，发送最新测试报告html
    send_email(new_report)
    print('=====AutoTest Over======')