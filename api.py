import requests
from bs4 import BeautifulSoup
import re
import json

# local proxy
proxy = {
    'http': '127.0.0.1:1080',
    'https': '127.0.0.1:1080'
}

# url to get cookie
cookieUrl = 'http://live2.nicovideo.jp/watch/lv315578370'

# new session
session = requests.Session()

# attach cookie
html = BeautifulSoup(session.get(cookieUrl, proxies=proxy).text,features="html.parser")

# get embedded-data
prop = html.find(id='embedded-data')['data-props']

# all url & param
prop_dict = json.loads(prop)

