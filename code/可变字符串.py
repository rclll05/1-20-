import io
s = "rcllllll"
sio = io.StringIO(s)  #sio就是可变字符串
print(sio)
print(sio.getvalue())
sio.seek(3)           #指针到索引3这个位置
sio.write("***")
print(sio.getvalue())
