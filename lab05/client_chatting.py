# 导入所需要的包
from sys import *
from socket import *
from select import *
# 定义一些初始变量 例如本地IP地址和端口
server_host = '192.168.31.169'
server_port = 3001
# 建立在线用户list和socketlist以及用户昵称list
online_user = []
socket_chart = []
username_chart = []
NICKNAME = ''

# 主程序开端
def client_main():
    # 设置用户名
    username_chart.append(input("Please input your nickname: "))
    global NICKNAME
    NICKNAME = username_chart[0]
    try:
        # 尝试创建端口
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_host, server_port))
        client_socket.send(NICKNAME.encode())
        client_socket.settimeout(30)
        # 接收返回消息
        ack = client_socket.recv(2048).decode()
        # 如果不是否定 则可以成功加入
        if ack != "No":
            socket_chart.append(client_socket)
        # 否则打印错误信息 重新启动程序
        else:
            print("Username already exist.")
            client_main()
            exit()
    # 服务器掉线则打印错误信息并退出
    except:
        print("Server offline")
        exit()
    finally:
        # 加入成功则显示成功信息
        print("Successively joined in chatting room", server_port)
        # 接收用户列表名单
        message = client_socket.recv(2048).decode()
        username_list = message.split('&')
        # 存到online_user的list中
        for temp_u in username_list:
            online_user.append(temp_u)
        stdout.flush()
        # 循环监听
        while 1:
            try:
                # 创建列表
                socket_list = [stdin, client_socket]
                # 利用select方法选择list并实现多线程
                read_sockets, write_sockets, error_sockets = select(socket_list, [], [])
                for temp_socket in read_sockets:
                    # 对于列表里的端口们 如果发送了消息 就要接收
                    if temp_socket == client_socket:
                        message = temp_socket.recv(2048).decode()
                        # 解码后打印出来
                        print(message)
                        # 换行
                        stdout.flush()
                    else:
                        # 否则则判定为在输入 读取屏幕输入信息
                        message = stdin.readline()
                        # 发送到服务器端口
                        client_socket.send(message.encode())
                        # 打印自己输入的信息
                        stdout.write(NICKNAME + ":" + message)
            except:
                exit()

if __name__ == "__main__":
    client_main()
