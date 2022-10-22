import socket
import threading

Header=8
Port = 5050
Format='utf-8'
Disconnect_message="Disconnect!"
#automatically get the ip adresse of the machine
Server = socket.gethostbyname(socket.gethostname())
Addr=(Server,Port)
#creating a socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#binding the socket to the addresse
server.bind(Addr)

def Handle_Client(conn,addr):
	print(f"[New connection]{addr} connected")
	connected=True
	#blocking until reciving a msg from the client
	while connected:
		msg_length = conn.recv(Header).decode(Format)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(Format)
			print(f"[{addr}]{msg}")
			if msg == Disconnect_message:
				connected = False
			print(f"[{addr}]{msg}")
			conn.send("Message received".encode(Format))

	conn.close()
def start():
	server.listen()
	print(f"[LAUNCHING] server is Listenning on :{Server}")
	while True:
		conn,addr=server.accept()
		thread=threading.Thread(target=Handle_Client,args=(conn,addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS]{threading.activeCount()-1}")

print("[LAUNCHING] server is Launching")
start()