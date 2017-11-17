import json
import sys
import os
import time

def annotate():
	dir_name = "/mnt/ds3lab/yanping"
	i = 0
	with open(dir_name+"/data/comments_batch_"+str(i)+".out","r",encoding='utf-8') as fin, open(dir_name+"/data/annotation/"+str(i)+".txt","w",encoding='utf-8') as fout:
		counter = 0
		append = False

		line = fin.readline()

		while counter<1:
			counter += 1
			issue = json.loads(line)
			if 'l' in issue:
				if not append:
					fout.write(line)
					for j in range(issue['comments']):
						line = fin.readline()
						fout.write(line)
				#fout.flush()
				#fout.flush()
				#os.fsync(fout.fileno())
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
				os.fsync(fout.fileno())
				if cont != "":
					#fin.close()
					fout.flush()
					os.fsync(fout.fileno())
					time.sleep(2)
					#fout.close()
					return
			line = fin.readline()
	

if __name__ == "__main__":
	
		annotate()
		#time.sleep(5)
		#fin.close()
		#fout.close()


