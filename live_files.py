import requests

http_porxy = {
	'http':'127.0.0.1:1080',
	'https':'127.0.0.1:1080'
}



query = {
'ht2_nicolive': 'anonymous_user_14057428246504.4rvh5o_pfe71d_219op84ziqze1'
}

headers = {
'Origin': 'http://live2.nicovideo.jp',
'Referer': 'http://live2.nicovideo.jp/watch/lv315362855',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

url = 'https://pa025bcf625.dmc.nico/hlslive/ht2_nicolive/nicolive-hamster-lv315362855_main_5db587e6541c1a74ecb7475fb5b65f7e0ddba88ab51d9824ef648ff740b5a437/2/ts/playlist.m3u8'

rs = requests.get(url,params=query,headers=headers)

print(rs.text)