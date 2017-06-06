import sys


if sys.argv[1]:
	header = 'p cnf '
	old_header=''
	max_val = 0
	clauses = 0
	f = open(sys.argv[1])
	text = f.read()
	f.seek(0)
	for l in f:
		if l[0]=='p':
			old_header=l[:-1]
			continue
		if l[0]!='p' and l[0]!='c':
			clauses+=1
			st = list(map(int,l.split()))
			for v in st:
				if abs(v)>max_val:
					max_val=abs(v)
	f.close()
	header = header+str(max_val)+' '+str(clauses)
	text= text.replace(old_header, header)
	f = open(sys.argv[1],'w')
	f.write(text)
	f.close()
	print('Fixed')
else:
	print('No input file')
