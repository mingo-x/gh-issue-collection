from pymongo import MongoClient
import pprint
import time
from bson.objectid import ObjectId
import sys

skip_num = 0 #2583280 for repo5, 2404314 for repo4, 2120741 for repo3, 1877449 for repo2, 367376 for repo1, 0 for repo0
out_index = "x"
if len(sys.argv)<5:
	print("please specify the number of records to skip by \"-s xxx\" and the out file index by \"-i xxx\"")
	exit()
for i in range(1,len(sys.argv),2):
	if sys.argv[i] == '-s':
		skip_num = int(sys.argv[i+1])
	elif sys.argv[i] == '-i':
		out_index = sys.argv[i+1]

fout = open("./data/repos_"+out_index+".out",'w')
client = MongoClient('mongodb://127.0.0.1:27017/',unicode_decode_error_handler='ignore')
db = client.github
#print("test ",db.issues.count())
#print("total repos "+str(db.repos.count())) 
#64631770
c = 0
startTime = time.time()
for repo in db.repos.find().skip(skip_num):
	# pprint.pprint(repo)
	fout.write("{\"created_at\":\""+repo['created_at']+"\",\"name\":\""+repo['name']+"\",\"owner\":\""+repo['owner']['login']+"\"}\n")
	c = c+1
	#pprint.pprint(repo['name'])
	if c%10000==0:
		endTime = time.time()
		print("milestone "+str(c)+" time "+str(int(endTime-startTime))+"s",flush=True)
		startTime = time.time()
fout.close()
