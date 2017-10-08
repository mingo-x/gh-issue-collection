import json
import random

dir_path = "/mnt/ds3lab/yanping/data/"
fout = [open(dir_path+"comments_shuffled_"+str(out_idx)+".out",'w',encoding='utf-8') for out_idx in range(12)]
#4 to 22
for idx in range(4,23):
	counter = 0
	fin = open(dir_path+"comments_"+str(idx)+".out",'r')
	line = fin.readline()
	while line:
		out_idx = random.randint(0,11)
		counter = counter + 1
		if counter%10000 == 0:
			print(idx,counter,flush=True)
		fout[out_idx].write(line)
		issue = json.loads(line)
		for i in range(issue['comments']):
			line = fin.readline()
			fout[out_idx].write(line)
		line = fin.readline()
	fin.close()

for i in range(12):
	fout[i].close()