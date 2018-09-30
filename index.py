import requests
import json

http_porxy = {
	'http':'127.0.0.1:1080',
	'https':'127.0.0.1:1080'
}

url = 'http://live2.nicovideo.jp/watch/lv315362855'

rs = requests.get(url,proxies=http_porxy)

with open('index.html',mode='w',encoding='utf8') as f:
	f.write(json.dumps(dict(rs.headers)))
	f.write('\n')
	f.write(rs.text)