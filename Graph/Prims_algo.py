import collections, heapq

def prim(n, adj, src):
    visited = []
    graph = collections.defaultdict(list)
    h = []
    heapq.heapify(h)

    visited.append(src)
    for v,w in adj[src]:
        heapq.heappush(h, (w,src,v))
        
    while len(visited)!=n:
        w, u, v = heapq.heappop(h)
        
        if v not in visited:
            graph[u].append((v,w))
            graph[v].append((u,w))
            
            src2 = v
            for dest, weight in adj[src2]:
                heapq.heappush(h, (weight, src2, dest))
            
            visited.append(v)
            
    print(graph)
    
        
        
n = 9
lst = [[0,1,4], [0,7,8], [1,2,8], [1,7,11], [2,3,7], [2,5,4], [2,8,2], [3,4,9], [3,5,14], [4,5,10], [5,6,2], [6,7,1],[6,8,6],[7,8,7]]
adj = collections.defaultdict(list)

for u,v,w in lst:
    adj[u].append((v, w))
    adj[v].append((u, w))
    
prim(n, adj, 0)