import requests

class ProxyPool(object):
    def __init__(self):
        self.url = 'http://dev.kdlapi.com/api/getproxy/?orderid=967108906914177&num=55&protocol=2&method=2&an_an=1&an_ha=1&sep=1'
        self.headers = {'User-Agent':''}

    def save_proxy(self):
        html = requests.get(url=self.url,headers=self.headers).text
        # ip_list: ['1.1.1.1:8888','']
        ip_list = html.split('\r\n')
        print(ip_list)
        for ip in ip_list:
            # 测试ip,可用的保存到文件
            if self.test_ip(ip):
                # 把ip写入到文件
                with open('ip.txt','a') as f:
                    f.write(ip + '\n')

    # 测试代理ip是否可用
    def test_ip(self,ip):
        proxies = {
            'http':'http://{}'.format(ip),
            'https':'https://{}'.format(ip)
        }
        try:
            res = requests.get(
                url='http://www.baidu.com/',
                proxies=proxies,
                timeout=2
            )
            if res.status_code == 200:
                print(ip,'可用')
                return True
        except Exception as e:
            print(ip,'不可用')
            return False

if __name__ == '__main__':
    spider = ProxyPool()
    spider.save_proxy()

































