#coding=utf-8
from MinEntropyNew import *

#从目录1
mypath1 = "./Dev1"
print "The measured path1 is: ", mypath1
mypath2 = "./Dev2"
print "The measured path1 is: ", mypath2
DatasizePerfile = 512

DL1 = generateBitsList(mypath1,DatasizePerfile)
DL2 = generateBitsList(mypath2,DatasizePerfile)
#print len(DL1),len(DL1[0]),DL1[0]
#print len(DL2),len(DL2[0]),DL2[0]

#从dev1获得一组数据，从dev2获得一组数据，组合成真正的SRAM数据，共4096+4096=8192 bits，然后将其分成64组，每组128 bits，并进行最小熵的计算
SRAMdata = DL1[0] + DL2[0]
#print SRAMdata
#print len(SRAMdata)
GroupBits = 128
myMinEnt = clac_MinEntropyFromOneList(SRAMdata, GroupBits)
print "GroupLengths:",GroupBits,";randomness:",myMinEnt

#The data from random is not enough
#myrandom = "C:/vonwaist/workplacePython/random"
#ranDL = generateBitsList(myrandom,128)
#myrandomMinEnt = clac_MinEntropyFromOneList(ranDL[0], GroupBits)
#print "GroupLengths:",GroupBits,";randomness:",myrandomMinEnt


