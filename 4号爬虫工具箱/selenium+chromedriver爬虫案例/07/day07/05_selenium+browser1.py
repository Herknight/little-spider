from selenium import webdriver
import time

# 1.创建浏览器对象
browser = webdriver.PhantomJS()
# 2.输入地址
browser.get('http://www.baidu.com/')
html = browser.page_source
code = browser.page_source.find('dddddddd')
print(code)
# 获取截图
browser.save_screenshot('baidu.png')
# 3.关闭浏览器
browser.quit()



















