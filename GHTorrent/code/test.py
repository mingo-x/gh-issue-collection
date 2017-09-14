from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId
import json

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.github

# fin = open("./data/repos.out",'r')
# for line in fin:
# 	data = json.loads(line)
# 	_id = data['_id']
# 	pprint.pprint(db.repos.find_one({'_id':ObjectId(_id)})['name'])
# fin.close()

# for repo in db.repos.find({'name':'Childrens-Council'}):
# 	pprint.pprint(repo)
pprint.pprint(db.issues.find_one())
#_id = db.repos.find_one({'name':'gitflow'})['_id']
#print(_id)
#5784f0ac6480fd8caa050d64
#print("test ",db.issues.count())
#print("total repos "+str(db.repos.count())) 


