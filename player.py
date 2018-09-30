import requests
import json

url = 'http://live2.nicovideo.jp/api/v1/watch/lv315362855/playerbanner'

headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'nicosid=1537344974.1372684086; _ga=GA1.2.1750854307.1537344981; _gid=GA1.2.691391863.1537492614;',
'Host': 'live2.nicovideo.jp',
'Referer': 'http://live2.nicovideo.jp/watch/lv315362855',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

http_porxy = {
	'http':'127.0.0.1:1080',
	'https':'127.0.0.1:1080'
}

rs = requests.get(url,proxies=http_porxy,headers=headers)

with open('playerbanner.html',mode='w',encoding='utf8') as file:
	file.write(json.dumps(dict(rs.headers)))
	file.write('\n')
	file.write(rs.text)