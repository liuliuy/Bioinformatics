# -*- coding: cp936 -*-
import numpy as np
#################################定义全局比对函数Global_align############################
def Global_align(se1,se2,tab):
#####################创建2个2维矩阵，全部为0，然后初始化第一行和第一列#########################
#####################tab1存储分数，tab2存储分数来源#######################################
    tab1=np.zeros((len(se1)+1,len(se2)+1),np.int)
    tab2=np.zeros((len(se1)+1,len(se2)+1),np.string_)
    for i in range(len(se2)+1):
        tab1[0][i],tab2[0][i]=i*(-4),'-'
    for i in range(len(se1)+1):
        tab1[i][0],tab2[i][0]=i*(-4),'|'
#################################进行双序列全局比对######################################
    for i in range(len(se1)):
        aa1=se1[i]
        for j in range(len(se2)):
            aa2=se2[j]
            score1=int(tab[aa1][aa2])
            tab1[i+1][j+1]=max(tab1[i][j]+score1,tab1[i+1][j]-4,tab1[i][j+1]-4)            
            if tab1[i+1][j+1]==tab1[i][j]+score1:
                tab2[i+1][j+1]='*'
            elif tab1[i+1][j+1]==tab1[i+1][j]-4:
                tab2[i+1][j+1]='-'
            else:
                tab2[i+1][j+1]='|'
#################################进行路径返溯######################################
    seq1,seq2=[],[]
    i,j=len(se1),len(se2)
    Score1=tab1[i][j]   #全局比对的总分
    while i+j>0:
        if tab2[i][j]=='*':
            i,j=i-1,j-1
            seq1.append(se1[i])
            seq2.append(se2[j])
        elif tab2[i][j]=='|':
            i=i-1
            seq1.append(se1[i])
            seq2.append('*')
        elif tab2[i][j]=='-':
            j=j-1
            seq1.append('*')
            seq2.append(se2[j])
    seq1.reverse()
    seq2.reverse()
    seq1,seq2=''.join(seq1),''.join(seq2)
    return seq1,seq2,tab1,tab2  #返回的4个参数：序列1，序列2，打分表，路径表
#################################定义全局比对函数Global_align############################
def Local_align(se1,se2,tab):
#####################创建2个2维矩阵，全部为0，然后初始化第一行和第一列#########################
#####################tab1存储分数，tab2存储分数来源#######################################
    tab1=np.zeros((len(se1)+1,len(se2)+1),np.int)
    tab2=np.zeros((len(se1)+1,len(se2)+1),np.string_)
    for i in range(len(se2)+1):
        tab2[0][i]='-'
    for i in range(len(se1)+1):
        tab2[i][0]='|'
#################################进行双序列局部比对######################################
    for i in range(len(se1)):
        aa1=se1[i]
        for j in range(len(se2)):
            aa2=se2[j]
            score1=int(tab[aa1][aa2])
            tab1[i+1][j+1]=max(tab1[i][j]+score1,tab1[i+1][j]-4,tab1[i][j+1]-4,0)
            if tab1[i+1][j+1]==0:
                tab2[i+1][j+1]='X'
            elif tab1[i+1][j+1]==tab1[i][j]+score1:
                tab2[i+1][j+1]='*'
            elif tab1[i+1][j+1]==tab1[i+1][j]-4:
                tab2[i+1][j+1]='-'
            else:
                tab2[i+1][j+1]='|'
#################################进行路径返溯###########################################
    seq1,seq2=[],[]
    a=np.argmax(tab1)
    i,j=a/(len(se2)+1),a%(len(se2)+1)
    Score1=np.max(tab1)   #局部比对的总分
    while tab1[i][j]>0:
        if tab2[i][j]=='*':
            i,j=i-1,j-1
            seq1.append(se1[i])
            seq2.append(se2[j])
        elif tab2[i][j]=='|':
            i=i-1
            seq1.append(se1[i])
            seq2.append('*')
        elif tab2[i][j]=='-':
            j=j-1
            seq1.append('*')
            seq2.append(se2[j])
    seq1.reverse()
    seq2.reverse()
    seq1,seq2=''.join(seq1),''.join(seq2)
    return seq1,seq2,tab1,tab2  #返回的4个参数：序列1，序列2，打分表，路径表'''
