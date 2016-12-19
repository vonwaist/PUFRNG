#coding=utf-8

from MinEntropyNew import *
import pandas as pd
import matplotlib.pyplot as plt

def calc_HD(l1,l2):
	len1,len2 = len(l1),len(l2)
	if len1 != len2:
		return 0
	d = 0
	for i in range(len1):
		if l1[i] != l2[i]:
			d += 1
	return d 
	

def calc_IntraHD(list1):
	intraD = []
	dlen = len(list1)
	for i in range(dlen):
		for j in range(i+1,dlen):
			intraD.append(calc_HD(list1[i],list1[j]))
	return intraD
			
def calc_InterHD(list1, list2):
	len1,len2 = len(list1),len(list2)
	if len1 != len2:
		return 0
	interD = []
	for i in range(len1):
		interD.append(calc_HD(list1[i],list2[i]))
	return interD
	
def calc_InterHDNew(list1, list2):
	interD = []
	for i in list1:
		for j in list2:
			interD.append(calc_HD(i,j))
	return interD
	
def get_stats(group):
	return {'count': group.count()}

#从目录1
mypath1 = "./Dev1"
print "The measured path1 is: ", mypath1
mypath2 = "./Dev2"
print "The measured path1 is: ", mypath2
DatasizePerfile = 512

DL1 = generateBitsList(mypath1,DatasizePerfile)
DL2 = generateBitsList(mypath2,DatasizePerfile)

intraD1 = calc_IntraHD(DL1)
intraD2 = calc_IntraHD(DL2)
print len(intraD1),len(intraD2)
print max(intraD1),min(intraD1),sum(intraD1),sum(intraD1)/len(intraD1)
print max(intraD2),min(intraD2),sum(intraD2),sum(intraD2)/len(intraD2)

interD = calc_InterHDNew(DL1,DL2)
print len(interD)
print max(interD),min(interD),sum(interD),sum(interD)/len(interD)

#作图
#bins = [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200]
df = pd.DataFrame({'InterDistance': interD})
#cats = pd.cut(df['InterDistance'],bins)
#print cats
#grouped = df['InterDistance'].groupby(cats)
#bincounts = grouped.apply(get_stats).unstack()
#print bincounts
#bincounts.plot(kind='bar', alpha=0.5, rot=0)
df['InterDistance'].hist(bins=100,alpha=0.5)
plt.show()

df2 = pd.DataFrame({'IntraDistanceDev1': intraD1, 'IntraDistanceDev2': intraD2})
df2.hist(bins=100,alpha=0.5)
plt.show()