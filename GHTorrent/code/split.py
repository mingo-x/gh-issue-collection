import json
import sys

dir_name = "/mnt/ds3lab/yanping"
in_idx = "0"
idx = 13
unit = 200000
for i in range(1,len(sys.argv)):
	if sys.argv[i] == "-o":
		idx = int(sys.argv[i+1])
		print("out idx =",idx)
	elif sys.argv[i] == "-d":
		dir_name = sys.argv[i+1]
		print("dir name =",dir_name)
	elif sys.argv[i] == "-i":
		in_idx = sys.argv[i+1]
		print("in idx =",in_idx)
	elif sys.argv[i] == "-u":
		unit = int(sys.argv[i+1])
		print("file unit =",unit)

fin = open(dir_name+"/data/comments_"+in_idx+".out","r")
fout = open(dir_name+"/data/comments_"+str(idx)+".out","a",encoding='utf-8')
line = fin.readline()
counter = 0
while line:
	if counter == unit:
		idx = idx+1
		fout.close()
		fout = open(dir_name+"/data/comments_"+str(idx)+".out","a",encoding='utf-8')
		counter = 0
	counter = counter+1
	if counter%100000 == 0:
		print(idx,counter)
	fout.write(line)
	issue = json.loads(line)
	for i in range(issue['comments']):
		line = fin.readline()
		fout.write(line)
	line = fin.readline()

fin.close()	
fout.close()
