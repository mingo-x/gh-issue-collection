import json
import sys

dir_name = "/mnt/ds3lab/yanping"
unit = 100000
for i in range(1,len(sys.argv)):
	if sys.argv[i] == "-d":
		dir_name = sys.argv[i+1]
		print("dir name =",dir_name)
	elif sys.argv[i] == "-u":
		unit = int(sys.argv[i+1])
		print("file unit =",unit)

out_idx = 0
fout = open(dir_name+"/data/comments_batch_"+str(out_idx)+".out","w",encoding='utf-8')
counter = 0
for idx in range(12):
	fin = open(dir_name+"/data/comments_shuffled_"+str(idx)+".out","r")
	line = fin.readline()
	while line:
		if counter == unit:
			out_idx = out_idx+1
			fout.close()
			fout = open(dir_name+"/data/comments_batch_"+str(out_idx)+".out","w",encoding='utf-8')
			counter = 0
		counter = counter+1
		if counter%10000 == 0:
			print(idx,out_idx,counter,flush=true)
		fout.write(line)
		issue = json.loads(line)
		for i in range(issue['comments']):
			line = fin.readline()
			fout.write(line)
		line = fin.readline()
	fin.close()

fout.close()
