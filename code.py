#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import itertools
import random
from datetime import datetime
random.seed(datetime.now())
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from math import log
import collections
# [log(y,10) for y in x]
figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
ipf=os.listdir('Benchmarks/findata')


# In[14]:


print(ipf)


# In[15]:


mypath='Benchmarks/findata'


# In[16]:


def modelsatisfy(clauseMatrix,model):
    count=len(clauseMatrix)
    for i in range(len(clauseMatrix)):
        issat=0
        for j in range(len(clauseMatrix[i])):
            if clauseMatrix[i][j]<0:
                if (model[abs(clauseMatrix[i][j])])==0:
                    issat=1
#                     break
            else:
                if (model[clauseMatrix[i][j]])==1:
                    issat=1
#                     break
        if issat==0:
            count=count-1
    return count


# In[17]:


def findfalsevars(clauseMatrix,model):
    fvars=set()
    for i in range(len(clauseMatrix)):
        issat=0
        for j in range(len(clauseMatrix[i])):
            if clauseMatrix[i][j]<0:
                if (model[abs(clauseMatrix[i][j])])==0:
                    issat=1
#                     break
            else:
                if (model[clauseMatrix[i][j]])==1:
                    issat=1
#                     break
        if issat==0:
            for j in range(len(clauseMatrix[i])):
                fvars.add(abs(clauseMatrix[i][j]))
    return fvars


# In[18]:


def findminconf(clauseMatrix,model,v,fvars):
    maxnow=modelsatisfy(clauseMatrix,model)
    bestmodel=model.copy()
    temp=model.copy()
    for subset in itertools.combinations(fvars,v):
        model=temp.copy()
        for i in subset:
            if model[i]==0:
                    (model[i])=1
            else:
                    (model[i])=0
        newnow=modelsatisfy(clauseMatrix,model)
        if newnow>maxnow:
            bestmodel=model.copy()
            maxnow=newnow
    return bestmodel


# In[19]:


def mainfunc(f,mnratio,avgclause,totclause,meantime):
    print(f)
    text=f.read()
    text=text.split('\n')
    cstart=0
    while text[cstart][0]!='p':
        cstart=cstart+1
    pline=text[cstart].split()
    nvars=int(pline[1])
    nclause=int(pline[2])
    totclause.append(nclause)
    modelset=set()
    mnratio.append(float(nclause)/float(nvars))
    clauseMatrix=[]
    for i in range(int(nclause)):
        pline=text[cstart+1+i].split()
        t=[]
        for j in range(len(pline)-1):
            if(int(pline[j])<0):
                t.append((int(pline[j])))
            else:
                t.append(int(pline[j]))
        clauseMatrix.append(t)
    model=list()
    model=[None]*int(nvars+1)
    for i in range(nvars+1):
        model[i]=random.randint(0,1)
    v=0
    maxit=500
    maxv=4
    pflip=0.5
    bestclause=0
    key=0
    sumclause=0
    ccount=0
    temp=maxit
    while v<maxv:
        v=v+1
        maxit=temp
        for i in range(nvars+1):
            model[i]=random.randint(0,1)
        while maxit>0:
#             print(v,maxit)
            maxit=maxit-1
            count=modelsatisfy(clauseMatrix,model)
            mcopy=model.copy()
            modelset.add(tuple(mcopy))
            sumclause+=count
            ccount=ccount+1
            if(count>bestclause):
                bestclause=count
            if count==nclause:
                print(model[1:])
                print("-----------------------")
                verdict="YES"
                key=1
                v=maxv+1
                break
            fvars=findfalsevars(clauseMatrix,model)
            x=random.random()
            if x>=pflip:
                choose=v
                if(len(fvars)<v):
                    choose=len(fvars)
                flippy=random.sample(fvars,choose)
                for i in flippy:
                    if (model[i])==0:
                        (model[i])=1
                    else:
                        (model[i])=0
            else:
                model=findminconf(clauseMatrix,model,v,fvars)
    if key==0:
        print("NO")
        verdict="NO"
    avgclause.append(float(sumclause)/float(ccount))
    meantime.append(ccount)


# In[20]:


mnratio=[]
avgclause=[]
totclause=[]
meantime=[]
for file in ipf:
    f=open((mypath+"/"+file))
    mainfunc(f,mnratio,avgclause,totclause,meantime)
    f.close()


# In[26]:


figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(mnratio,meantime,color="blue",marker=".")
plt.xlabel('mnratio')
plt.ylabel('meantime')
plt.show()


# In[22]:


res=dict(zip(mnratio,meantime))
od = collections.OrderedDict(sorted(res.items()))
from matplotlib.pyplot import figure
figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(od.keys(),od.values())
plt.xlabel('mnratio')
plt.ylabel('meantime')
plt.show()


# In[25]:


figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(od.keys(),[log(y,2) for y in od.values()])
plt.xlabel('mnratio')
plt.ylabel('log(meantime)')
figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




