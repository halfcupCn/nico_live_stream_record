import m3u8
import re

def main(argv):
    with open('test.m3u8',mode='r') as file:
        text = file.read()

        obj = m3u8.loads(text)

        for url in obj.segments.uri:
            print(re.findall(r'\d+.ts',url)[0])

if __name__ == 'main':
    main(None)