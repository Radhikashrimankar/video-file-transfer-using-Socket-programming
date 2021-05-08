import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',5620))
sock.listen(2)

print('server Listening....')
while 1:
    conn,addr = sock.accept()
    print ('connection received from :: ',addr)
    f = open('v123.mp4','rb')
    print ('--INITIATING VIDEO TRANSFER---')
    l = f.read(1000)
    size = 0
    while l:
        size = size + len(l)
        print ('sent ',float(size/1024),'Bytes')
        conn.send(l)
        l = f.read(1000)
    print ('--- VIDEO SENT SUCCESSFULLY---')
    f.close()
    conn.close()
    break
sock.close()
