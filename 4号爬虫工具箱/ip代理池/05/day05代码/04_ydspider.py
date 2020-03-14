import requests
import time
import random
from hashlib import md5

class YdSpider(object):
    def __init__(self):
        # 1.url一定要写F12抓到的POST的地址: Request URL
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            # 2.检查频率最高的三个
            "Cookie": "OUTFOX_SEARCH_USER_ID=584508170@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=415742579.8667161; JSESSIONID=aaa6xixEY8dfdcuUIHo3w; ___rl__test__cookies=1571131223483",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        }
        self.proxies = {
            'http': 'http://309435365:szayclhp@123.56.246.33:16816',
            'https': 'https://309435365:szayclhp@123.56.246.33:16816'
        }

    # 获取ts,salt,sign
    def get_ts_salt_sign(self,word):
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0,9))
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts,salt,sign

    def attack(self,word):
        ts,salt,sign = self.get_ts_salt_sign(word)
        # form表单数据
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "5d4cb17cceb9ecd02ece3ed9923d3a7a",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # 此处为post请求,一定使用 reqeusts.post()方法
        html = requests.post(
            url=self.url,
            data=data,
            headers=self.headers,
            proxies=self.proxies
        ).json()
        print('翻译结果:',html['translateResult'][0][0]['tgt'])

    def run(self):
        word = input('请输入要翻译的单词:')
        self.attack(word)

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()














