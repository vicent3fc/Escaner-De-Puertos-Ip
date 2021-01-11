import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Ingrese IP")
ip = input()

for puerto in range(0, 1000):
	result = sock.connect_ex((ip, puerto))
	if result == 0:
		print(f"El puerto {puerto} esta abierto")