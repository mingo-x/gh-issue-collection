from pymongo import MongoClient
import pprint
import time
import json
import sys

break_point = False
start_repo = ""
start_user = ""
if len(sys.argv)<3:
	print("please specify whether starts from breakpoint by \"-b x\" (x: 0 for no, 1 for yes)")
	exit()
for i in range(1,len(sys.argv),2):
	if sys.argv[i] == '-b':
		if sys.argv[i+1] == '1':
			break_point = True;
		break;

if break_point and len(sys.argv)<7:
	print("please specify starting repo by \"-r reponame -u username\"")
	exit()

if break_point:
	for i in range(1,len(sys.argv),2):
		if sys.argv[i] == '-r':
			start_repo = sys.argv[i+1]
		elif sys.argv[i] == '-u':
			start_user = sys.argv[i+1]

fin = open("./data/repos_0.out","r")
fout = open("./data/issues_1.out","w",encoding='utf-8')

client = MongoClient('mongodb://127.0.0.1:27017/',unicode_decode_error_handler='ignore')
db = client.github

issue_total = 0
start_time = time.time()
for line in fin:
	repo = json.loads(line)
	#"name":"1CUnit","owner":"kuntashov"
	if break_point:
		if repo['name']==start_repo and repo['owner']==start_user:
			break_point = False
		continue

	issues =  db.issues.find({'repo':repo['name'], 'owner':repo['owner']})
	if db.issues.find({'repo':repo['name'], 'owner':repo['owner']}).count()==0:
		continue
	
	issue_buffer = []
	issue_count = 0
	for issue in issues:
		if issue['comments'] < 2:
			continue
		else:
			issue_count = issue_count+1
			issue_buffer.append(issue)

	#print(issue_count)
	if issue_count != 0:
		fout.write(line[:len(line)-2]+",\"issues\":"+str(issue_count)+"}\n")
		for issue in issue_buffer:
			issue_total = issue_total + 1
			if issue_total%10000 == 0:
				end_time = time.time()
				print("milestone",issue_total,"time",int(end_time-start_time),flush = True)
				start_time = time.time()
			#print("{\"number\":"+str(issue['number'])+",\"title\":\""+issue['title']+"\",\"body\":\""+issue['body']+"\",\"created_at\":\""+issue['created_at']+"\",\"owner\":\""+issue['user']['login']+"\"}\n")
			fout.write("{\"number\":"+str(issue['number'])+",\"title\":"+json.dumps(issue['title'])+",\"body\":"+json.dumps(issue['body'])+",\"created_at\":\""+issue['created_at']+"\",\"owner\":\""+issue['user']['login']+"\"}\n")

fin.close()
fout.close()