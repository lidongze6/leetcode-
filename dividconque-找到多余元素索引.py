def findextranum(num1,num2):
    num1.sort()
    num2.sort()
    l1=l2=0
    while l1<len(num1) and l2<len(num2):
        if num1[l1]==num2[l2]:
            l1+=1
            l2+=1
        elif num1[l1] !=num2[l2]:
            return num2[l2] if len(num2)>len(num1) else num1[l1]

