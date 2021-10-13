instruction_set = {
    "ADD": 0x18, "ADDF": 0x58, "AND": 0x40, "COMP": 0x28, "COMPF": 0x88,
    "DIV": 0x24, "DIVF": 0x64, "J": 0x3C, "JEQ": 0x30, "JGT": 0x34,
    "JLT": 0x38, "JSUB": 0x48, "LDA": 0x00, "LDB": 0x68, "LDCH": 0x50,
    "LDF": 0x70, "LDL": 0x08, "LDS": 0x6C, "LDT": 0x74, "LDX": 0x04,
    "LPS": 0xD0, "MUL": 0x20, "MULF": 0x60, "OR": 0x44, "RD": 0xD8,
    "RSUB": 0x4C, "SSK": 0xEC, "STA": 0x0C, "STB": 0x78, "STCH": 0x54,
    "STF": 0x80, "STI": 0xD4, "STL": 0x14, "STS": 0x7C, "STSW": 0xE8,
    "STT": 0x84, "STX": 0x10, "SUB": 0x1C, "SUBF": 0x5C, "TD": 0xE0,
    "TIX": 0x2C, "WD": 0xDC
}
 
pseudo_list = ["START", "END", "BYTE", "WORD", "RESB", "RESW"]
 
sym_table = {}
 
def is_instuction(code):
 	prase = code.split()
 	for i in prase:
 		if i in pseudo_list:
 			result = False
 			break
 		else:
 			result = True
 	return result
 		
#LOC
loctr = 0
with open('source.txt', 'r') as f:
	for line in f.readlines():
 		with open('loc.txt', 'a') as floc:
 			code = line.split()
 			pseudo_chk = is_instuction(line)
 			if line.startswith('.'):
 				floc.write(line)
 			elif pseudo_chk == True:
 				floc.write("{:X}".format(loctr) + '\t' + line)
 				loctr += 3
 			elif pseudo_chk == False:
 				if  'START' in code:
 					loctr = int(code[2], 16)
 					floc.write('\t' + line)
 				elif  ('END' in code) and ('FIRST' in code):
 					floc.write("{:X}".format(loctr) + '\t' + line)
 				elif 'WORD' in code:
 					floc.write("{:X}".format(loctr) + '\t' + line)
 					loctr += 3
 				elif 'RESW' in code:
 					floc.write("{:X}".format(loctr) + '\t' + line)
 					loctr += int(code[len(code)-1])*3
 				elif 'RESB' in code:
 					floc.write("{:X}".format(loctr) + '\t' + line)
 					loctr += int(code[len(code)-1])
 				elif 'BYTE' in code:
 					floc.write("{:X}".format(loctr) + '\t' + line)
 					loctr_add = code[len(code)-1].split('\'')
 					if loctr_add[0] == 'C':
 						loctr += len(loctr_add[1])
 					elif loctr_add[0] == 'X':
 						loctr += len(loctr_add[1])//2
