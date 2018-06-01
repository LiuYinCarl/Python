#!/usr/bin/env python
from urllib import request, parse
import re
import os

import time
import random
from urllib.error import URLError, HTTPError
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
import smtplib

class Spider:
    def __init__(self, url):
        self.url = url
        self.old_title = r'章一九零 谁的心魔'
        
    #获取html
    def open_url(self):
        wanted_page = self.url
        req = request.Request(wanted_page)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                   '(KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        return html
    
    #检查是否更新
    def update(self):
        html = self.open_url()
        title_pattern = re.compile(r'永夜之王旗飞扬：(.*\r)')
        title = re.findall(title_pattern, html)
        #print(title)
        title = ''.join(title[0])
        title = title.split('\r')[0]
        print(title)
        if(title != self.old_title):
            old_title = title
            #生成邮件发送实例
            new_email = SendEmail(title)
            new_email.send()
        else:
            print(0)
            

class SendEmail:
    def __init__(self, title):
        self.title = title
    def send(self):
        data_1 = ['1427518212@qq.com', 'xxxxxxxxxx', '17368080695@163.com', 'smtp.qq.com'] #写xxx的存放的是邮箱的客户授权码
        from_addr = data_1[0]
        password = data_1[1]
        to_addr = data_1[2]
        smtp_server = data_1[3]

        msg = MIMEMultipart('alternative')
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = r'同志，小说更新了！！！' 
        html = """
        <html> 
          <head></head> 
          <body> 
            <p>同志，最新章节在此：<br> 
               点击链接立即阅读<br> 
               <a href="http://book.zongheng.com/book/342974.html">""" + self.title + """<a><br>
                <hr style="border:1px dashed #000; height:1px">
               <a href ="http://www.bearcarl.top">点击链接加入我们的社区<a><br>
            </p> 
          </body> 
        </html> 
    """
        part1 = MIMEText(html, 'html')
        msg.attach(part1)
        try:
            server = smtplib.SMTP_SSL(smtp_server, 465)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, to_addr, msg.as_string())
            print('success')
        except server.SMTPException as e:
            print("failed")
        finally:
            server.quit()

if __name__ == '__main__':
    update_Spider = Spider(r'http://book.zongheng.com/book/342974.html')
    while(1):
        title = update_Spider.update()
        #每半小时检查一次是否更新
        time.sleep(1800)
        
    
    

