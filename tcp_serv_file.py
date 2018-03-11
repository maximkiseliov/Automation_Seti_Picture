import socket
import threading
import os

def RetrFile(name, sock):
    filename = sock.recv(1024).decode('utf-8')
    if os.path.isfile("pictures/"+filename):
        success = "EXISTS" + str(os.path.getsize("pictures/"+filename))
        sock.send(success.encode('utf-8'))
        userResponse = sock.recv(1024).decode('utf-8')
        if userResponse[:2] == 'OK':
            with open("pictures/"+filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)               
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("Err".encode('utf-8'))
    sock.close()
    
def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)
    
    print("Server started")
    while True:
        c, addr = s.accept()
        print("Client connected: " + str(addr))
        t = threading.Thread(target=RetrFile, args=("retrThread", c))
        t.start()
    s.close()
    
if __name__ == '__main__':
    Main()
