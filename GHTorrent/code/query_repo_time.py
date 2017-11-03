from pymongo import MongoClient
import pprint
import time
import json
import sys

dir_name = "/mnt/ds3lab/yanping"
client = MongoClient('mongodb://127.0.0.1:27017/',unicode_decode_error_handler='ignore')
db = client.github
counter = 0
for i in range(27):
	print("file",i)
	fin = open(dir_name+"/data/comments_batch_"+str(i)+".out","r",encoding='utf-8')
	fout = open(dir_name+"/data/issue/issues_"+str(i)+".txt","w",encoding='utf-8')
	line = fin.readline()
	while line:
		counter += 1
		if counter%10000 == 0:
			print(i,counter,flush=True)
		issue = json.loads(line)
		repo = db.repos.find({"name":issue['repo'],"owner":issue['repo_owner']})
		fout.write(line[:-2]+",\"repo_time\":"+repo["created_at"]+"}\n")
		for j in range(issue['comments']):
			line = fin.readline()
			fout.write(line)
		line = fin.readline()
	fin.close()
	fout.close()
