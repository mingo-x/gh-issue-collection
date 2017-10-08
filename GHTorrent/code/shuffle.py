import json
import random
import sys

start = 4
end = 22
for i in range(1,len(sys.argv)):
	if sys.argv[i] == "-a":
		start = int(sys.argv[i+1])
		print("start from file",start)
	elif sys.argv[i] == "-b":
		end = int(sys.argv[i+1])
		print("end by file", end)
dir_path = "/mnt/ds3lab/yanping/data/"
fout = [open(dir_path+"comments_shuffled1_"+str(out_idx)+".out",'a',encoding='utf-8') for out_idx in range(12)]
#4 to 22
for idx in range(start,end+1):
	counter = 0
	fin = open(dir_path+"comments_"+str(idx)+".out",'r')
	line = fin.readline()
	while line:
		out_idx = random.randint(0,11)
		counter = counter + 1
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