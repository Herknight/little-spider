from selenium import webdriver
import time
import pymongo

class JdSpider(object):
    def __init__(self):
        self.url = 'https://www.jd.com/'
        self.browser = webdriver.Chrome('E:\学习用\工具\Google\Chrome\Application\chromedriver.exe')
        # 计数
        self.i = 0
        # 3个对象
        self.conn = pymongo.MongoClient(
            '127.0.0.1',27017
        )
        self.db = self.conn['jddb']
        self.myset = self.db['jdset']

    # 输入地址+输入商品+点击按钮
    def get_html(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)

    # 把进度条拉到最底部+提取商品信息
    def get_data(self):
        # 拉动进度条
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        # 给页面元素加载预留时间
        time.sleep(3)

        # 提取数据
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')

        for li in li_list:
            item = {}
            item['name'] = li.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div/div[2]/div[1]/div[3]/a/em').text.strip()
            item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            item['commit'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
            item['shop'] = li.find_element_by_xpath('.//div[@class="p-shop"]').text.strip()
            print(item)
            # 存入mongodb数据库
            self.myset.insert_one(item)
            self.i += 1

    def run(self):
        # 此方法一定只执行一次
        self.get_html()
        while True:
            self.get_data()
            # class: pn-next
            # class: pn-next disabled
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                # 给元素加载预留时间
                time.sleep(1)
            else:
                print('数量:',self.i)
                break

if __name__ == '__main__':
    spider = JdSpider()
    spider.run()





















