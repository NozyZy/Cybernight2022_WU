with open('ports.txt') as f:
	lines = [l.strip() for l in f.readlines()]
	flag = ""
	for line in lines:
		if 'Destination Port:' in line:
			port = line.split('Destination Port:')[1].split()[0].strip()
			c = chr(int(port))
			flag += c

print(flag)