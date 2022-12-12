flag = "871 1157 858 1014 1599 1287 507 663 1508 1261 1365 1508 1235 1456 676 1495 1235 637 1235 1287 663 1495 1261 1482 1625"
f = list(map(int,flag.split()))

diff = ord('Y') - ord('C')
di = f[1] - f[0]

d = di / diff
print(d)

for s in f:
	print(chr(int(s//d)), end="")
