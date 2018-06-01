from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://www.baidu.com/')
time.sleep(10)

browser.find_element_by_name(r'tj_login').click()


#<a href="https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F&amp;sms=5" name="tj_login" class="lb" onclick="return false;">登录</a>
