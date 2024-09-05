import math
import heapq

class Graph:
    def __init__(self):
        self.g={}
    
    def dist(self,n1,n2,x1,y1,x2,y2):
        d=math.sqrt((abs(x2-x1))**2 + (abs(y2-y1))**2)
        self.add(n1,n2,round(d,1))
    
    def add(self,n1,n2,w):
        if n1 not in self.g:
            self.g[n1]=[]
        if n2 not in self.g:
            self.g[n2]=[]
        self.g[n1].append((n2,w))
        self.g[n2].append((n1,w))

    def disp(self):
        for i,j in self.g.items():
            self.g[i]=list(set(j))
        return self.g
    
    def huristic(self,s,e):
        self.dist={i:float('inf') for i in self.g.keys()}
        self.parent = {i:None for i in self.g.keys()}
        self.dist[s]=0
        p=[(0,s)]
        while p:
            cur_dist,node = heapq.heappop(p)
            if cur_dist>self.dist[node]:
                continue
            if node==e:
                break
            for i,w in self.g[node]:
                d=cur_dist+w
                if d<self.dist[i]:
                    self.dist[i]=d
                    self.parent[i]=node
                    heapq.heappush(p, (d,i))
        self.path = []
        cur=e
        while cur is not None:
            self.path.append(cur)
            cur=self.parent[cur]
        self.path = self.path[::-1]
        print(self.path, self.dist[e])
            
G=Graph()
G.dist('o','z',0,10,-2,12)
G.dist('o','s',0,10,4,10)
G.dist('d','m',10,20,8,18)
G.dist('d','c',10,20,12,10)
G.dist('z','o',-2,12,0,10)
G.dist('z','a',-2,12,2,12)
G.dist('c','d',12,10,10,20)
G.dist('c','r',12,10,14,12)
G.dist('c','p',12,10,8,6)
G.dist('a','z',2,12,-2,12)
G.dist('a','t',2,12,4,14)
G.dist('a','s',2,12,14,10)
G.dist('r','c',14,12,12,10)
G.dist('r','s',14,12,4,10)
G.dist('r','p',14,12,8,6)
G.dist('t','l',4,14,6,16)
G.dist('t','a',4,14,2,12)
G.dist('l','t',6,16,4,14)
G.dist('l','m',6,16,8,18)
G.dist('m','d',8,18,10,20)
G.dist('m','l',8,18,6,16)
G.dist('p','c',8,6,12,10)
G.dist('p','r',8,6,14,12)
G.dist('p','b',8,6,10,4)
G.dist('u','b',14,4,10,4)
G.dist('u','v',14,4,16,6)
G.dist('u','h',14,4,16,2)
G.dist('f','s',6,8,4,10)
G.dist('f','b',6,8,10,4)
G.dist('g','b',12,2,10,4)
G.dist('v','i',16,6,18,8)
G.dist('v','u',16,6,14,4)
G.dist('n','i',20,10,18,8)
G.dist('h','u',16,2,14,4)
G.dist('h','e',16,2,18,0)
G.dist('e','h',18,0,16,2)
G.dist('i','v',18,8,16,6)
G.dist('i','n',18,8,20,10)
G.dist('b','p',10,4,8,6)
G.dist('b','f',10,4,6,8)
G.dist('b','g',10,4,12,2)
G.dist('b','u',10,4,14,4)
G.dist('s','o',4,10,0,10)
G.dist('s','r',4,10,14,12)
G.dist('s','a',4,10,2,12)
G.dist('s','f',4,10,6,8)
print(G.disp())
S=input("strarting vertex : ")
E=input("ending vertex : ")
G.huristic(S,E)