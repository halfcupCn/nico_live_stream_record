# 获取stream对应的host等信息

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
        ws.send(json.dumps(playerversion))
        ws.send(json.dumps(getpermit))
    thread.start_new_thread(run, ())


url = 'http://live2.nicovideo.jp/watch/lv315362855'

http_porxy = {
	'http':'127.0.0.1:1080',
	'https':'127.0.0.1:1080'
}

ws_url = 'wss://a.live2.nicovideo.jp/wsapi/v1/watch/994262910780?audience_token=14117557517983_994262910780_1538031604_72320fd4efa00680f33aeedf846404feabf39bed'

headers={
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'no-cache',
'Connection': 'Upgrade',
'Host': 'msg.live2.nicovideo.jp',
'Origin': 'http://live2.nicovideo.jp',
'Pragma': 'no-cache',
'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
'Sec-WebSocket-Protocol': 'msg.nicovideo.jp#json',
'Sec-WebSocket-Version': '13',
'Upgrade': 'websocket',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

#{"Date": "Wed, 26 Sep 2018 06:22:06 GMT", "Server": "Apache", "Vary": "Accept-Encoding,User-Agent", "Content-Encoding": "gzip", "Content-Length": "19844", "Connection": "close", "Content-Type": "text/html; charset=UTF-8"}

#{"type":"watch","body":{"command":"playerversion","params":["leo"]}}

#{"type":"watch","body":{"command":"getpermit","requirement":{"broadcastId":"994262910780","route":"","stream":{"protocol":"hls","requireNewStream":true,"priorStreamQuality":"abr","isLowLatency":true},"room":{"isCommentable":true,"protocol":"webSocket"}}}}

#wss://a.live2.nicovideo.jp/wsapi/v1/watch/994262910780?audience_token=14117557517983_994262910780_1538031604_72320fd4efa00680f33aeedf846404feabf39bed

playerversion = {"type":"watch","body":{"command":"playerversion","params":["leo"]}}
getpermit = {"type":"watch","body":{"command":"getpermit","requirement":{"broadcastId":"994262910780","route":"","stream":{"protocol":"hls","requireNewStream":True,"priorStreamQuality":"abr","isLowLatency":True},"room":{"isCommentable":True,"protocol":"webSocket"}}}}

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,on_message = on_message,on_error = on_error,on_close = on_close,header=headers)
    ws.on_open = on_open
    ws.run_forever(http_proxy_host='127.0.0.1',http_proxy_port='1080')