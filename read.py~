import os
inputfile = "c:\ip.txt"
inputfile='c:\column.bmp'
outputfile = 'c:\ip_result.txt'
outputfile2 = 'c:\ip_result2.txt'
def translatefile(filename):
	inputfile=filename
	outputfile=filename+".result"
	infile = open(inputfile, 'rb')
	outfile = open(outputfile, 'w')
	#outfile2 = open(outputfile2, 'w')
	fcount = os.path.getsize(inputfile)
	contype = 2
	while fcount > 0:
		if fcount<1024:
			data=infile.read(fcount)
			fcount -= fcount
		else:
			data=infile.read(1024)
			fcount-=1024
		#outfile.write(data)
		for cval in data:
			if contype == 1:
				strval=bin(ord(cval))
				strval=strval[2:]
				strval.zfill(8)
				strval2=int(strval, 2)
				strval2=chr(strval2)		
			else:
				strval=hex(ord(cval))
				strval=strval[2:]
				strval.zfill(2)
				strval2=int(strval, 16)
				strval2=chr(strval2)
			outfile.write(strval)
			#outfile2.write(strval2)
	infile.close()
	outfile.close()
	#outfile2.close()

def travsedir(path):
	import os
	files=os.listdir(path)
	for strfile in files:
		print strfile
		if (os.path.isfile(strfile)):
			root, extension = os.path.splitext(strfile)
			if (extension != ".result"):
				translatefile(strfile)


import sys
if __name__ == '__main__':
	if (len(sys.argv)) != 2:
		print 'Input filepath'
		exit(1)
	f_input = sys.argv[1]
	print f_input
	travsedir(f_input)


