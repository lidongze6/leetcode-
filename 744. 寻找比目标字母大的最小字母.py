def nextGreatestLetter(letters, target):
    l,r=0,len(letters)-1
    while l<r:
        mid=(l+r)//2
        if letters[mid]>target:r=mid
        else:l=mid+1

    if l>=r:
        return letters[l] if letters[l]>target else letters[0]



letters = ["c", "f", "j"]
target = "g"
print(nextGreatestLetter(letters,target))

