# Client PROGRAM

import socket
def Main():
    host ='127.0.0.1'                      # Use the Server adress & port
    port = 5000

    s= socket.socket()
    s.connect((host,port))
    message = bytes(input(' -> '),'utf-8')
    while message !='q':
        s.send(message)
        data =s.recv(1024)
        print('Recieved from server: '+str(data))
        message = bytes(input(),'utf-8')      
    c.close()
