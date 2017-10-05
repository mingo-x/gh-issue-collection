from pymongo import MongoClient, ASCENDING
import pprint
import time
import json
import sys
import helper

# settings
dir_path = "/mnt/ds3lab/yanping/"
idx = "0"
skip_num = 0
for i in range(1,len(sys.argv),2):
	if sys.argv[i]=="-i":
		idx = sys.argv[i+1]
		print("idx:",idx)
	elif sys.argv[i]=="-s":
		skip_num = int(sys.argv[i+1])
fin = open(dir_path+"data/issues_"+idx+".out","r")
fout = open(dir_path+"data/comments_"+idx+".out",'a',encoding='utf-8')
flog = open(dir_path+"log/comments_"+idx+".out",'a',encoding='utf-8')

client = MongoClient('mongodb://127.0.0.1:27017/',unicode_decode_error_handler='ignore')
db = client.github

issue_count = 0
start_time = time.time()
for line in fin:
	issue_count = issue_count+1
	if issue_count <= skip_num:
		continue
	issue = json.loads(line)
	comments = db.issue_comments.find({"repo":issue['repo'],"owner":issue['repo_owner'],"issue_id":issue['number']}).sort('created_at',ASCENDING)
	comment_buffer = []
	users = set()
	for comment in comments:
		users.add(comment['user']['login'])
		comment_buffer.append(comment)

	if len(users)<=1:
		flog.write(str(issue_count)+"\n")
		if issue_count%10000==0:
			end_time = time.time()
			print("milestone",issue_count,"time",int(end_time-start_time),flush = True)
			start_time = time.time()
		continue
	else:
		fout.write(line[:len(line)-2]+",\"comments\":"+str(len(comment_buffer))+"}\n")
		for comment in comment_buffer:
			fout.write("{\"owner\":\""+comment['user']['login']+"\",\"body\":"+json.dumps(comment['body'])+",\"created_at\":\""+comment['created_at']+"\"}\n")
	
	fout.flush()
	flog.write(str(issue_count)+"\n")
	flog.flush()
	if issue_count%10000==0:
		end_time = time.time()
		print("milestone",issue_count,"time",int(end_time-start_time),flush = True)
		start_time = time.time()

fin.close()
fout.close()
flog.close()
