from numbers import *
from operator import *
from sys import *
from math import*
from functools import*
def Dot(self,v):
    '(vec,vec)--> Integer , Dot Production Of Vectors'
    a=vec(v.D,{})
    if len(self.D)!=len(v.D):
        print("Domain Is Not The Same")
    else:
        s=0
        for i in v.D:
            s=s+self.R[i]*v.R[i]
        return s
def list2vec(list_1,list_2=[]):
    "(Domain , Codomain)--> vec , List To Vector Convert"
    if len(list_2)==0:
        Domain=[]
        for i in range(len(list_1)):
            Domain.append(i+1)
        R={Domain[i]:list_1[i] for i in range(len(list_1))}
        return vec(set(Domain),R)
    elif len(list_1)!=len(list_2):
        print("Size Of Lists Are Not Same")
    else:
        E={list_1[i]:list_2[i] for i in range(len(list_1))}
        return vec(set(list_1),E)
def vec2list(vector,a=1):
    "(vec ,1:Domain)--> list , Vector To List Convert"
    if a==1:
        return list(vector.R.keys())
    else :
        return list(vecotr.R.values())
def vec2dic(vecotr):
    "(vec)--> dict , Vector To Dictionary Convert"
    return vecotr.R      
def dic2vec(dic):
    "(dict)--> vec , Dictionary To Vector Convert"
    return vec(set(dic.keys()),dic)
def cardinal(vector):
    "(vec)--> integer , Vector Cardinality"
    return len(vector)
def num(vector):
    "(vector)--> integer , Vector Number"
    s=0
    for i in list(vector.R.values()):
        s=s+i**2
    return sqrt(s)
def total_sum(vector):
    '''
 (vec)--> number  , Sum Of All Values

'''
    v=list(vector.R.values())
    return sum(v)
def total_mul(vector):
    '''
    (vec)--> number , Multiplication Of All Values
'''
    v=list(vector.R.values())
    return reduce(lambda x,y:x*y , v)
class vec:
        
    def __init__(self,D={},R={}):
        "(set,dict)--> vec"
        self.D=set(D)
        self.R=dict(R)
        for j in list(self.R.keys()):
            if j not in self.D:
                print("Domain And CoDomain Are  Not Syns")
                return None
        for i in range(len(self.D)):
            if list(self.D)[i] not in list(self.R.keys()):
                self.R[list(self.D)[i]]=0        
    def __add__(self,v):
        ''' (vec , vec(number)) -> vec
        '''
        a=vec(self.D,{})
        if type(v)==int or type(v)==float:
            for i in a.D:
                a.R[i]=self.R[i]+v
            return a
        else:
            
            if len(self.D)!=len(v.D):
                print("Domains Are Not The Same")
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
    def __mul__(self,other):
        ''' (vec , int) -> vec
        '''
        v=vec(self.D,{})
        for i in self.D:
            v.R[i]=self.R[i]*other
        return v        
    def __sub__(self,other):
        ''' (vec , vec) -> vec
        '''
        r=self+other*(-1)
        return r
    def __neg__(self):
        ''' (vec) -> vec
        '''     
        return -1*self

    def __pow__(self,v):
        ''' (vec , Int) -> vec
        '''
        w=vec(self.D,{})
        for i in self.D:
            w.R[i]=self.R[i]**v
        return w   
    def __equal__(self,v):
        ''' (vec , Vec) -> Bool
        '''     
        if self.D==v.D:
            if self.R==v.R:
                return True
        return False
    def __truediv__(self,other):  
        return (1/other)*self
    def __len__(self):
        ''' (vec) -> Number
        '''     
        e=0
        for i in self.D:
            if self.R[i]!=0:
                e=e+1
        return e
    __dim__=__len__
    def __sum__(self):
        s=0
        for i in self.D:
            s=s+self.R[i]
        return s
    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.R) + ")" 
                
        
               
        
