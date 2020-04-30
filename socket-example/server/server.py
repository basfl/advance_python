import socket

HOST = '127.0.0.1'  
PORT = 8000       
def my_server():
    with socket.socket() as s:
        print("socket has been created")
        s.bind((HOST,PORT))
        s.listen(3)
        print("waiting for client ...")
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024).decode()
            print(f"connected with client at address {addr} message is {data}")
            conn.send(bytes(" you are connected !!!","utf-8"))
            
            conn.close()



if __name__=="__main__":
    my_server()