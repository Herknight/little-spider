import requests

class RenrenLogin(object):
    def __init__(self):
        self.post_url = 'http://www.renren.com/PLogin.do'
        self.get_url = 'http://www.renren.com/969255813/profile'
        # 实例化session对象
        self.session = requests.session()

    def parse_html(self):
        # 1.先post
        data = { 'email':'18633615542','password':'zhanshen001' }
        self.session.post(url=self.post_url,data=data)
        # 2.再get
        html = self.session.get(
            url=self.get_url
        ).text
        print(html)

if __name__ == '__main__':
    spider = RenrenLogin()
    spider.parse_html()

























