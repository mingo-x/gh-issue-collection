import json
import requests

fin = open("./data/2015-01-01-15.json",'r',encoding='utf-8')
# actions = set()
for line in fin:
	#print(line)
	if line.find("\"type\":\"IssuesEvent\"") != -1:
		data = json.loads(line)
		# act = data["payload"]["action"]
		# actions.add(act)
		if act == "opened":
			issue_title = data["payload"]["issue"]["title"]
			issue_body = data["payload"]["issue"]["body"]
			comments_url = data["payload"]["issue"]["comments_url"]
			comments = requests.get(comments_url)
			print(comments,flush=True)
# for ac in actions:
# 	print(ac)
fin.close()
