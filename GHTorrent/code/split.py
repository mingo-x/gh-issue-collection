import json
import sys

dir_name = "/mnt/ds3lab/yanping"
in_idx = "0"
idx = 1
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

fin = open(dir_name+"/data/comments_"+in_idx+".out","r")
fout = open(dir_name+"/data/comments_"+str(idx)+".out","a",encoding='utf-8')
line = fin.readline()
counter = 0
while line:
	if counter == 100000:
		idx = idx+1
		fout.close()
		fout = open(dir_name+"/data/comments_"+str(idx)+".out","a",encoding='utf-8')
		counter = 0
	counter = counter+1
	if counter%10000 == 0:
		print(idx,counter)
	fout.write(line)
	issue_line = fin.readline()
	fout.write(issue_line)
	issue = json.loads(issue_line)
	comment_num = issue['comments']
	for j in range(comment_num):
		comment_line = fin.readline()
		fout.write(comment_line)
	line = fin.readline()

fin.close()	
fout.close()
