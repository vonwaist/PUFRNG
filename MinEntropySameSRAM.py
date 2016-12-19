#coding=utf-8
from MinEntropyNew import *

#从指定目录中读取512字节的数据，以字节为单位读取
#mypath = "./Dev1"
mypath = "./Dev2"
print "The measured path is: ", mypath
mydata = getDataFromDir(mypath,512)
#将读取的数据进行转置，
mychangedata = [[r[col] for r in mydata] for col in range(len(mydata[0]))]
#计算最小熵：比如文件夹中包含n个文件，先对每个文件的第一个字节计算最小熵，接着对第二个，...，最后对第512个字节计算最小熵，积累的最小熵为512字节中包含的随机性
MinEntropy = 0.0
for eachdata in mychangedata:
	eachpmax,eachmine = calc_MinEntropy_Byte(eachdata)
#	print eachmine
	MinEntropy += eachmine
print "512bytes's randomness:",MinEntropy

#以二进制字符串的形式从文件夹中读取
mydatabitstring = getDatabitsFromDir(mypath,512)
datalen = len(mydatabitstring)
mydatabits = [[] for i in range(datalen)]
#将读取的二进制串的形式转换为一个比特一个比特构成的数组形式，存储到mydatabits中
indexcow = 0 
for da in mydatabitstring:
	for dabyte in da:
		mydatabits[indexcow].append(int(dabyte[0],2))
		mydatabits[indexcow].append(int(dabyte[1],2))
		mydatabits[indexcow].append(int(dabyte[2],2))
		mydatabits[indexcow].append(int(dabyte[3],2))
		mydatabits[indexcow].append(int(dabyte[4],2))
		mydatabits[indexcow].append(int(dabyte[5],2))
		mydatabits[indexcow].append(int(dabyte[6],2))
		mydatabits[indexcow].append(int(dabyte[7],2))
	indexcow += 1
#print len(mydatabits[0])
#print mydatabits[0]
#转置数据
mychangedatabits = [[r[col] for r in mydatabits] for col in range(len(mydatabits[0]))]
#以比特形式计算最小熵：4096比特中包含多少比特的随机性
MinEntropybits = 0.0
for ed in mychangedatabits:
	em,emin = calc_MinEntropy_bit(ed)
#	print emin
	MinEntropybits += emin
print "4096bits's randomness:",MinEntropybits

#计算二进制串中1所占的百分比
myper = 0.0 
for eb in mydatabits:
	eper = cacl_Probs(eb)
	#print eper
	myper += eper
myper = myper / len(mydatabits)
print "Avg Percent of 1 in SRAM:",myper
