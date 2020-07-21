# Dijisktra implementation using adjacency list (greedy - without priority heap)

from collections import defaultdict
import heapq
    
    
def print_res(dist):
    print("\n\nFinal Result :: ")
    print("Vertex   Distance from source")
    for i in range(len(dist)):
        print(i, "\t\t", dist[i])
    
    
    
def print_step(u, dist):
    print(u, end="\t\t")
    for i in range(len(dist)):
        print(dist[i], end="  ")
    print("\n")
    

def min_dist(dist, visited):
    minn = float('inf')
    
    for i in range(len(dist)):
        if visited[i]==False and dist[i]<minn:
            minn = dist[i]
            min_ind = i
            
    return min_ind
    
    
    

def dijikstra(graph, src):
    dist = [float('inf')]*(len(graph))
    
    dist[src] = 0
    visited = [False]*(len(graph))
    
    
    for i in range(len(graph)):
        u = min_dist(dist, visited)
        
        if visited[u]==False:
            for v, w in graph[u]:
                
                if visited[v]==False and w>0:
                    if (dist[u]+ w) < dist[v]:
                        dist[v] = dist[u] + w
   
            visited[u] = True

        print_step(u, dist)
    print_res(dist)
    
    
    


graph = defaultdict(list)

lst = [ [0,1,2], [0,3,7], [1,2,8], [3,2,5], [2,4,4],[2,5,8], [5,4,2] ]

for u,v,w in lst:
    graph[u].append((v, w))
    graph[v].append((u, w))
    
dijikstra(graph, 0)