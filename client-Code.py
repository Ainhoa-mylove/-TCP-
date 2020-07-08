from socket import *
import struct

s=socket(AF_INET,SOCK_STREAM)
server_addr = ('127.0.0.1', 8888)
s.connect(server_addr)
st=struct.Struct('i8sii')
num=int(input("请输入年龄："))
name=input("请输入姓名：")
math=int(input("请输入数学分数："))
chinese=float(input("请输入语文分数："))
data=st.pack(num,b'name',math,chinese)
s.send(data)
print('数据已经发送')
s.close()
