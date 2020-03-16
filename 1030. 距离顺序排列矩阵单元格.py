
def allCellsDistOrder(R: int, C: int, r0: int, c0: int):
    list1=[]
    for i in range(R):
        for j in range(C):
            list1.append([abs(i-r0)+abs(j-c0),i,j])

    return [[i,j] for _,i,j in sorted(list1)]


R = 2
C = 3
r0 = 1
c0 = 2
print(allCellsDistOrder(R,C,r0,c0))

