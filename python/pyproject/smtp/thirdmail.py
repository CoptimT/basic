#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018年5月4日
使用其他邮件服务商的 SMTP 访问
@author: zhangxw17
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == '__main__':
    # 第三方 SMTP 服务
    mail_host="smtp.163.com"  #设置服务器
    mail_user="zxw@163.com"    #用户名
    mail_pass=""   #口令 

    sender = 'zxw@163.com'
    receivers = ['zxw@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')   # 发送者
    message['To'] =  Header("测试", 'utf-8')        # 接收者
    
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException as e:
        print "Error: 无法发送邮件"
        raise e
        