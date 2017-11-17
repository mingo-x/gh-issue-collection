import json
import os
import sys

def annotate(mode,line_start):
	dir_name = "/mnt/ds3lab/yanping"
	i = 0
	with open(dir_name+"/data/comments_batch_"+str(i)+".out","r",encoding='utf-8') as fin, open(dir_name+"/data/annotation/"+str(i)+".txt",mode,encoding='utf-8') as fout:
		counter = 0
		line_count = 0
		append = True
		if mode == "w":
			append = False
		line = fin.readline()

		while line:
			issue = json.loads(line)
			if 'l' in issue or line_count <= line_start:
				if not append:
					fout.write(line)
				for j in range(issue['comments']):
					line = fin.readline()
					if not append:
						fout.write(line)
			else:
				counter += 1
				print("no.",counter)
				print(line)
				issue_line = line
				comments = []
				for j in range(issue['comments']):
					line = fin.readline()
					comments.append(line)
					print(line)
				label = input("label:")
				while label<'0' or label>'9':
					label = input("label 0~9:")
				fout.write(issue_line[:-2]+",\"l\":"+label+"}\n")
				
				for j in range(issue['comments']):
					fout.write(comments[j])
				cont = input("continue?")
				if cont != "":
					fin.close()
					fout.flush()
					os.fsync(fout.fileno())
					fout.close()
					return
			line_count += 1+issue['comments']
			line = fin.readline()
	

if __name__ == "__main__":
		mode = "a"
		line_start = 1158
		for i in range(1,len(sys.argv),2):
			if(sys.argv[i]=="-l"):
				line_start = int(sys.argv[i+1])
		annotate(mode,line_start)


