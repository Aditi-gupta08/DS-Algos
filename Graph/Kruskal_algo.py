# Kruskal implementation using DSU

import collections, heapq

class solution:
    
    def _init_(self):
        self.n = 9
        self.lst = [[0,1,4], [0,7,8], [1,2,8], [1,7,11], [2,3,7], [2,5,4], [2,8,2], [3,4,9], [3,5,14], [4,5,10], [5,6,2], [6,7,1],[6,8,6],[7,8,7]]
        self.link = []
        self.size = [1]*self.n
        
    def find(self, t):
        if self.link[t]==t:
            return t
            
        return self.find(self.link[t])
        
    
    def same(self, i, j):
        if self.find(i)== self.find(j):
            return True
        else:
            return False
            
    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        
        if self.size[i]<self.size[j]:
            i,j = j,i
            
        self.link[j] = self.link[i]
        self.size[i]+= self.size[j]
        
            
    
    
    def kruskal(self):
        graph = collections.defaultdict(list)
        res = []
        cost = 0
        
        for i in range(self.n):
            self.link.append(i)
            
        self.lst.sort(key = lambda x:x[2])
        
        for u,v,w in self.lst:
            if not self.same(u, v):
                self.union(u, v)
                cost+= w
                res.append((u,v))
        
        print("Input edges:  ", self.lst)
        print("\nEdges included in mst:  ", res)
        print("Cost:  ", cost)
        


s1 = solution()
s1.kruskal()