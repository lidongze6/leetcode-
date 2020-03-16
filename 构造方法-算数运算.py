class C1(int)
    def __init__(self,x):
        self.x=x
    
    def __add__(self,other):
        return int.__add__(self,other)



class C2:
    def __init__(self,x):
        self.x=x
    
    def __add__(self,other):
        return self.x+other.x



class C3:
    def __init__(self,x):
        self.x=x
    
    def __add__(self,other):
        return self+other



class C4(int):
    def __add__(self,other):
        return self+other



class C5:
    def __init__(self,x):
        self.x=x
    
    def __add__(self,other):
        return C.__add__(self,other)




#这5种方法C1和C2能够成功，其中C2，因为a.x+b.x时，type(a.x)是int,相当于int类的相加，而int类的add并没有被改变
#C3会形成无限循环，因为a+b时，type(a)是class,相当于自身类的相加，而返回的是self+other也是类+类这就造成无限的循环了
#C4与C3的区别在于不需初始化，这是因为C4类继承了int类，而int类默认的初始化函数__init__ 故不需添加自身的初始化函数了，如果想改变自身的初始化，则再自己的类中添加初始化函数，其导致的无限循环问题与C2相同
#C5的原因：descriptor '__add__' requires a 'int' object but received a 'C'是由于自身调用了自身的add而我们的目的就是改变add故这种编写方式不能成功



class C6(int)
    def __init__(self,x):
        self.x=x
    
    def __add__(self,other):
        return int.__sub__(self,other)



class C7:
    def __init__(self,x):
        self.x=x
    
    def __add__(self,other):
        return self.x-other.x



class C8:
    def __init__(self,x):
        self.x=x
    
    def __add__(self,other):
        return self-other



class C9(int):
    def __add__(self,other):
        return self-other



class C10:
    def __init__(self,x):
        self.x=x
    
    def __add__(self,other):
        return C.__sub__(self,other)


#上述4种方法均能成功，C6,C7不做阐述，C8此时不会陷入无限循环，因为我们这时定义的是add，而返回的是sub函数，而sub并没有被改变，C9也是同理，C10也不存在调用自身的情况了
