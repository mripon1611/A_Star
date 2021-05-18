from array import *
import heapq
from queue import PriorityQueue
import math
f = open("input.txt", "r")
sl=f.readlines()
pcw=[]
hw=[]
j=0
k=0
for i in range(len(sl)):
    t=sl[i].split()
    if len(t)==3:
        pcw.insert(j,t)
        j+=1
    elif len(t)==2:
        hw.insert(k,t)
        k+=1
#print(pcw)
#print(hw)
h_dic={}
pr_dic={}
w_dic={}
pw_dic={} #from starting node to Nth node
w_dic[pcw[0][0]]=0
for i in range(len(hw)):
    h_dic[hw[i][0]]=int(hw[i][1])
#print(h_dic)
for i in range(len(pcw)):
    pr_dic[pcw[i][1]]=pcw[i][0]
    w_dic[pcw[i][1]]=int(pcw[i][2])
#print(pr_dic)
#print(w_dic)
qu = PriorityQueue()
qu.put((h_dic[pcw[0][0]], pcw[0][0]))
h= math.inf
pw=math.inf
path=[]
z=0
while qu:
    rr=qu.get()
    ch=rr[1]
    cw=rr[0]
    path.insert(z,ch)
    z+=1
    if h==0:
        break
    for i in range(len(pcw)):
        if ch ==(pcw[i][0]):
            h=h_dic[pcw[i][1]]
            x= (cw - h_dic[ch] + h + w_dic[pcw[i][1]])
            qu.put((x,pcw[i][1]))
            if h==0:
                pw=x
print("\n\nPath wieght = ",end='')
print(pw)
print("\npath : ",end='')
for i in range(len(path)):
    print(path[i],end='')
    if ((i+1)<len(path)):
        print("-->",end='')
print("\n\n")
f.close()