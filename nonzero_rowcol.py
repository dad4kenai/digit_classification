import pandas as pd
import sys

def countRowBelow(image,row,thresh):
    count = 0
    for i in range(row*28,row*28+28):
        if image[i] <= thresh:
            count += 1
    return count

def countColBelow(image,col,thresh):
    count = 0
    for i in range(col,col+28*28,28):
        if image[i] <= thresh:
            count += 1
    return count

def countZeroRows(image,thresh):
    count = 0
    for i in range(0,28):
        if countRowBelow(image,i,thresh) == 28:
            count += 1;
    return count;

def countZeroCols(image,thresh):
    count = 0
    for i in range(0,28):
        if countColBelow(image,i,thresh) == 28:
            count += 1;
    return count

if len(sys.argv) < 4:
    print "USAGE: datafile [row|col] #thresh"
    exit()

useRows = False
if sys.argv[2] == "row":
    useRows = True
elif sys.argv[2] == "col":
    useRows = False
else:
    print "Must specify either \"row\" or \"col\""
    exit()

thresh = int(sys.argv[3])
if thresh < 0 or thresh > 255:
    print "thresh must be between 0 and 255"
    exit()

datafile = sys.argv[1]
allimages = pd.DataFrame.from_csv(datafile)

if useRows:
    print "imagenum, zerorowcount"
    for i in range(len(allimages)):
        count = countZeroRows(allimages.iloc[i],thresh)
        print repr(i) + ', ' + repr(count)
else:
    print "imagenum, zerocolcount"
    for i in range(len(allimages)):
        count = countZeroCols(allimages.iloc[i], thresh)
        print repr(i) + ', ' + repr(count)

