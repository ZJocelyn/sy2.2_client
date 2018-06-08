# coding:utf8  
'''''创建客户端程序，向服务器传递文件'''

from socket import *        #引入socket模块内的函数，创建一个套接口

HOST = "127.0.0.1"          #指定ip为本机ip地址
PORT = 50000                #指定监听端口为50000
ADDR = (HOST,PORT)          #指定地址，以元组（host,port）的形式表示地址

client = socket(AF_INET,SOCK_STREAM)            #建立服务器之间的网络通信，建立基于TCP的流式套接口（SOCK_STREAM 类型是基于TCP的，有保障的面向连接的socket）
client.connect(ADDR)                   #调用客户端的connect()函数，连接到address(ADDR)处的套接字，如果连接出错，返回socket.error错误

with open("./ww.jpg","wb") as f:         #以二进制写方式打开传输的文件
    while True:
        data = client.recv(1024)     #客户端接收服务器发来的文件数据
        if not data:         #如果没有数据则跳出循环
            break;
        f.write(data)       #向文件中写入数据

f.close()              #关闭文件
print("Finished!")      #显示传输完成
client.close()             #关闭套接字
