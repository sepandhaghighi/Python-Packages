from numbers import *
from operator import *
from sys import *
class vec:
    class One:
        def __add__(self, other): return self if other == 0 else 0
        __sub__ = __add__
        def __mul__(self, other):
            if isinstance(other, Number):
                return 0 if other == 0 else self
            return other
        def __div__(self, other):
            if other == 0: raise ZeroDivisionError
            return self
        __truediv__ = __div__
        def __rdiv__(self,other): return other
        __rtruediv__ = __rdiv__
        __radd__ = __add__
        __rsub__ = __add__
        __rmul__ = __mul__
        def __str__(self): return 'one'
        __repr__ = __str__
        def __neg__(self): return self
        def __bool__(self): return True
        
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
    def show(self):
        print('Vec(',self.D,',',self.R,')')
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
    def Dot(self,v):
        ''' (vec , vec) -> Number
        '''     
        a=vec(v.D,{})
        if len(self.D)!=len(v.D):
            print("Domain Is Not The Same")
        else:
            s=0
            for i in v.D:
                s=s+self.R[i]*v.R[i]
            return s
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
                
        
               
        
