# 导入所需要的包
from socket import *

# 主程序开始
def main():
    # 设置端口号
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    # 绑定端口
    serverSocket.bind(('10.21.116.236',serverPort))
    # 开始监听
    serverSocket.listen(1)
    # 循环监听
    while True:
        # 打印开始信息
        print('Ready to serve...')
        # 确定接受端口
        connectionSocket, addr = serverSocket.accept()
        try:
            # 进行接收及解码
            sentence = connectionSocket.recv(1024).decode()                         
            # 从url中读取路径 
            path = sentence.split()[1]
            # 判断申请的是文本文件还是媒体文件
            if path[-3:] == 'txt' or path[-4:] == 'html':
                f = open(path[1:])
            else:
                # 如果是媒体文件 需要进行二进制解码
                f = open(path[1:],'rb')
            # 以1024的位数进行传输
            display = f.read()
            # 传输文件头信息
            connectionSocket.send(('HTTP/1.1 200 OK\n').encode())
            connectionSocket.send(('Connection: close\n').encode())
            connectionSocket.send(('Content-Type: text/html/image/audio/video\n').encode())
            connectionSocket.send(('\n').encode())
            # 对内容进行字节流传输
            if path[-3:] == 'txt':
                for i in range(0, len(display)):
                    connectionSocket.send(display[i].encode('GBK'))
            else:
                connectionSocket.send((("""{0}""").format(display)).encode())
            # 打印传输成功信息
            print ('Successfully transfered.')    
            # 关闭接收端口
            connectionSocket.close()
        # 没有找到文件的情况
        except:
            # 发送文件头信息
            connectionSocket.send(('HTTP/1.1 404 Not Found\n').encode())
            connectionSocket.send(('Connection: close\n').encode())
            connectionSocket.send(('Content-Type: html\n').encode())
            connectionSocket.send(('\n').encode())
            # 以html格式传输404内容
            connectionSocket.send(("""<html><body><h1>
                404 Not Found</h1></body></html>""").encode())
            # 关闭接收端口
            connectionSocket.close()
    # 关闭服务器端口
    serverSocket.close()
    pass


if __name__ == '__main__':
    main()
