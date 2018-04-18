# -*- coding:utf8 -*-


"""
@author: MJ
@file: sendEmail.py
@time: 2017-10-19 1:12
"""
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def send_email(newfile):
    # 输入Email地址和口令:
    from_addr = 'xxxxx@126.com'
    password = '密码'
    # 输入收件人地址:
    to_addr = 'majie@3gosc.com'
    #多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver=['邮箱账号']
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.126.com'
    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr('淡淡<%s>' % from_addr)
    #msg['From'] = Header('Python爱好者 <%s>' % from_addr,'utf-8')
    msg['To'] = Header(";".join(receiver)).encode()
    #msg['To']=Header('管理员 <%s>' % to_addr,'utf-8')
    msg['Subject'] = Header('自动定时发送测试报告20171019', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('发送带附件邮件', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(newfile, 'r',encoding='utf-8') as f:
        msg_html = MIMEText(f.read(),'html','utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)
        set_payload(f.read())
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    #server.helo(smtp_server)
    #server.ehlo(smtp_server)
    server.login(from_addr, password)
    server.sendmail(from_addr, receiver, msg.as_string())

    server.quit()
