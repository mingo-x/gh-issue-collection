from pymongo import MongoClient, ASCENDING
import pprint
import time
import json
import sys
import helper

# settings
break_point, start_repo, start_user = helper.breakpoint_set(sys.argv)
out_open_mode = "w"
if break_point:
	out_open_mode = "a"
fin = open("./data/issues_0.out","r")
fout = open("./data/comments_1.out",out_open_mode,encoding='utf-8')

client = MongoClient('mongodb://127.0.0.1:27017/',unicode_decode_error_handler='ignore')
db = client.github

issue_count = 0
start_time = time.time()
line = fin.readline()
while line:
	# read in repo
	repo = json.loads(line)
	issue_num = repo['issues']
	if break_point:
		if repo['name']==start_repo and repo['owner']==start_user:
			break_point = False
		for i in range(0,issue_num):
			issue_line = fin.readline()
		line = fin.readline()
		continue
	
	for i in range(0,issue_num):
		issue_line = fin.readline()
		#print(issue_line,flush=True)
		issue = json.loads(issue_line)
		comments = db.issue_comments.find({"issue_id":issue['number'],"repo":repo['name'],"owner":repo['owner']}).sort('created_at',ASCENDING)
		comment_buffer = []
		users = set()
		for comment in comments:
			users.add(comment['user']['login'])
			comment_buffer.append(comment)
		#print(len(users),flush=True)

		if len(users)<=1:
			continue
		else:
			issue_count = issue_count+1
			if issue_count%10000==0:
				end_time = time.time()
				print("milestone",issue_count,"time",int(end_time-start_time),flush = True)
				start_time = time.time()
			fout.write(line)
			fout.write(issue_line[:len(issue_line)-2]+",\"comments\":"+str(len(comment_buffer))+"}\n")
			for comment in comment_buffer:
				fout.write("{\"body\":"+json.dumps(comment['body'])+",\"owner\":\""+comment['user']['login']+"\",\"created_at\":\""+comment['created_at']+"\"}\n")

	line = fin.readline()

fin.close()
fout.close()
