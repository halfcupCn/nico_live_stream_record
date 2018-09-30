import requests
from bs4 import BeautifulSoup
import json


import websocket
try:
    import thread
except ImportError:
    import _thread as thread

# local proxy
proxy = {
    'http': '127.0.0.1:1080',
    'https': '127.0.0.1:1080'
}

# url to get cookie
cookieUrl = 'http://live2.nicovideo.jp/watch/lv315240601'

# new session
session = requests.Session()

# attach cookie
html = BeautifulSoup(session.get(
    cookieUrl, proxies=proxy).text, features="html.parser")

# get embedded-data
prop = html.find(id='embedded-data')['data-props']

# all url & param
prop_dict = json.loads(prop)

webSocketUrl = prop_dict['site']['relive']['webSocketUrl']
broadcastId = prop_dict['program']['broadcastId']

playerversion = {"type": "watch", "body": {
    "command": "playerversion", "params": ["leo"]}}
getpermit = {"type": "watch", "body": {"command": "getpermit", "requirement": {"broadcastId": "994262910780", "route": "", "stream": {
    "protocol": "hls", "requireNewStream": True, "priorStreamQuality": "abr", "isLowLatency": True}, "room": {"isCommentable": True, "protocol": "webSocket"}}}}
getpermit['body']['requirement']['broadcastId'] = broadcastId


def pong(ws):
    ws.send(json.dumps({"type":"pong","body":{}})) 


def on_message(ws, message):
    rep = json.loads(message)
    type_method = rep['type']
    body = rep['body']

#    type_switch = {'ping':pong(ws),}

    if type_method == 'ping':
        pong(ws)

#    type_switch[type_method]

    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")
    session.close()


def on_open(ws):
    def run(*args):
        ws.send(json.dumps(playerversion))
        ws.send(json.dumps(getpermit))
    thread.start_new_thread(run, ())


headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'Upgrade',
    'Host': 'msg.live2.nicovideo.jp',
    'Origin': 'http://live2.nicovideo.jp',
    'Pragma': 'no-cache',
    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
    'Sec-WebSocket-Version': '13',
    'Upgrade': 'websocket',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

cookie_str = ';'.join(['%s=%s' % (name, value) for (name, value) in session.cookies.get_dict().items()])

websocket.enableTrace(True)
ws = websocket.WebSocketApp(webSocketUrl, on_message=on_message, on_error=on_error,
                            on_close=on_close, header=headers, cookie=cookie_str)
ws.on_open = on_open
ws.run_forever(http_proxy_host='127.0.0.1', http_proxy_port='1080')