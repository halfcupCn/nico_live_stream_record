# 用来获取指定 lvID 的弹幕

import websocket
import json
try:
    import thread
except ImportError:
    import _thread as thread

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(json.dumps(msg))
    thread.start_new_thread(run, ())


url = 'http://live2.nicovideo.jp/watch/lv315362855'

http_porxy = {
	'http':'127.0.0.1:1080',
	'https':'127.0.0.1:1080'
}

ws_url = 'wss://msg.live2.nicovideo.jp/o10685/websocket'

headers={
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'no-cache',
'Connection': 'Upgrade',
'Cookie': 'nicosid=1537344974.1372684086; _ga=GA1.2.1750854307.1537344981; _gid=GA1.2.691391863.1537492614; audience_token=14057428246504_a4c5e220eeaeabd41b6d02ca05967501b817c9ae; nicolivehistory=%5B315362855%5D',
'Host': 'msg.live2.nicovideo.jp',
'Origin': 'http://live2.nicovideo.jp',
'Pragma': 'no-cache',
'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
'Sec-WebSocket-Protocol': 'msg.nicovideo.jp#json',
'Sec-WebSocket-Version': '13',
'Upgrade': 'websocket',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

#ws = create_connection(ws_url,http_proxy_host='127.0.0.1',http_proxy_port='1080',header=headers)

msg = [{"ping":{"content":"rs:0"}},{"ping":{"content":"ps:0"}},{"thread":{"thread":"1630688866","version":"20061206","fork":0,"user_id":"NaN","res_from":-1000,"with_global":1,"scores":1,"nicoru":0}},{"ping":{"content":"pf:0"}},{"ping":{"content":"rf:0"}}]

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,on_message = on_message,on_error = on_error,on_close = on_close,header=headers)
    ws.on_open = on_open
    ws.run_forever(http_proxy_host='127.0.0.1',http_proxy_port='1080')