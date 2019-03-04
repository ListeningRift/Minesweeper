

def record(level,result,score):
	
	with open('text.txt') as f1:
		lines = f1.readlines()
	
	if level == '低':
		if score<int(lines[2]):
			lines[2] = str(score)+'\n'

		lines[4] = str(int(lines[4])+1)+'\n'

		if result == '游戏胜利':
			lines[6] = str(int(lines[6])+1)+'\n'
		
		lines[8] = (int(lines[6])/int(lines[4]))*100

		lines[8] = str(lines[8])+'%'+'\n'
	
	if level == '中':
		if score<int(lines[11]):
			lines[11] = str(score)+'\n'

		lines[13] = str(int(lines[13])+1)+'\n'

		if result == '游戏胜利':
			lines[15] = str(int(lines[15])+1)+'\n'
		
		lines[17] = (int(lines[15])/int(lines[13]))*100

		lines[17] = str(lines[17])+'%'+'\n'

	if level == '高':
		if score<int(lines[20]):
			lines[20] = str(score)+'\n'

		lines[22] = str(int(lines[22])+1)+'\n'

		if result == '游戏胜利':
			lines[24] = str(int(lines[24])+1)+'\n'
		
		lines[26] = (int(lines[24])/int(lines[22]))*100

		lines[26] = str(lines[26])+'%'+'\n'
	
	f2 = open('text.txt','w')
	for i in range(len(lines)):
		f2.write(lines[i])
	f2.close()






if __name__ == '__main__':
	record('低','游戏胜利',10)
