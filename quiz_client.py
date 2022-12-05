import socket
from threading import Thread

nickname = input("Please enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connecting with the server...")

def recieve():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        conn,addr = server.accept()
        conn.send('NICKNAME'.encode('uft-8'))
        nickname = conn.recv(2048).decode('utf-8')
        list_of_clients.append(conn)
        nicknames.append(nickname)
        print(nickname + "connected!")
        new_thread = Thread(target= clientthread, args=(conn, nickname))
        new_thread.start()

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()