# Topological sort (using bfs)

import collections

class solution:
    
    def topological_sort(self):
        n = 6
        lst = [[0,1], [0,3], [1,2], [1,3], [2,3], [2,5], [2,4], [3,5], [3,4], [5,4] ]
       
        graph = collections.defaultdict(list)
        in_degree = [0]*n
        queue = []
        res = []
        
        for u,v in lst:
            graph[u].append(v)
            in_degree[v]+=1
            
        for i in range(n):
            if in_degree[i]==0:
                queue.append(i)
                
        
        while( len(queue)>0 ):
            top = queue.pop(0)
            res.append(top)
            
            for neigh in graph[top]:
                in_degree[neigh]-=1
                
                if in_degree[neigh]==0:
                    queue.append(neigh)
                    
        return res  
       
    
    

s1 = solution()
print(s1.topological_sort())