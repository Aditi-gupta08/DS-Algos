# Topological sort (using dfs)

import collections

class solution:
    
    def topological_sort(self):
        n = 6
        lst = [[0,1], [0,3], [1,2], [1,3], [2,3], [2,5], [2,4], [3,5], [3,4], [5,4] ]
        self.graph = collections.defaultdict(list)
        self.stack = []
        
        for u,v in lst:
            self.graph[u].append(v)
        
        self.visited = [False]*n
        
        # Calling dfs for source node
        for i in range(n):
            if self.visited[i]==False:
                self.dfs(i)
                
        while(len(self.stack)>0):
            print(self.stack.pop(), end=" ")
        
        
        
    def dfs(self, i):
        
        self.visited[i] = True
        
        for neigh in self.graph[i]:
            if self.visited[neigh] == False:
                self.dfs(neigh)
        
        # Appending to stack when out-degree is 0 (Means no neighbour unvisited is left)
        self.stack.append(i)
    
    

s1 = solution()
s1.topological_sort()