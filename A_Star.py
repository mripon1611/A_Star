from array import *
import heapq
from queue import PriorityQueue
import math
f = open("input.txt", "r")
sl=f.readlines()
#print(sl)
pcw=[] #parent cheild and weight
hw=[] #he weight
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
h_dic={} #dictionary for he
pr_dic={} #dictionary came from
w_dic={} #dictionary for weight
pw_dic={} #from starting node to Nth node
w_dic[pcw[0][0]]=0 #start to start
for i in range(len(hw)):
    h_dic[hw[i][0]]=int(hw[i][1])
#print(h_dic)
for i in range(len(pcw)):
    pr_dic[pcw[i][1]]=pcw[i][0]
    w_dic[pcw[i][0]+pcw[i][1]]=int(pcw[i][2])
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
            x= (cw - h_dic[ch] + h + w_dic[pcw[i][0]+pcw[i][1]])
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

""""
def a_star(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or graph[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)

            path.reverse()

            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in graph:
        return graph[v]
    else:
        return None


def heuristic(n):

    dist = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0,

    }

    return dist[n]


graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('J', 3)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],



    'J': [('I', 5), ('J', 5)],


}
a_star('A', 'J')
"""