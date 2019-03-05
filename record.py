
#游戏战绩方面
def record(level,result,process_time):
	
	with open('record.txt') as f1:
		lines = f1.readlines()
	
	if level == '低':
		if process_time<int(lines[2]):
			lines[2] = str(process_time)+'\n'

		lines[4] = str(int(lines[4])+1)+'\n'

		if result == '游戏胜利':
			lines[6] = str(int(lines[6])+1)+'\n'
		
		lines[8] = (int(lines[6])/int(lines[4]))*100

		lines[8] = str(lines[8])+'%'+'\n'
	
	if level == '中':
		if process_time<int(lines[11]):
			lines[11] = str(process_time)+'\n'

		lines[13] = str(int(lines[13])+1)+'\n'

		if result == '游戏胜利':
			lines[15] = str(int(lines[15])+1)+'\n'
		
		lines[17] = (int(lines[15])/int(lines[13]))*100

		lines[17] = str(lines[17])+'%'+'\n'

	if level == '高':
		if process_time<int(lines[20]):
			lines[20] = str(process_time)+'\n'

		lines[22] = str(int(lines[22])+1)+'\n'

		if result == '游戏胜利':
			lines[24] = str(int(lines[24])+1)+'\n'
		
		lines[26] = (int(lines[24])/int(lines[22]))*100

		lines[26] = str(lines[26])+'%'+'\n'
	
	f2 = open('record.txt','w')
	for i in range(len(lines)):
		f2.write(lines[i])
	f2.close()

#记录获取
def get_record(level):
	with open('record.txt','r') as f:
		lines = f.readlines()
	if level == '低':
		return lines[2],lines[4],lines[8]
	elif level == '中':
		return lines[11],lines[15],lines[17]
	elif level == '高':
		return lines[20],lines[24],lines[26]
	






if __name__ == '__main__':
	record('低','游戏胜利',10)
