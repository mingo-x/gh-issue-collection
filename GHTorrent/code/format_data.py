import json

dir_path = "/mnt/ds3lab/yanping/"

in_idx = 0
path_in = dir_path+"data/annotation/"+str(in_idx)+".txt"
path_pos = dir_path+"data/format_data/pos.txt"
path_neg = dir_path+"data/format_data/neg.txt"
path_oth = dir_path+"data/format_data/other.txt"

with open(path_in,"r") as fin, open(path_pos,"w") as fpos, open(path_neg,"w") as fneg, open(path_oth,"w") as foth:
	while True:
		issue_line = fin.readline()
		issue = json.loads(issue_line)
		if "l" not in issue:
			break

		if issue["l"] == 1:
			fout = fpos
		elif issue["l"] == 0:
			fout = fneg
		else:
			fout = foth

		# title
		fout.write("<b>Title:"+issue["title"]+"</b>\n")
		# time user
		fout.write("<b>time</b>:"+issue["created_at"]+" <b>user</b>:"+issue["owner"]+"\n")
		# post
		print(issue["body"])
		print(json.loads(issue["body"]))
		fout.write("<b>post</b>:"+json.loads(issue["body"])+"\n")

		for i in range(issue["comments"]):
			comment_line = fin.readline()
			comment = json.loads(comment_line)
			# time user
			fout.write("<b>time</b>:"+comment["created_at"]+" <b>user</b>:"+comment["owner"]+"\n")
			# body
			fout.write("<b>comment</b>:"+json.loads(comment["body"])+"\n")