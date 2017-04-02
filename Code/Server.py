# SERVER Side Program

import socket
def Main():
    host ='127.0.0.1'
    port = 5000

    s= socket.socket()
    s.bind((host,port))

    s.listen(1)                                 # only listen to 1 connection
    c,addr = s.accept()
    print ('Connection from: '+str(addr))

    while True:
        data = c.recv(1024)                      # buffer size
        if not data:
            break
        print ('from connected user:'  +str(data))
        data = bytes(str(data).upper(),'utf-8')
        print('sending: ' +str(data))
        c.send(data)
    c.close()

if __name__=='__main__':
    Main()
