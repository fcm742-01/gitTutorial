#!/usr/local/bin/python -O
import math
import io
from collections import defaultdict
from numpy import random

WIDTH=10
SIZE=10000
random.seed()
av = [random.randint(WIDTH) for _ in range(10)]


def constraint1(av):
    if sum(av) < 55:
	av +=['A']
	return True,av
    return False,av

def constraint2(av):
    if sum(av) >= 55:
	av +=['B']
	return True,av
    return False,av

def generate(s=SIZE,cons=constraint1):
    c = None
    size = 0
    while size < s:
        av = [random.randint(WIDTH) for _ in range(10)]
        tf,av =  cons(av)
	if tf :
	    if c is None :
                c = [av]
            else:
                c.append(av)
            size += 1
    return c



def printcsv(a,name,flag='w'):
    f = open(name + '.csv',flag)
    for r in a:
        print >> f , ','.join(map(str,r))
    f.close()

def readcsv(name,cats,header=False):
    a1 = []
    a2 = []
    f = open(name,'r')
    if header:
	h = f.readline()
    for r in f.readlines():
	
	l = r.strip().split(',')
	cat = l.pop()
	if cat == cats[1]:
	    a1.append(map(int,l))
	else:
	    a2.append(map(int,l))
	
    return a1,a2
    
def generate_datasets():
    #generate test data
    a1 = generate(10000,constraint1)
    printcsv(a1,'v1')
    a2 = generate(10000,constraint2)
    printcsv(a2,'v1','a')
    #b = generate(av1,v11,1)    
    
    

class em:
    # p(t | xi=vi) = p(xi=v1| t) / p(xi=vi)
    _l = defaultdict(lambda : defaultdict(float))
    _s = defaultdict(float)
    _c = defaultdict(float)
    _n = 0
    _ITER = 16
    
    def score(self,word,cat):
	p = 1	
	for i, e in enumerate(word):
	    if self._s[(i,e)] > 0:
		p += self._l[cat][(i,e)]/self._s[(i,e)]*self._c[cat]
		
	return p/self._c[cat]
	
    def add_p(self,i,v,cat):
	self._s[(i,v)] += 1
	self._l[cat][(i,v)] += 1
	self._c[cat] += 1
	self._n += 1


    def e_step(self,word,cat):
	for i, z in enumerate(word):
	    self.add_p(i,z,cat)
    
    def m_step(self,word,cat):
	s = self.score(word,cat)
	for i,v in enumerate(word):
	    self._l[cat][(i,v)] += 0.1
	    self._c[cat] += 0.1
	
	
    def	train(self,word, cat):	
	for h in range(0,self._ITER):
	    self.e_step(word, cat)
	    self.m_step(word, cat)  
	    
    def trainlist(self,l,cat):
	for x in l :
	    self.train(x,cat)	

    def guess(self,l):
	s1,s2 =  self.score(l,1),self.score(l,2)
	return 1 if s1 > s2 else 2
		
		

def test1():
    
    e = em()
    A = generate(10000,constraint1)
    B = generate(10000,constraint2)
     
    em.trainlist(A,1)
    em.trainlist(B,2)  
       
    t1,t2 = generate(100,constraint1),generate(100,constraint2)
    sc,s = 0.0,0.0
    for a1 in t1:
	s1,s2 =  e.score(a1[0],1),e.score(a1[0],2)
	sc += 1
	if s1 > s2 :
	    s+=1
    print 'success',s/sc
    
    
    for a2 in t2:
	s1,s2 = e.score(a2[0],1),e.score(a2[0],2)
	sc +=  1
	if s1 < s2 :
	    s+=1
    print 'success', s/sc    
    






def train_guess(f):   
    e = em()
    a1,a2 = readcsv(f[0],f[1],f[2])
    off1 = int(0.9*float(len(a1)))
    off2 = int(0.9*float(len(a2)))

    e.trainlist(a1[:off1], 1)
    e.trainlist(a2[:off2], 2)
    print f[0], ' training done :',off1,off2
    sc,s = 0.0,0.0


    for x in a1[off1:]:
        g = e.guess(x)
        s += 1 if g == 1 else 0
	if g == 1:
	    print '+',
        sc += 1
    print
    for x in a2[off2:]:
        g = e.guess(x)
        s += 1 if g == 2 else 0
	if g == 2:
	    print '*',
        sc += 1    
    print
    print f[0], ' success rate :',float(s/sc*100.0)    

#generate_datasets()

files = [ 
    #('dataset-AlevMorgan.csv',['A','B'],True),('dataset-CarlosPablo.csv',['A','B'],True),
    ('hw1_Min_Ma.csv',['T','F'],False),
    ('v1.csv',['A','B'],False),
    ('ex0.txt',[1,0],False),
    ]
    
for t in files:
    train_guess(t)