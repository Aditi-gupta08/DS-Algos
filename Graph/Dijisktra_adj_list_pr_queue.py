# updated- Dijisktra implementation using adjacency list & priority queue 

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
    


def dijikstra(graph, src):
    dist = [float('inf')]*(len(graph))
    
    dist[src] = 0
    pr_queue = [(0, src)]
    heapq.heapify(pr_queue)
    visited = [False]*(len(graph))
    
    
    for i in range(len(graph)):
        elem, u = heapq.heappop(pr_queue)
        
        if visited[u]==False:
            for v, w in graph[u]:
                
                if visited[v]==False and w>0:
                    if (dist[u]+ w) < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pr_queue, (dist[v], v))
   
            visited[u] = True

        print_step(u, dist)
    print_res(dist)
    
    
    


graph = defaultdict(list)

lst = [ [0,1,2], [0,3,7], [1,2,8], [3,2,5], [2,4,4],[2,5,8], [5,4,2] ]

for u,v,w in lst:
    graph[u].append((v, w))
    graph[v].append((u, w))
    
dijikstra(graph, 0)