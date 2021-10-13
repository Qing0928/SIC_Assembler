#OBJECTCODE
with open('loc.txt', 'r') as f:
	for line in f.readlines():
		with open('objcode.txt', 'a') as fobj:
			line = line.strip('\n')
			code = line.split()
			code_len = len(code)
			if line.startswith('.'):
				fobj.write(line + '\n')
			elif ('START' or 'END' or  'RESW' or  'RESB') in code:
				fobj.write(line + '\n')