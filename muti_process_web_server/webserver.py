# coding=utf-8
import socket
import multiprocessing
import re
import zlib


def server_client(new_socket):
    """与一个浏览器进行交互"""
    web_req = new_socket.recv(1024)
    request = zlib.decompress(web_req ,16+zlib.MAX_WBITS)
    #request = web_req.decode("utf-8")
    print(request)
    web_req_lines = request.splitlines()
    if len(web_req_lines) > 0:
        ret = re.match(r"[^/]+(/[^ ]*)", web_req_lines[0])
        if ret:
            file_name = ret.group(1)
            print(file_name)

    response_body = "<h1>安安 = 猪\r\n我喜欢猪\r\n我喜欢安安</h1>\r\n"
    response_body += "<h1>我喜欢安安</h1>\t"


    response_header = "HTTP/1.1 200 OK\r\n"
    response_header += "Content-length:%d\r\n" % len(response_body)
    response_header += "\r\n"

    response = response_header + response_body
    new_socket.send(zlib.compress(response ,16+zlib.MAX_WBITS))

    new_socket.close()


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定IP 端口
    tcp_server_socket.bind(("", 7788))

    # 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 等待新客户端的链接
        new_socket, client_addr= tcp_server_socket.accept()

        # 为这个客户端服务
        process = multiprocessing.Process(target=server_client, args=(new_socket,))
        process.start()

        new_socket.close()

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
