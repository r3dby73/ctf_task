import sys

pswd = ''
check = '776a737b7761366d606c6c'

if len(sys.argv) < 2:
	print('Use: 7zip.py "<PASSWORD>"')
	sys.exit()
else:
	pswd = list(sys.argv[1])

for i in range(0, len(pswd) - 1, 2):
	hold = pswd[i]
	pswd[i] = pswd[i+1]
	pswd[i+1] = hold

for i in range(0, len(pswd)):
	pswd[i] = hex(ord(pswd[i]) ^ 24)[2:]

if len(pswd) != len(check) / 2:
	print('~Incorrect password~')
	sys.exit()

for i in range(0, len(check) - 1, 2):
	if check[i:i+2] != pswd[i//2]:
		print('~Incorrect password~')
		sys.exit()

print('~Congrats, correct password~')