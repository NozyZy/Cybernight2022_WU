from pwn import *
conn = remote('10.242.0.1', 10002)
while True:
	data = conn.recvline().decode('utf-8').strip()
	print("!!!!!!! " + data)
	if data and 'Répète après moi :' not in data and 'Bravo ! Plus vite maintenant' not in data:
		print(data)
		conn.send(f'{data}\n'.encode())
conn.close()