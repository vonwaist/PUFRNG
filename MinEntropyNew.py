#coding=utf-8

import os
import os.path
import struct
import math
from collections import Counter
import numpy as np

#将n转换为二进制字符串
def bstr(n): # n in range 0-255
    return ''.join([str(n >> x & 1) for x in (7,6,5,4,3,2,1,0)])

#输入文件路径path，和文件的字节长度size，一个字节一个字节的读取，将读取的字节列表返回
def read_binary(path,size):
	f = open(path,'rb')
	binlist = []
	count =0
	while (count < size):
		bin, = struct.unpack('B',f.read(1)) # B stands for unsigned char (8 bits)
		binlist.append(bin)
		count = count + 1
	f.close()
	return binlist

#与read_binary一样读二进制文件，不过返回的列表是二进制字符串
def read_binary_str(path,size):
	f = open(path,'rb')
	binlist = []
	count = 0
	while (count < size):
		bin, = struct.unpack('B',f.read(1)) # B stands for unsigned char (8 bits)
		strBin = bstr(bin)
		binlist.append(strBin)
		count = count + 1
	f.close()
	return binlist
	
#输入一个目录dir，读取dir所有文件，并将读取的字节协议二维数组FileDataLists中并返回
def getDataFromDir(dir,size):
	for root,dirs,files in os.walk(dir):
		file_nums = len(files)
		FileDataLists = [[] for i in range(file_nums)]
		index = 0
		for name in files:
			#print name
			filepath = root + '/' + name
			FileDataLists[index] = read_binary(filepath,size)
			index = index + 1
	return FileDataLists

#与getDataFromDir一样，不过返回的二维数组中是二进制字符串
def getDatabitsFromDir(dir,size):
	for root,dirs,files in os.walk(dir):
		file_nums = len(files)
		FileDataLists = [[] for i in range(file_nums)]
		index = 0
		for name in files:
			#print name
			filepath = root + '/' + name
			FileDataLists[index] = read_binary_str(filepath,size)
			index = index + 1
	return FileDataLists

#以字节为单位计算最小熵，每个字节可取的值有2^8=256，故log计算以256为基数
#最小熵值表示1字节里面包含多少字节的随机性，如均匀分布是理想的随机情况，这样pmax=1.0/256，得到最小熵为1
def calc_MinEntropy_Byte(x):
	L = float(len(x))
	if L <= 1.0:
		return 0
	counts = np.bincount(x)
	probs = counts / L 
	pmax = probs.max()
	if pmax <= 0.0:
		return 0 
	minentropy = -math.log(pmax, 256)
	return pmax,minentropy

#以比特为单位计算最小熵，每个比特可取的值有0或者1两种可能，故log计算以2为基数
#最小熵值表示1比特里面包含多少比特的随机性，如均匀分布是理想的随机情况，这样pmax=0.5，得到最小熵为1	
def calc_MinEntropy_bit(x):
	L = float(len(x))
	if L <= 1.0:
		return 0
	counts = np.bincount(x)
	probs = counts / L 
	pmax = probs.max()
	if pmax <= 0.0:
		return 0 
	minentropy = -math.log(pmax, 2)
	return pmax,minentropy
	
#计算列表中1所占的百分比,x列表中只有0和1
def cacl_Probs(x):
	L = float(len(x))
	counts = np.bincount(x)
	probs = counts / L
	return probs[0]
	
#从文件里一个bit一个bit的读取，存入数组mydatabits中，有多少个文件就有多少个数组（相当于二维数组）
def generateBitsList(path, size):
	mydatabitstring = getDatabitsFromDir(path,size)
	datalen = len(mydatabitstring)
	mydatabits = [[] for i in range(datalen)]
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
	return mydatabits

#输入SRAMdata（一组SRAM数据列表），GroupBits（分组长度），返回最小熵
def clac_MinEntropyFromOneList(SRAMdata, GroupBits):
	GroupNums = len(SRAMdata)/GroupBits
	print "Total Bits: ",len(SRAMdata),";Bits for Each Group: ", GroupBits,";Total Group numbers:",GroupNums
	SRAMdataGroups = [[] for i in range(GroupBits)]
	for i in range(GroupBits):
		SRAMdataGroups[i] = SRAMdata[i::GroupBits]
	MinEntropybits = 0.0
	for ed in SRAMdataGroups:
		em,emin = calc_MinEntropy_bit(ed)
		#print emin
		MinEntropybits += emin
	return MinEntropybits