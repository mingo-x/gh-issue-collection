from pymongo import MongoClient
import pprint
import time
from bson.objectid import ObjectId

fout = open("./data/repos_2.out",'w')
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.github
#print("test ",db.issues.count())
#print("total repos "+str(db.repos.count())) 
#64631770
c = 0
startTime = time.time()
for repo in db.repos.find().skip(1877447):
	# if str(repo['_id']) <= '5784f0ac6480fd8caa050d64':
	# 	continue
	fout.write("{\"created_at\":\""+repo['created_at']+"\",\"name\":\""+repo['name']+"\",\"owner\":\""+repo['owner']['login']+"\"}\n")
	c = c+1
	#pprint.pprint(repo['name'])
	if c%10000==0:
		endTime = time.time()
		print("milestone "+str(c)+" time "+str(int(endTime-startTime))+"s",flush=True)
		startTime = time.time()
fout.close()
