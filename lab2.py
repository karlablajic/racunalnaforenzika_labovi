import magic
import glob
import hashlib

#ZADATAK 1#
filenames= glob.glob("Dokaz1/*")

for filename in filenames:
    print(filename, magic.from_file(filename))
    print(filename, magic.from_buffer(open(filename,"rb").read(2048)))

#ZADATAK 2#

filenames= glob.glob("Dokaz2/*")

for filename in filenames:
    with open(filename,'rb') as inputFile:
        data=inputFile.read()
        print('--------------',filename,'-----------------')
        print(hashlib,hashlib.md5(data).hexdigest())
        print(hashlib,hashlib.sha1(data).hexdigest())
        print(hashlib,hashlib.sha256(data).hexdigest())
        

#ZADATAK 3#

filenames= glob.glob("Dokaz3/*")

for filename in filenames:
    with open(filename,'rb') as inputFile:
        data=inputFile.read()
        print('--------------',filename,'-----------------')
        print(hashlib,hashlib.md5(data).hexdigest())
        print(hashlib,hashlib.sha1(data).hexdigest())
        print(hashlib,hashlib.sha256(data).hexdigest())
        

#ZADATAK 4#

filenames= glob.glob("Dokaz4/*")
CHALLENGE="c15e32d27635f248c1c8b66bb012850e5b342119"

for filename in filenames:
    with open(filename,'rb') as inputFile:
        data=inputFile.read()
    
        if hashlib.sha1(data).hexdigest() == CHALLENGE:
            print('Founded target file')
            print('------', filename, '-------')
            print(filename, magic.from_file(filename))
            break
