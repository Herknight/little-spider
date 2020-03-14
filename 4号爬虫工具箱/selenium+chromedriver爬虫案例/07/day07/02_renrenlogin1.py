# (.*): (.*)
# "$1": "$2",
# //*[@id="operate_area"]/div[1]/ul/li[1]/span
import requests
from lxml import etree

class RenrenLogin(object):
    def __init__(self):
        self.url = 'http://www.renren.com/969255813/profile'
        self.headers = {
            "Cookie": "td_cookie=18446744071755925920; anonymid=k1u1d9w1-74iox1; depovince=GW; _r01_=1; JSESSIONID=abcB2p2gp7PgCepRLxx3w; ick_login=21331dc6-741c-48b0-9bc0-2b108f6537ad; first_login_flag=1; ln_uact=18633615542; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=9c4bdeee-d396-4774-9804-a9ec189e321a%7C2e9beece3ead42fe6a26739d515f14df%7C1571276385847%7C1%7C1571276390161; jebe_key=9c4bdeee-d396-4774-9804-a9ec189e321a%7C2e9beece3ead42fe6a26739d515f14df%7C1571276385847%7C1%7C1571276390164; wp_fold=0; td_cookie=18446744071756139140; jebecookies=ba19300e-2925-4b13-b8af-d21ee45da052|||||; _de=2229A2704041535FC5E7FC3B0F076082; p=db307493030c61b1e1b3b498a780655b3; t=4fe365d1adf8179ea16550ae0b895aab3; societyguester=4fe365d1adf8179ea16550ae0b895aab3; id=969255813; xnsid=28993c4d; ver=7.0; loginfrom=null",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        }

    def parse_html(self):
        html = requests.get(
            url=self.url,
            headers=self.headers
        ).text
        p = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = p.xpath(xpath_bds)

        print(r_list)

if __name__ == '__main__':
    spider = RenrenLogin()
    spider.parse_html()













