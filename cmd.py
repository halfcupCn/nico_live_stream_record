import argparse
import re

# 命令行入口，提供-u和-o参数指定输入和输出

parser = argparse.ArgumentParser(
    description='一个windows下用来录制/下载niconico生放送的简陋工具')
parser.add_argument('-u', help='想下载的视频地址', required=True)
parser.add_argument('-o', help='指定输出文件的路径，默认使用lv号.mp4作为最终文件名', default=None)

args = parser.parse_args()

url = args.u
output_location = args.o or re.search(r'lv[1-9]+', url).group()+".mp4"

print(url, output_location)
