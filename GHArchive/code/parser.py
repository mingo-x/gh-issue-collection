import json
import requests
import sys

fin = open("./data/2015-01-01-15.json",'r',encoding='utf-8')
fout = open("./data/2015-01-01-15.out",'w',encoding='utf-8')
# actions = set()
db = {}
for line in fin:
	#print(line)
	if line.find("\"type\":\"IssuesEvent\"") != -1:
		data = json.loads(line)
		act = data["payload"]["action"]
		# actions.add(act)
		if act == "opened":
			issue_title = data["payload"]["issue"]["title"]
			issue_body = data["payload"]["issue"]["body"]
			# comments_url = data["payload"]["issue"]["comments_url"]
			# comments = requests.get(comments_url)
			# print(comments,flush=True)
			issue_id = data["payload"]["issue"]["id"]
			db[issue_id] = [issue_title, issue_body]
	elif line.find("\"type\":\"IssueCommentEvent\"") != -1:
		data = json.loads(line)
		# act = data["payload"]["action"]
		# actions.add(act)
		issue_id = data["payload"]["issue"]["id"]
		comment = data["payload"]["comment"]["body"]
		if db.get(issue_id,0) != 0:
			db[issue_id].append(comment)
		# print(comment)
for (k,v) in db.items():
	print("[ISSUE_ID]",k)
	# print("	[TITLE]",v[0].encode("utf8"))
	# print("	[BODY]",v[1].encode("utf8"))
	fout.write("[ISSUE_ID]"+str(k)+"\n")
	fout.write("	[TITLE]"+v[0]+"\n")
	fout.write("	[BODY]"+v[1]+"\n")
	if len(v)>2:
		fout.write("	[COMMENTS]:\n")
		for i in range(2,len(v)):
			fout.write("	["+str(i-1)+"]"+v[i]+"\n")
# for ac in actions:
 	# print(ac)
fin.close()
fout.close()
