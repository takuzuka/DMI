#piedod, nezinu ka no servera augspieladet uz github. Pilna versija, kura ari strada ir serveri, x171REB096

import sys
k = open("meta.bin", "rb")
k.seek(0)

s=open("data.bin" , "rb")
m=0

while 1:
	a = k.read(1)
	if not a:
		break
	m+=ord(a)
	s.seek(m)
	b = s.read(1)
	if not b:
		break
	c = k.read(1)
	xor = ord(b) ^ ord(c)
	sys.stdout.write(chr(xor))

k.close()
s.close()
print("")
