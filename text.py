with open('text.txt') as f1:
		lines = f1.readlines()
lines[4] = str(int(lines[4])+1)+'\n'
print(lines)
f2 = open('text.txt','w')
for i in range(len(lines)):
	f2.write(lines[i])

