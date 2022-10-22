import socket

#expect size of the msg in bytes
Header=8
#Port Reciving
Port = 5050
#encoding format
Format='utf-8'
Disconnect_message="Disconnect!"
#server adresse to connect to
Server ="192.168.1.104"
Addr=(Server,Port)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(Addr)

def send(msg):
	message=msg.encode(Format)
	msg_leng=len(message)
	send_len = str(msg_leng).encode(Format)
	send_len += b' ' * (Header-len(send_len))
	client.send(send_len)
	client.send(message)
	print(client.recv(msg_leng.decode(Format)))

send("hi mate ")
input()
send(Disconnect_message)