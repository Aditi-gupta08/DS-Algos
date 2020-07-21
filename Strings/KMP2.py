def prefix( w ):
    n = len(w)
    aux = [0] * n
    
    for i in range(1,n):
        j = aux[i-1]
        
        while j>0 and w[i] != w[j]:
            j = aux[j-1]
            
        if w[i] == w[j]:
            j+=1
        aux[i] = j
    return aux
    
    
    
def kmp(w, t):
    if len(w)==0:
        print("Invalid pattern")
        return []
        
    aux = prefix(w)
    i = 0
    j = 0
    
    found= []
    
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
                found.append(j-i)
                i = aux[i-1]
    return found       


n = int(input())
for i in range(n):
    tmp = input()
    lst = list(tmp.split(" "))
    
    t = lst[0]
    w = lst[1]
    found = kmp(w, t)
    
    if len(found)==0:
        print("Not Found")
    else:   
        print(len(found))
        
        for i in found:
            print(i+1, end=" ")
    print("\n")