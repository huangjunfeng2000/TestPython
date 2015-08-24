import os
def Bin2Hex(bindata):
    result =''
    for cval in bindata:
        strval=hex(ord(cval))
        strval=strval[2:]
        strval.zfill(2)
        result = result + strval
    return result

def Hex2Bin(hexdata):
    result = ''
    bFirst = True
    iResult = 0
    for cval in hexdata:
        if bFirst:
            iResult = int(cval, 16) * 16
            bFirst = False
        else:
            iResult += int(cval, 16)
            result += chr(iResult)
            bFirst = True
        result.zfill(18)
    return result

import struct

def Int2Str36(n):
    loop = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = []
    while n != 0:
        a.append( loop[n % 36] )
        n = n / 36
    a.reverse()
    out = ''.join(a)  # out:'hzqhoyh9'
    out = out.zfill(6)
    return out

def Int2Str(iVal):
#    return struct.pack('i', iVal)
    return hex(iVal);

def Str2Int(strVal):
#    return struct.unpack('i', strVal)
    return int(strVal, 36);

if __name__ == '__main__':
    data = 'aAbB'
    hexv = Bin2Hex(data)
    binv = Hex2Bin(hexv)
    print ('Hex2Bin: %s : %s' % (data, hexv))
    print ('Bin2Hex: %s : %s' % (hexv, binv))
    iVal = 1024
    strVal = Int2Str36(iVal)
    iVal2 = Str2Int(strVal)
    print ('Int2Str: %s : %s' % (iVal, strVal))
    print ('Str2Int: %s : %s' % (strVal, iVal2))

