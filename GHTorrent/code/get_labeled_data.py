import json

dir_path = "/mnt/ds3lab/yanping/"

in_idx = 0
path_in = "data/annotation/"+str(in_idx)+".txt"
path_pos = "labeled_data/pos.txt"
path_neg = "labeled_data/neg.txt"
path_oth = "labeled_data/other.txt"

with open(path_in,"r"), open(path_pos,"w"), open(path_neg,"w"), open(path_oth,"w") as fin, fpos, fneg, foth:
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

		fout.write(issue_line)
		for i in range(issue["comments"]):
			fout.write(fin.readline())