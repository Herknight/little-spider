import requests

url = 'https://www.xicidaili.com/nn/'
url = 'http://httpbin.org/get'
proxies = {
    'http':'http://309435365:szayclhp@114.215.174.98:16817',
    'https':'https://309435365:szayclhp@180.116.148.128:21661'
}
headers = {'User-Agent':''}
html = requests.get(url=url,proxies=proxies,headers=headers).text
print(html)