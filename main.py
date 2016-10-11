# -*- coding: cp936 -*-
import re
import Align
f=open(r'BLOSUM62.txt')
###############################将23种aa单字母放在aa列表里#########################
while True:
    aa1=f.readline()
    if aa1[0]==' ':
        break
#print aa1
aa=aa1.replace(' ','')[:-2]
#print aa,len(aa)
##############################将BLOSUM矩阵读入字典blosum中########################
blosum={}
for i in aa:
    blosum[i]={}
#print len(blosum)
for i in range(len(aa)):
    s=f.readline()[:-2]
    blo=re.split('[ ]+',s)
    #print blo
    del blo[0]
    #print blo   
    for j in range(len(aa)):
        blosum[aa[i]][aa[j]]=blo[j]
#print blosum['C']
f.close()
##############################将氨基酸序列读入seq1,2中############################
f=open(r'data.txt')
s=f.readline()
#print s,type(s)
s=f.readline()
seq1,seq2=[],[]
while True:
    if s[0]!='>':
        print s[:],type(s)
        seq1+=s[:].replace('\n','').replace('\r','')
        print seq1
        s=f.readline()        
    else:
        break
#print seq1
seq2=list(''.join(f.readlines()).replace('\n','').replace('\r',''))
seq1,seq2=''.join(seq1),''.join(seq2)
f.close()
##############################全局比对结果输出####################################
#######gloseq1/gloseq2--比对的序列结果###gloscore--打分表##glotab--路径信息#########
gloseq1,gloseq2,gloscore,glotab=Align.Global_align(seq1,seq2,blosum)
##############################局部比对结果输出####################################
#######locseq1/locseq2--比对的序列结果###locscore--打分表##loctab--路径信息#########
locseq1,locseq2,locscore,loctab=Align.Local_align(seq1,seq2,blosum)


