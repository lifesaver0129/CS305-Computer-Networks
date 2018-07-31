# 导入所需要的各种包
from sys import *
from socket import *
from select import *
from time import *
# 设置节点地址和端口地址
server_host = '192.168.31.169'
server_port = 3001
# 创建初始端口表 以字典结构储存
socket_list = {}

# 主程序开端
def server_main():
    # 设置初始服务器节点数据
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定服务器节点到指定端口地址
    server_socket.bind((server_host, server_port))
    server_socket.listen(10)
    # 加入第一个端口 本地管理员端口
    socket_list['Admin'] = server_socket
    # 打印聊天室通知
    print("Chatting room " + str(server_port) + " has just created.")
    # 换行
    stdout.flush()
    # 持续接听
    while 1:
        try:
            # 创建一个端口列表表格准备传入到客户端
            socket_chart = [stdin]
            # 对于目前连接的所有端口进行导入操作 只存储端口名
            for temp_username, temp_socket in socket_list.items():
                socket_chart.append(temp_socket)
            # 利用select方法实现不同列表的调用
            ready_to_read, ready_to_write, in_error = select(socket_chart, [], [], 0)
            # 对于已经在列表内的端口
            for temp_socket in ready_to_read:
                # 情况1 有新端口加入
                if temp_socket == server_socket:
                    # 调用登陆方法
                    online(server_socket)
                # 情况2 系统进行广播或者发送聊天内容
                elif temp_socket == stdin:
                    # 读取键盘输入信息
                    message = stdin.readline().rstrip()
                    # 调用管理员广播
                    broadcast(server_socket, server_socket, "Admin: " + message)
                # 情况3 接受客户端发来的信息
                else:
                    # 调用接收方法
                    receive(server_socket, temp_socket)
        except:
            pass

# 接收方法
def receive(server_socket, client_socket):
    try:
        # 读取客户端发来的消息
        message = client_socket.recv(2048).decode()
        # 寻找客户端口对应的用户名
        temp_username = ''
        # 进行for循环 寻找用户名
        for temp_u, temp_sock in socket_list.items():
            # 如果找到相对应的端口号 就把用户名取出
            if client_socket == temp_sock:
                temp_username = temp_u
        # 如果接收到message
        if message:
            # 整理message到一个可以广播的形式
            message = temp_username + ": " + message.rstrip()
            # 进行全体广播
            broadcast(server_socket, client_socket, message)
        else:
            # 如果没有找到对应信息 说明用户已经下线 调用下线方法
            offline(temp_username)
    except:
        pass

# 发送广播方法
def broadcast(server_socket, client_socket, message):
    # 对于在列表中的每一个端口
    for username, tem_socket in socket_list.items():
        # 如果是发送方或者管理员方就跳过
        if tem_socket != server_socket and tem_socket != client_socket:
            try:
                # 不是的话就进行发送
                tem_socket.send(message.encode())
            except:
                # 出现异常说明client已经下线 进行关闭端口及下线方法
                tem_socket.close()
                offline(username)
    # 打印信息 这是针对服务器自己的现实
    print(message)
    # 换行
    stdout.flush()

# 上线方法
def online(server_socket):
    # 进行新建socket操作
    client_socket, client_addr = server_socket.accept()
    # 提取用户名
    temp_username = client_socket.recv(2048).decode().rstrip()
    client_socket.settimeout(30)
    # 如果用户名没有在用户名列表里的话
    if temp_username not in socket_list and temp_username.strip() != "":
        # 创建新的对应关系
        socket_list[temp_username] = client_socket
        # 创建完毕 发送OK
        client_socket.send("OK".encode())
        # 对于新加入的用户 向其发送现在在线的用户消息
        all_users = ''
        for user, temp_socket in socket_list.items():
            all_users += "&" + user
        client_socket.send(all_users.encode())
        # 进行新用户上线广播方法构造
        message = "[" + temp_username + " online]"
        # 进行新用户上线广播
        broadcast(socket_list['Admin'], socket_list['Admin'], message)
        sleep(1)
        # 向所有用户发送现在在线的用户
        broadcast(socket_list['Admin'], socket_list['Admin'], username_list())

# 下线方法
def offline(username):
    # 关闭对应接收端口
    socket_list[username].close()
    # 在字典类删除对应用户
    del socket_list[username]
    # 构建下线信息
    message = "[" + username + " offline]"
    # 广播用户下线消息
    broadcast(socket_list['Admin'], socket_list['Admin'], message)
    sleep(1)
    # 向所有用户发送现在在线的用户
    broadcast(socket_list['Admin'], socket_list['Admin'], username_list())

# 在线用户方法
def username_list():
    # 构建在线用户方法信息
    message = "Online users: "
    # 从端口字典类中调用所有的用户名
    for temp_user, temp_socket in socket_list.items():
        message += temp_user + ","
    message = message[:-1]
    # 返回构造的信息
    return message


if __name__ == "__main__":
    server_main()
