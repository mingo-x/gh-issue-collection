import json

def stat():
	dir_name = "/mnt/ds3lab/yanping"
	i = 0
	with open(dir_name+"/data/annotation/"+str(i)+".txt",'r',encoding='utf-8') as fin:
		counter = 0
		line = fin.readline()
		pos_count = 0
		neg_count = 0
		unsure_count = 0
		other_count = 0
		while line:
			issue = json.loads(line)
			if issue['l'] == 0:
				neg_count += 1
			elif issue['l'] == 1:
				pos_count += 1
			elif issue['l'] == 2:
				unsure_count += 1
			else:
				other_count +=1
			counter += 1
			for j in range(issue['comments']):
				line = fin.readline()
			line = fin.readline()
		print("total",counter,"pos",pos_count,"neg",neg_count,"unsure",unsure_count,"other",other_count)
	

if __name__ == "__main__":
		stat()


