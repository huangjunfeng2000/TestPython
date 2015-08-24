import os

class ReadFile(object):
    def __init__(self, strfile):
        self.filename = strfile
        self.fp = open(self.filename, 'rb')
        self.filecount = os.path.getsize(strfile)
        self.iPosition = 0;

    def readvalue(self, iSize):
        data = self.fp.read(iSize)
        self.iPosition += len(data)
        return data

    def readvaluepos(self, iPos, iSize):
        self.fp.seek(iPos)
        return self.readvalue(iSize)

import sys
if __name__== '__main__':
    fFile = 'c:\\mvstats3.txt'
    obj = ReadFile(fFile)
    print '%s' % obj.readvalue(10)
    print '%s' % obj.readvaluepos(100, 10)
