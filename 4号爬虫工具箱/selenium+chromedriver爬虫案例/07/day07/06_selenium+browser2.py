from selenium import webdriver

browser = webdriver.Chrome('E:\学习用\工具\Google\Chrome\Application\chromedriver.exe')
browser.get('http://www.baidu.com/')
# 1.找到搜索框,发送关键字
kw = browser.find_element_by_id('kw')
kw.send_keys('赵丽颖')
# 2.找到百度一下按钮,点击一下
su = browser.find_element_by_id('su')
su.click()





