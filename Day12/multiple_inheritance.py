# Inherit more then one class( Two parent class one child class)
class A:
    def class_a_method(self):
        return 'I \'m just a class A method '
    def hello(self):
        return 'hello from class A'
class B:
    def class_b_method(self):
        return 'I \'m just a class B method '
    def hello(self):
        return 'hello from class B'
class C(A,B):                                 #C(B,A)........C-->B-->A-->            C(A,B)..........C-->A-->B
    pass
instance_c = C()
print(instance_c.class_a_method())            
print(instance_c.class_b_method())
print(instance_c.hello())                    #call hello method of class A because C(A,B)  
print(help(C))
#print(C.mro())
#print(C.__mro__)                            #work same like hello but hello easy to learn