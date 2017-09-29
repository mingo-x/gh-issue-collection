import json

idx = 1
fin = open("./data/comments_0.out","r")
fout = open("./data/comments_"+str(idx)+".out","w",encoding='utf-8')
line = fin.readline()
counter = 0
while line:
	if counter == 500000:
		idx = idx+1
		fout.close()
		fout = open("./data/comments_"+str(idx)+".out","w",encoding='utf-8')
	counter = counter+1
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
