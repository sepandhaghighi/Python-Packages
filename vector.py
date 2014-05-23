from numbers import *
from operator import *
from sys import *
from math import*
def Dot(self,v):
    '(vec,vec)--> Integer'
    a=vec(v.D,{})
    if len(self.D)!=len(v.D):
        print("Domain Is Not The Same")
    else:
        s=0
        for i in v.D:
            s=s+self.R[i]*v.R[i]
        return s
def list2vec(list_1,list_2=[]):
    "(Domain , Codomain)--> vec"
    if len(list_2)==0:
        Domain=[]
        for i in range(len(list_1)):
            Domain.append(i+1)
        R={Domain[i]:list_1[i] for i in range(len(list_1))}
        return vec(Domain,R)
    elif len(list_1)!=len(list_2):
        print("Size Of Lists Are Not Same")
    else:
        E={list_1[i]:list_2[i] for i in range(len(list_1))}
        return vec(list_1,E)
def vec2list(vector,a=1):
    "(vec ,1:Domain)--> list"
    if a==1:
        return list(vector.R.keys())
    else :
        return list(vecotr.R.values())
def vec2dic(vecotr):
    "(vec)--> dict"
    return vecotr.R      
def dic2vec(dic):
    "(dict)--> vec"
    return vec(list(dic.keys()),dic)
def cardinal(vector):
    "(vec)--> integer"
    return len(vector)
def num(vector):
    "(vector)--> integer"
    s=0
    for i in list(vector.R.values()):
        s=s+i**2
    return sqrt(s)    
    
    
class vec:
        
    def __init__(self,D,R):
        self.D=D
        self.R=R
        for j in list(self.R.keys()):
            if j not in self.D:
                print("Domain And Co-Domain Are  Not Syns")
                return None
        for i in range(len(self.D)):
            if self.D[i] not in list(self.R.keys()):
                self.R[self.D[i]]=0        
    def __add__(self,v):
        ''' (vec , vec) -> vec
        '''     
        a=vec(v.D,{})
        if len(self.D)!=len(v.D):
            print("Domain Is Not The Same")
        else:
            for i in v.D:
                a.R[i]=v.R[i]+self.R[i]
            return a
    def __getitem__(self,d):
        if d in self.R.keys():
            return self.R[d]
        else:
            print("Wrong Items")
    def __setitem__(self,d,v):
        if d in self.R.keys():
            self.R[d]=v
        else:
            print("Wrong Items")
    def __sub__(self,other):
        ''' (vec , vec) -> vec
        '''     
        return self+(-1)*other
    def __neg__(self):
        ''' (vec) -> vec
        '''     
        return -1*self

    def __pow__(self,v):
        ''' (vec , Int) -> vec
        '''     
        for i in self.D:
            self.R[i]=self.R[i]**v
        self.show()    
    def __equal__(self,v):
        ''' (vec , Vec) -> Bool
        '''     
        if self.D==v.D:
            if self.R==v.R:
                return True
        return False
    def __truediv__(self,other):  
        return (1/other)*self
    def __mul__(self,other):
        ''' (vec , int) -> vec
        '''     
        for i in self.D:
            self.R[i]=self.R[i]*other
        self.show()
    def __len__(self):
        ''' (vec) -> Number
        '''     
        e=0
        for i in self.D:
            if self.R[i]!=0:
                e=e+1
        return e
    __dim__=__len__
    
    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.R) + ")" 
                
        
               
        
