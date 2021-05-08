import socket
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
r = input('Enter the IP addr of server :: ')
r = str(r)
sock.connect((r,5620))

while 1:
    cd = os.getcwd()
    try :
        os.chdir(cd+'/CNASSAIGNMENT')
    except OSError:
        os.mkdir('CNASSAIGNMENT')
        os.chdir(cd+'/CNASSAIGNMENT')
    f = open('vid.mp4','wb')
    print ('PREPARING TO RECEIVE VIDEO...')
    l = sock.recv(1024)
    size = 0
    while l :
        size = size + len(l)
        print ('Received ',size,'Bytes')
        f.write(l)
        l = sock.recv(1024)

    print ('VIDEO RECEIVED SUCCESSFULLY...')
    f.close()
    os.chdir(cd)
    break
sock.close()
