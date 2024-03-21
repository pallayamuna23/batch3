###
'''
s1="hello how are you"
s2="hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

###
#find the 8th fibonacci number
num=8
n1=-1
n2=1
for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
    print(ans)

#constructors
class profile:
    def __init__(self):
        print("hello world")
obj=profile()


#parameter constructor
#eg:3
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)
obj=profile(1,"yamuna",19)

#eg:4
class c1:
    email="sidhu@gmail.com"
    def m1(self):
        name="sidhu"
        place="chitthor"
        print(name,place)
        print(self.email)
object=c1()
object.m1()

#eg:5
class c1:
    def m1(self):
        name="sidhu"
        age=28
        return name,age
    def dispaly(self):
        print(name,age)
        print(self.m1())
object=c1()
object.display()

# eg:6
# to use the variables inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "malli"
        self.email = "malli@gmail.com"
        # return name, email # error --> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()

#-->Inheritance
#the process of utilising the methods and attributes of parent class
#throught the object of child class it is called as inheritance
#5 types of inheritance
#single inheritance
#multilevel inheritance
#multiple inheritance
#hybrid inheritance
#heirarichal inheritance

#*single inheritance
#it has only one parent class and only one child class
#eg:1
class parent:
    def m1(self):
        print("I am parent class")


class child(parent):
    def m2(self):
        print("I am child class")

obj = child()
obj.m1()

#eg:2
class c1:
    def __init__(self):
        print("Iam constructor from parent class")
class child1(c1):
    pass

obj = child1()

#multilevel inheritance
#eg:1
class voice:
    def sound(self):
        print("all the animals have their own voices")
class dog(voice):
    def dog_voice(self):
        print("bark")
class cat(dog):
    def cat_voice(self):
        print("meow")
class parrot(cat):
    def parrot_voice(self):
        print("speak")
all=parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

# Multiple Inheritance
 #? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()

# ! Eg:2
#method resolution order
class addition:
    def add(self, a,b):
        print(a+b)

class substract:
    def sub(self, a,b):
        print(a-b)

class multiply:
    def mul (self, a,b):
        print(a*b)

class division(addition, substract, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc.mul(5, 2)    
'''
# hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2(c1):
    def m2(self):
        print("class2")
class c3(c2):
    def m3(self):
        print("Class 3")
class c4(c2):
    def m4(self):
        print("class 4")
    def m3(self):
        print("iam m3 from c4")
class c5(c4):
    def m5(self):
        print("Class 4")
class c6(c3,c5):
    def m6(self):
        print("Class 4")
obj=c6()
obj.m3()

# ! -------> Polymorphism
# poly - many, morph--> form
# A function which has the ability t perform more than 1 functionality
# then it is considered to be as polymorphism

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

# * Ploymorphism in operators
#-----> +
# print(8+8)
# print("k"+'l')
# print([1,2,3]+[4,5,6])

# *
# print(6*7)
# l1 = [1,2,3,4]
# print(*l1)
# def f1(*args)
# l1= [1,2,3,4]
# print(l1*10)
# polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading
# 2.) Method overriding






























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































