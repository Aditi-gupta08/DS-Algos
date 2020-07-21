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
        pair<int, int> top = pq2.top();
        cout<<top.first<<"  "<<top.second<<endl;
        pq2.pop();
    }
    cout<<endl;
    
}