import json

dir_path = "/mnt/ds3lab/yanping/data/"
out_idx = 0
counter = 0
unit = 100000
fout = open(dir_path+"comments_shuffled_"+str(out_idx)+".out",'w',encoding='utf-8')
#4 to 22
for idx in range(4,23):
	fin = open(dir_path+"comments_"+str(idx)+".out",'r')
	line = fin.readline()
	while line:
		if counter == unit:
			out_idx = out_idx+1
			fout.close()
			fout = open(dir_path+"comments_shuffled_"+str(out_idx)+".out",'w',encoding='utf-8')
			counter = 0
		counter = counter+1
		if counter%100000 == 0:
			print(idx,out_idx,counter)
		fout.write(line)
		issue = json.loads(line)
		for i in range(issue['comments']):
			line = fin.readline()
			fout.write(line)
		line = fin.readline()
	fin.close()
fout.close()