# Dijisktra implementation without using priority queue

def min_dist(dist, visited):
    minn = float('inf')
    
    for i in range(len(dist)):
        if visited[i]==False and dist[i]<minn:
            minn = dist[i]
            min_ind = i
            
    return min_ind
    
def print_res(dist):
    print("Vertex   Distance from source")
    for i in range(len(dist)):
        print(i, "\t\t", dist[i])

def dijikstra(graph, src):
    dist = [float('inf')]*(len(graph))
    dist[src] = 0
    # heapq.heapify(dist)
    visited = [False]*(len(graph))
    
    
    for i in range(len(graph)):
        u = min_dist(dist, visited)
        
        for v in range(0, len(graph)):
            if visited[v]==False and graph[u][v]>0:
                if dist[u]+graph[u…
# Dijisktra implementation using adjacency list & priority queue 

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
        
        for v, w in graph[u]:
            
            if visited[v]==Fals…
#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define vi vector<int>
#define vii vector<vector<int>>

int main() {
   
    vii data {  {1, 2},
            {2, 3},
            {3, 4},
            {4, 0},
            {2, 4},
            {2, 0},
            {1, 0}};
            
    vector<int> graph[5];
    int u, v;
    
    for(int i=0; i<data.size(); i++)
    {
        u = data[i][0];
        v = data[i][1];
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    for(int i=0; i<5; i++)
    {
        cout<<i;
        for(auto x:graph[i])
            cout<<" -> "<<x;
        
        cout<<"\n";
    }
    
    
}
#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define vi vector<int>
#define vii vector<vector<int>>
#define V 5

    
void print(vector<int> graph[])
{
    for(int i=0; i<V; i++)
    {
        cout<<i;
        for(auto x:graph[i])
            cout<<" -> "<<x;
        
        cout<<"\n";
    }
}


void dfs(vector<int> graph[], int u)
{
    vector<bool> visited(V, false);  
    
    visited[u] = true;
    stack<int> s;
    s.push(u);
    int v, w;
    
    cout<<"DFS Traversal:  ";
    
    while(!s.empty())
    {
        v = s.top();
        s.pop();
        cout<<v<<"  ";
        
        for(int i=0; i<graph[v].size(); i++)
        {
            w = graph[v][i];
            if(!visited[w])
            {
                s.push(w);
…
import heapq
H = [25, 11, 7, 15, 9]

heapq.heapify(H)
print("After heapifying H:  ", list(H))

heapq.heappush(H, 5)
print("After pushing:  ", list(H))

print(heapq.heappop(H))
print("Popping out elem:  ", list(H))

H2 = [5, 7, 9, 4, 3]
H3 = [5, 7, 9, 4, 3]

heapq.heapify(H2)
heapq.heapify(H3)

print("H2: ", list(H2))
print("H3: ", list(H3))

print(heapq.heappushpop(H2, 2))
print(heapq.heapreplace(H3, 2))

print("Heappushpop func:  ", list(H2))
print("Heapreplace func:  ", list(H3))

print(heapq.nlargest(3, H2))
print(heapq.nlargest(1, H2))
print(heapq.nsmallest(2, H2))

# arr = [[2,4], [5,1], [3, 2]]
# heapq.heapify(arr)
# print(list(arr))
#include <bits/stdc++.h>

using namespace std;

int main() {
    priority_queue<int> arr;
    arr.push(10);
    arr.push(2);
    arr.push(7);
    arr.push(5);
    arr.push(1);
    
    priority_queue<int> pq = arr;
    while(!pq.empty())
    {
        cout<<pq.top()<<"   ";
        pq.pop();
    }
    cout<<endl;
    
    cout<<arr.top()<<endl;
    cout<<arr.size()<<endl;
    arr.pop();
    cout<<arr.top()<<endl;
    cout<<arr.size()<<endl;
    
    
    // For pair
    priority_queue<pair<int, int>> arr2;
    arr2.push(make_pair(6,4));
    arr2.push(make_pair(2,2));
    arr2.push(make_pair(4,1));
    arr2.push(make_pair(4,6));
    arr2.push(make_pair(1,1));
    
    priority_queue<pair<int,int>> pq2 = arr2;
    while(!pq2.empty())
    {
        pair<int, in…
def prefix( w ):
    
    aux = [0] * len(w)
    m = 0
    i = 1
    
    while i<len(w):
        if w[m] == w[i]:
            m+= 1
            aux[i] = m
            i+= 1
            
        elif w[m] != w[i] and m!=0:
            m = aux[m-1]
            
        else:
            aux[i] = 0
            i+= 1
    return aux
    
    
    
def kmp(w, t):
    if len(w)==0:
        print("Invalid pattern")
        return 0
        
    aux = prefix(w)
    i = 0
    j = 0
    
    while j<len(t):
        if w[i] != t[j]:
            
            if i!=0:
                i = aux[i-1]
            else:
                j+=1
        
        else:
            i+= 1
            j+= 1
            
            if i==len(w):
                print("Pattern found at index ", j-i)
                i = aux[i-1]
    return 0       
    
print("KMP for 1st pattern: ") 
kmp( "ABABCABAB" , "ABABDABACDABABCABAB")

print("\n\nKMP for 2nd pattern:  ")
kmp( "AABA", "AABAACAADAABAABA")