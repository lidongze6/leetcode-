import random

def shuffle_1(Card):
    random.shuffle(Card)

def shuffle_2(Card):
    for k in range(len(Card)):
        i=random.randint(0,len(Card)-1)
        j=random.randint(0,len(Card)-1)
        Card[i],Card[j]=Card[j],Card[i]


def shuffle_text(f):
    result=[[0 for i in range(10)] for j in range(10)]

    for i in range(1000):
        A=[n for n in range(0,10)]
        f(A)
        for j in range(len(A)):
            result[A[j]][j]+=1
    print("\n".join([" ".join(["{:6}".format(item) for item in row])
                     for row in result]))


shuffle_text(shuffle_1)


