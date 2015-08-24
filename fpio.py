import os
# inputfile = "c:\ip.txt"
# inputfile='c:\column.bmp'
# outputfile = 'c:\ip_result.txt'
# outputfile2 = 'c:\ip_result2.txt'

from transfor import *
from ReadFile import *
gFilePath = ''

def getReadStart(filename):
    return 0

def getFileIndex(filename):
    return 1

def convert2filename(ipos, iFileIndex, data):
    if (len(data) == 0):
        return ''
    strPos = Int2Str36(ipos, 2)
    strIndex = Int2Str36(iFileIndex)
    strData = Bin2Hex(data)
    strData = strData.zfill(24)
    result = strPos+strIndex+'-'+ strData[0:4] + '-' + strData[4:8]  + '-' + strData[8:12] + '-' + strData[8:20];
    return result

lstFiles = () 
iFileIndex = 0
def getoldfile():
    if (iFileIndex < len(lstFiles)):
        result = lstFiles[iFileIndex]
        iFileIndex = iFileIndex + 1
        return result
    return ''

def convert2newfile(oldfile, newname):
    (path, name) = os.path.split(oldfile)
    (pr, las) = os.path.splitext(name)
    newfilename = path + '\\' + newname + las
    os.rename(oldfile, newfilename)

def translatefile(filename):
    inputfile = filename
    iReadStart = getReadStart(filename)
    iFileIndex = getFileIndex(filename)
        
    readObj = ReadFile(inputfile)
    iFileSize = readObj.filesize()
    (iPos, data) = readObj.readvalue(iReadStart, 12)
    while(len(data) > 0):
        oldFile = getoldfile()
        if iReadStart == 0:
            newName = convert2filename(iFileSize, 0, filename)
        else:
            newName = convert2filename(iPos, iFileIndex, data)
        while (len(oldFile) == 0):
            sleep(1000)
            oldFile = getoldfile()
        convert2newfile(oldFile, newName)
         

def translatefile2(filename):
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
    gFilePath = path
	for strfile in files:
		print ('%s' % strfile)
		if (os.path.isfile(path + strfile)):
#			(root, extension) = os.path.splitext(strfile)
			translatefile(strfile)

def writefile(path):
    import os
    files = os.listdir(path)
    for strfile in files:
        print ('%s' % strfile)
        if (os.path.isfile(strfile)):
            translatefile(strfile)


import sys
if __name__ == '__main__':
	#if (len(sys.argv)) != 2:
    #		exit(1)
    f_input = 'c:\\tran\\' 
    #sys.argv[1]
    print ('%s' % f_input)
    lstFiles = os.listdir('c:\\itestftptrans')
    travsedir(f_input)


