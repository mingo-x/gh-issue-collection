from pymongo import MongoClient
import pprint
import time
import json
import sys
import helper

dir_path = "/mnt/ds3lab/yanping/"
# settings
out_index = 'x'
skip_num = 0
for i in  range(1,len(sys.argv),2):
	if sys.argv[i] == '-i':
		out_index = sys.argv[i+1]
	elif sys.argv[i] == '-s':
		skip_num = int(sys.argv[i+1])

fout = open(dir_path+"data/issues_"+out_index+".out",'w',encoding='utf-8')
flog = open(dir_path+"log/issues_"+out_index+".out",'w',encoding='utf-8')

client = MongoClient('mongodb://127.0.0.1:27017/',unicode_decode_error_handler='ignore')
db = client.github

issue_total = 0
start_time = time.time()
for issue in db.issues.find().skip(skip_num):
	if issue['comments'] < 2:
		issue_total = issue_total+1
		if issue_total%100000 == 0:
			end_time = time.time()
			flog.write("milestone: "+str(issue_total)+" time: "+str(int(end_time-start_time))+"\n")
			start_time = time.time()
		print(issue_total)
		continue
	fout.write("{\"created_at\":\""+issue['created_at']+"\",\"owner\":\""+issue['user']['login']+"\",\"title\":"+json.dumps(issue['title'])+",\"body\":"+json.dumps(issue['body'])+",\"repo_owner\":\""+issue['owner']+"\",\"repo\":\""+issue['repo']+"\",\"number\":"+str(issue['number'])+"}\n")
	issue_total = issue_total+1
	if issue_total%100000 == 0:
		end_time = time.time()
		flog.write("milestone: "+str(issue_total)+" time: "+str(int(end_time-start_time))+"\n")
		start_time = time.time()
	print(issue_total)
fout.close()
flog.close()
