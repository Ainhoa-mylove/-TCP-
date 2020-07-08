from socket import *
import struct

def go_on(c):
    #利用struct定义数据传输包格式（整形、32位字符串、整形、浮点型）
    st=struct.Struct('i32sii')
    #再E盘创建一个txt文本用于后面的数据输入
    f=open(r'E:\my.txt','a')
    while True:
        data=c.recv(4096)
        #加入无数据输入则跳出循环
        if not data:
            break
        #按定义的格式解析数据
        true_data = st.unpack(data)
        #处理-数据
        info='%d %s %d %f\n'%(true_data[0],
                              true_data[1].decode(),true_data[2],true_data[3])
        f.writelines(info)
        f.close()
        print('写入完成')
    c.close()
    
def main():
    s=socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
    server_addr=('127.0.0.1',8888)
    s.bind(server_addr)
    s.listen(5)
    c, addr = s.accept()
    print('连接客户端为：', addr)
    go_on(c)
    s.close()

if __name__ == '__main__':
    print('waiting for connecting')
    main()
