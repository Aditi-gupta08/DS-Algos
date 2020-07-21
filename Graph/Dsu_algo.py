# DSU

def find(lst, n):
    if lst[n]==-1:
        return n
        
    lst[n] = find(lst, lst[n])
    return lst[n]
    

def union(lst, n1, n2):
    if n1==n2:
        return lst
    
    s1 = find(lst, n1)
    s2 = find(lst, n2)
    if s1 != s2:
        lst[s1] = s2
    
    return lst
        

lst = [-1]*5
print(find(lst, 1))
print(find(lst, 2))
print(find(lst, 3))
lst = union(lst, 1, 2)
print(find(lst, 1))
print(find(lst, 2))

lst = union(lst, 3, 4)
print(find(lst, 3))
print(find(lst, 4))


print("\n\n final:")
lst = union(lst, 3, 2)
print(find(lst, 1))
print(find(lst, 2))
print(find(lst, 3))
print(find(lst, 4))
print(find(lst, 0))

print(lst)