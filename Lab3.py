lineNumber=0
with open('./Dokaz/setupapi.dev.log') as f:
    lines = f.readlines()
    for line in lines:
        if(line.startswith(">>>  [Device Install (Hardware initiated)")):
            lineCopy=line
            index1=lineCopy.find("#")#prva pojava #
            if(index1!=-1):
                print("\n")
                index2=lineCopy[(index1+1):(len(lineCopy))].find("#")+index1+1
                #print("First string between #")
                index3=lineCopy[(index2+1):(len(lineCopy))].find("#")+index2+1
                vendorProductRevision=lineCopy[index1+1:index2].split("&")
                if(len(vendorProductRevision)==4):
                    vendorID=vendorProductRevision[0]+vendorProductRevision[1]
                    productID=vendorProductRevision[2]
                    revision=vendorProductRevision[3]
                    serialNumber=lineCopy[index2+1:index3]
                    print("Product ID: "+productID)
                    print("Revision: "+revision)
                    print("Vendor ID: "+vendorID)
                    print("Serial number: "+serialNumber)
                    dateLine=lines[lineNumber+1]
                    date=dateLine.replace(">>>  Section start ","")
                    print("Date: "+date)
        lineNumber=lineNumber+1