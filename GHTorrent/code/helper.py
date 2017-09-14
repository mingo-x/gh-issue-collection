def breakpoint_set(args):
	break_point = False
	start_repo = ""
	start_user = ""
	if len(args)<3:
		print("please specify whether starts from breakpoint by \"-b x\" (x: 0 for no, 1 for yes)")
		exit()
	for i in range(1,len(args),2):
		if args[i] == '-b':
			if args[i+1] == '1':
				break_point = True
			break

	if break_point and len(args)<7:
		print("please specify starting repo by \"-r reponame -u username\"")
		exit()

	if break_point:
		for i in range(1,len(args),2):
			if args[i] == '-r':
				start_repo = args[i+1]
			elif args[i] == '-u':
				start_user = args[i+1]

	return break_point, start_repo, start_user
