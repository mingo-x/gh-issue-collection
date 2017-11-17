import json
import sys
import os

def annotate(fin,fout):
	counter = 0
	append = False
	line = fin.readline()

	while line:
		issue = json.loads(line)
		if 'l' in issue:
			if not append:
				fout.write(line)
				for j in range(issue['comments']):
					line = fin.readline()
					fout.write(line)
			fout.flush()
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
			fout.flush()
			if cont != "":
				#fin.close()
				#fout.flush()
				#os.fsync(fout.fileno())
				#fout.close()
				return
		line = fin.readline()
	

if __name__ == "__main__":
	dir_name = "/mnt/ds3lab/yanping"
	i = 0
	fin = open(dir_name+"/data/comments_batch_"+str(i)+".out","r",encoding='utf-8')
	fout = open(dir_name+"/data/annotation/"+str(i)+".txt","w",encoding='utf-8')
	annotate(fin,fout)
	fout.flush()
	os.fsync(fout.fileno())
	fin.close()
	fout.close()


