import json

dir_name = "/mnt/ds3lab/yanping"
idx = 1
fin = open(dir_name+"/data/comments_0.out","r")
fout = open(dir_name+"/data/comments_"+str(idx)+".out","w",encoding='utf-8')
line = fin.readline()
counter = 0
while line:
	if counter == 100000:
		idx = idx+1
		fout.close()
		fout = open(dir_name+"/data/comments_"+str(idx)+".out","w",encoding='utf-8')
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
