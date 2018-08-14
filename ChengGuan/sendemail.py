#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time

class Mailer(object):

  def __init__(self,maillist,mailtitle,mailcontent):
    self.mail_list = maillist
    self.mail_title = mailtitle
    self.mail_content = mailcontent
    ##### email服务器配置 #####
    self.mail_host = "smtp.qq.com"
    self.mail_user = "1640464937@qq.com"
    self.mail_pass = "plixxiabopvdfdcc"
    self.mail_postfix = "qq.com"
 
  def sendMail(self):
    now = int(time.time())  #显示为时间戳
    timeArray = time.localtime(now)
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
    msg = MIMEMultipart()
    msg['Subject'] = currentTime+'180城管系统接口测试'
    msg['From'] = me
    msg['To'] = ";".join(self.mail_list)
 
    #puretext = MIMEText('<h1>你好，<br/>'+self.mail_content+'</h1>','html','utf-8')
    puretext = MIMEText(''+self.mail_content)
    msg.attach(puretext)
 
#     # jpg类型的附件
#     jpgpart = MIMEApplication(open('321.jpg', 'rb').read())
#     jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
#     msg.attach(jpgpart)
 
#      首先是xlsx类型的附件
    #xlsxpart = MIMEApplication(open('E:/test/dcms/JiangChengJiShi/test_report/TestRunner.html', 'rb').read())
    xlsxpart = MIMEApplication(open('E:/test/jenkins_dcms/ChengGuan/test_report/TestRunner.html', 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename='TestRunner.html')
    msg.attach(xlsxpart)
 
    # mp3类型的附件
    #mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
    #mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
    #msg.attach(mp3part)
 
    # pdf类型附件
    #part = MIMEApplication(open('foo.pdf', 'rb').read())
    #part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
    #msg.attach(part)
 
    try:
      s = smtplib.SMTP_SSL() #创建邮件服务器对象
      s.connect(self.mail_host) #连接到指定的smtp服务器。参数分别表示smpt主机和端口
      s.login(self.mail_user, self.mail_pass) #登录到你邮箱
      s.sendmail(me, self.mail_list, msg.as_string()) #发送内容
      s.close()
      return True
    except Exception:
      print( str)
      return False
 
 
if __name__ == '__main__':
  #send list
  mailto_list = ["1640464937@qq.com"]
  mail_title = '180城管系统测试反馈'
  mail_content = '城管测试报告'
  mm = Mailer(mailto_list,mail_title,mail_content)
  res = mm.sendMail()
  print("发送成功")