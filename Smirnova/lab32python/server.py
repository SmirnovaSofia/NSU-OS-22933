import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    y = str(input())
    b = bytes(y, 'utf-8')
    conn.send(b)

conn.close()