import heapq

list=[6,9,7,2,4,3,6]
while list:
    print(heapq.heappop(list))


print("------------------------")
list1=[6,9,7,2,4,3,6]
heapq.heapify(list1)
while list1:
    print(heapq.heappop(list1))

