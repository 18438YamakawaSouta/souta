import socket

#.AF = IPv4 という意味
#TCP/IP の場合は、  SOCK_STREAQM を使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #IPアドレスとポートを指定
    s.bind(('0.0.0.0', 50007))
    #１接続!
    s.listen(1)
    #connection するまで待つ
    while True:
        #誰かがアクセスしてきたら、コネクションとアドレスをいれる
        conn, addr = s.accept()
        with conn:
            while True:
                #データを受け取る
                data = conn.recv(1024)
                if not data:
                    break
                print('data :{}, addr: {}'.format(data, addr))
                #クライアントにデータを返す（b.-> byte でないといけない
                conn.sendall(b'Received: ' + data)