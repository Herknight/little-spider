import requests
from lxml import etree
import re

class GovSpider(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Cookie':'td_cookie=18446744071602793018; td_cookie=18446744071601712718; _gscu_190942352=711200480urfj316; _gscbrs_190942352=1; td_cookie=18446744071602559600; wzws_cid=7c25b6f33e355504f8779f50aed809a99f6c76ad8aa92c93a43d8c6f1eab82a8deba674257edf01f29378319c08ade1f67e5d099d66adab79554be470a97d993; _gscs_190942352=t71122459w1kg4p19|pv:4'
        }
        self.proxies = {
            'http': 'http://309435365:szayclhp@123.56.246.33:16816',
            'https': 'https://309435365:szayclhp@123.56.246.33:16816'
        }

    # 获取最新链接
    def get_link(self):
        one_html = requests.get(url=self.url,headers=self.headers,proxies=self.proxies).content.decode()

        # xpath提取最新链接
        p = etree.HTML(one_html)
        link_list = p.xpath('//a[@class="artitlelist"]/@href')
        link = link_list[1] if link_list else None
        if link:
            # link为假链接
            link = 'http://www.mca.gov.cn' + link
            # 通过假链接link来提取真链接
            self.get_real_link(link)
        else:
            print('提取链接失败')

    # 提取真实链接
    def get_real_link(self,link):
        html = requests.get(
            url=link,
            proxies=self.proxies,
            headers=self.headers
        ).content.decode()
        # 正则解析提取
        re_bds = 'window.location.href="(.*?)"'
        p = re.compile(re_bds,re.S)
        real_link = p.findall(html)[0]
        # 提取数据
        self.parse_html(real_link)

    # 提取数据
    def parse_html(self,real_link):
        two_html = requests.get(url=real_link,headers=self.headers).text
        p = etree.HTML(two_html)

        # 基准xpath: 节点对象列表
        tr_list = p.xpath('//tr[@height="19"]')
        for tr in tr_list:
            name = tr.xpath('./td[3]/text()')[0].strip()
            code = tr.xpath('./td[2]/text()')[0].strip()
            print(name,code)

    # 入口函数
    def run(self):
        self.get_link()

if __name__ == '__main__':
    spider = GovSpider()
    spider.run()



















