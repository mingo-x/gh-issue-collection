from pymongo import MongoClient
import pprint
import time
import json

fin = open("./data/repos_0.out","r")
fout = open("./data/issues_0.out","w",encoding='utf-8')

client = MongoClient('mongodb://127.0.0.1:27017/',unicode_decode_error_handler='ignore')
db = client.github

issue_total = 0
start_time = time.time()
for line in fin:
	repo = json.loads(line)
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