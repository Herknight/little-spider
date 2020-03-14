'find_element_ 和 find_elements_ 的区别'
from selenium import webdriver
import time

# 1.创建浏览器对象
browser = webdriver.Chrome()
# 2.打开猫眼电影页面
browser.get('https://maoyan.com/board/4')

def get_data():
    # 3.根据xpath找到dd节点对象 (先用find_element_)
    xpath_bds = '//*[@id="app"]/div/div/div[1]/dl/dd'
    # element - 1个节点对象
    dd = browser.find_element_by_xpath(xpath_bds)
    # elements - 列表
    dd_list = browser.find_elements_by_xpath(xpath_bds)
    # 4.获取dd节点的所有文本内容并打印查看 (.text 属性)
    for dd in dd_list:
        item = {}
        info_list = dd.text.split('\n')
        item['number'] = info_list[0]
        item['name'] = info_list[1]
        item['star'] = info_list[2]
        item['time'] = info_list[3]
        item['score'] = info_list[4]
        print(item)

while True:
    get_data()
    try:
        browser.find_element_by_link_text('下一页').click()
        time.sleep(1)

    except Exception as e:
       print('恭喜你!抓取完成')
       browser.quit()
       break

# if __name__=='__main__':
#     get_data()














