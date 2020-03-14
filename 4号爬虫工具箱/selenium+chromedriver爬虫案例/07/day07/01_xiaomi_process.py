import requests
from multiprocessing import Process,Lock
# 队列必须使用进程模块中的Queue,支持跨进程通信
# 标准库模块queue中的Queue不支持进程间通信
from multiprocessing import Queue
import time
import csv
import re

class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        self.headers = {'User-Agent':''}
        # 创建url队列,存放所有待爬取的URL地址
        self.q = Queue()
        self.f = open('xiaomi.csv','a')
        self.lock = Lock()
        self.writer = csv.writer(self.f)
        # 计数
        self.i = 1

    # 获取所有类别及code
    def get_all_type(self):
        url = 'http://app.mi.com/'
        html = requests.get(url=url,headers=self.headers).text
        p = re.compile('<a href="/category/(.*?)">(.*?)</a>',re.S)
        # r_list: [(2,'聊天社交'),(),()]
        r_list = p.findall(html)
        for r in r_list:
            # 遍历一个类别,就要把这个类别的所有页put到队列中
            self.url_in(r)

    # 总页数
    def get_total(self,code):
        url = self.url.format(0,code)
        html = requests.get(url=url,headers=self.headers).json()
        count = html['count']
        if count % 30 == 0:
            total = count // 30
        else:
            total = (count // 30) + 1

        return total

    # url入队列
    def url_in(self,r):
        # 获取此类别总页数
        total = self.get_total(r[0])
        for page in range(total):
            url = self.url.format(page,r[0])
            self.q.put(url)

    # 线程事件函数
    def parse_html(self):
        while True:
            if not self.q.empty():
                url = self.q.get()
                html = requests.get(url=url,headers=self.headers).json()
                app_list = []
                for app in html['data']:
                    name = app['displayName']
                    app_list.append((name,))
                    print(name)
                    self.lock.acquire()
                    self.i += 1
                    self.lock.release()

                # 加锁+释放锁
                self.lock.acquire()
                self.writer.writerows(app_list)
                self.lock.release()
                time.sleep(0.1)
            else:
                break

    # 入口函数
    def run(self):
        # url地址入队列
        self.get_all_type()

        t_list = []
        for i in range(5):
            t = Process(target=self.parse_html)
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()

if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.run()
    end = time.time()
    print('数量:',spider.i)
    print('执行时间:%.2f' % (end-start))















