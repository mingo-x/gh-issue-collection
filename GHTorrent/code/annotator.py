from pymongo import MongoClient
import json

dir_name = "/mnt/ds3lab/yanping"
counter = 0
i = 0
append = False
fin = open(dir_name+"/data/comments_batch_"+str(i)+".out","r",encoding='utf-8')
fout = open(dir_name+"/data/annotation/"+str(i)+".txt","w",encoding='utf-8')
line = fin.readline()
while line:
	issue = json.loads(line)
	if 'l' in issue:
		if not append:
			fout.write(line)
			for j in range(issue['comments']):
				line = fin.readline()
				fout.write(line)
	else:
		counter += 1
		print("no.",counter)
		print(line)
		comments = []
		for j in range(issue['comments']):
			line = fin.readline()
			comments += line
			print(line)
		label = input("label:")
		while label<'0' or label>'9':
			label = input("label 0~9:")
		fout.write(line[:-2]+",\"l\":"+label+"}\n")
		for j in range(issue['comments']):
			fout.write(comments[j])
		cont = input("continue?")
		if cont != "":
			fin.close()
			fout.close()
			exit()
	line = fin.readline()
fin.close()
fout.close()
