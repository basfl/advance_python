import socket

HOST = '127.0.0.1'  
PORT = 8000 

def client():

    with socket.socket() as s:
        s.connect((HOST, PORT))
        #while True:
        s.send(bytes('Hello server','utf-8'))
        data = s.recv(1024).decode()
    print('Received :', repr(data))


if __name__=="__main__":
    client()