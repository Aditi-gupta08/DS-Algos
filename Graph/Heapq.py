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