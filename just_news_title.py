from urllib import request, parse
#import urllib
import re
import os
import time
import random
from urllib.error import URLError, HTTPError


class SpiderJust:
    def __init__(self, url):
        self.url = url
        self.final_link = []
        self.final_name = []

    def open_url(self, link, key = 0):
        if key == 0:
            wanted_page = self.url
        else:
            wanted_page = link
        req = request.Request(wanted_page)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                    '(KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        return html

    #提取标题
    def get_title(self, url):
        title_pattern = re.compile(r'<title>(.*)</title>')
        title = re.findall(title_pattern, url)
        if(len(title) == 0):
            return 0
        else:
            return title[0]

    #拼凑完整链接，获取标题，保存
    def full_url(self,count):
        num = 0
        for i in range(count,99999):
           # time.sleep(random.choice(range(1,4)))
            full_url = 'http://hbd.just.edu.cn/news/times/news10000' +str(i)
            print('当前页面' + str(i))
            #调用open_url()
            html = 'http:/www.bearcarl.top'
            try:
                html = self.open_url(full_url, 1)
            except HTTPError as e:
                print('HTTP错误编码')
                print(e.code)
               # print(e.read().decode('utf-8'))
            #调用get_title()
            title = self.get_title(html)
            if title != 0:
                self.final_name.append(title)
                self.final_link.append(full_url)
                num = num + 1
            #每收集到10个标题存储一次
            if num%100 == 0:
                print('收集到了' + str(num))
                file_store = open('news_title.txt', 'a', encoding = 'utf-8')
                try:
                    n = len(self.final_name)
                    for i  in range(n):
                        file_store.write(self.final_name[i] + '         ' + self.final_link[i] + '\n')
                finally:
                    file_store.close
                    self.final_name = []
                    self.final_link = []
        return num
                    #time.sleep(random.choice(range(20,30)))

if __name__ == '__main__':
    title_spider = SpiderJust('http://hbd.just.edu.cn/news/times/news1000044374.html')
    title_spider.full_url(10000)
    

    
