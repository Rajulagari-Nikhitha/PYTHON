import heapq

class Graph:
    def __init__(self):
        self.d={}
        
    
    def add(self,n1,n2,w):
        if n1 not in self.d:
            self.d[n1]=[]
        if n2 not in self.d:
            self.d[n2]=[]
        self.d[n1].append((n2,w))
        self.d[n2].append((n1,w))
    
    def disp(self):
        for i,j in self.d.items():
            self.d[i]=list(set(j))
        print(self.d)
        

    def dijk(self,s,e):
        self.dist={i:float('inf') for i in self.d.keys()}
        self.parent = {i:None for i in self.d.keys()}
        self.dist[s]=0
        p=[(0,s)]
        print(self.dist,self.parent)
        while p:
            cur_dist,node = heapq.heappop(p)
            if cur_dist>self.dist[node]:
                continue
            if node==e:
                break
            for i,w in self.d[node]:
                d=cur_dist+w
                if d<self.dist[i]:
                    self.dist[i]=d
                    self.parent[i]=node
                    heapq.heappush(p, (d,i))
        print(self.dist,self.parent)
        self.path = []
        cur=e
        while cur is not None:
            self.path.append(cur)
            cur=self.parent[cur]
        self.path = self.path[::-1]
        print(self.path, self.dist[e])

G=Graph()
G.add('o','z',71)
G.add('o','s',151)
G.add('d','m',75)
G.add('d','c',120)
G.add('z','o',71)
G.add('z','a',75)
G.add('c','d',120)
G.add('c','r',146)
G.add('c','p',138)
G.add('a','z',75)
G.add('a','t',118)
G.add('a','s',140)
G.add('r','c',146)
G.add('r','s',80)
G.add('r','p',97)
G.add('t','l',111)
G.add('t','a',118)
G.add('l','t',111)
G.add('l','m',70)
G.add('m','d',75)
G.add('m','l',70)
G.add('p','c',138)
G.add('p','r',97)
G.add('p','b',101)
G.add('u','b',85)
G.add('u','v',142)
G.add('u','h',98)
G.add('f','s',99)
G.add('f','b',211)
G.add('g','b',90)
G.add('v','i',92)
G.add('v','u',142)
G.add('n','i',87)
G.add('h','u',98)
G.add('h','e',86)
G.add('e','h',86)
G.add('i','v',92)
G.add('i','n',87)
G.add('b','p',101)
G.add('b','f',211)
G.add('b','g',90)
G.add('b','u',85)
G.add('s','o',151)
G.add('s','r',80)
G.add('s','a',140)
G.add('s','f',99)
G.disp()

S=input("starting vertex : ")
E=input('ending vertex : ')
G.dijk(S,E)
