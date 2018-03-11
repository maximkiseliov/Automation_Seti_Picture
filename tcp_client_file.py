import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = str(input('Filename\n-> '))
    if filename != 'q':
        s.send(filename.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        if data[:6] == 'EXISTS':
            filesize = int(data[6:])
            message = str(input("File Exists, " + str(filesize) + " Bytes, download? (Y/N)\n->"))
            if message == 'Y':
                s.send('OK'.encode('utf-8'))
                f = open("received/"+"new_"+filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print("{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done")
                print("Download Complete!")
        else:
            print("File does not Exists!")
    s.close()
        
if __name__ == '__main__':
    Main()
        
