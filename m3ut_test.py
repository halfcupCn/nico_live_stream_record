import m3u8

with open('test.m3u8',mode='r') as file:
    text = file.read()

    obj = m3u8.loads(text)

    print(obj.segments.uri)