s=['GTCACGTCCG', 'GTCACTCCGA', 'GTCACCCGAA','GTCACCGAAT', 'TCACCGTCCG',
  'TCACCTCCGA', 'TCACCCCGAA', 'TCACCCGAAT', 'CACCAGTCCG', 'CACCATCCGA',
   'CACCACCGAA', 'CACCACGAAT', 'ACCACGTCCG', 'ACCACTCCGA','ACCACCCGAA',
   'ACCACCGAAT']
basetype=['A','G','C','T']
def my_func(n):
    motilist=[]
    for column in range(5):
        for columntype in basetype:
            motilist.append(s[n][column::5].count(columntype))
    return motilist
            
