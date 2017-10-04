from pymongo import MongoClient, ASCENDING
import pprint
import time
import json
import sys
import helper

# settings
dir_path = "/mnt/ds3lab/yanping/"
idx = "0"
fin = open(dir_path+"data/issues_"+idx+".out","r")
fout = open(dir_path+"data/comments_"+idx+".out",'w',encoding='utf-8')
flog = open(dir_path+"log/comments_"+idx+".out",'w',encoding='utf-8')

client = MongoClient('mongodb://127.0.0.1:27017/',unicode_decode_error_handler='ignore')
db = client.github

issue_count = 0
start_time = time.time()
line = fin.readline()
while line:
	issue = json.loads(line)
	issue_count = issue_count+1
	comments = db.issue_comments.find({"issue_id":issue['number'],"repo":issue['repo'],"owner":issue['repo_owner']}).sort('created_at',ASCENDING)
	comment_buffer = []
	users = set()
	for comment in comments:
		users.add(comment['user']['login'])
		comment_buffer.append(comment)

	if len(users)<=1:
		flog.write(issue_count)
		if issue_count%10000==0:
			end_time = time.time()
			print("milestone",issue_count,"time",int(end_time-start_time),flush = True)
			start_time = time.time()
		continue
	else:
		fout.write(line[:len(line)-2]+",\"comments\":"+str(len(comment_buffer))+"}\n")
		for comment in comment_buffer:
			fout.write("{\"owner\":\""+comment['user']['login']+"\",\"body\":"+json.dumps(comment['body'])+",\"created_at\":\""+comment['created_at']+"\"}\n")
	
	flog.write(issue_count)
	if issue_count%10000==0:
		end_time = time.time()
		print("milestone",issue_count,"time",int(end_time-start_time),flush = True)
		start_time = time.time()
	line = fin.readline()

fin.close()
fout.close()
flog.close()
