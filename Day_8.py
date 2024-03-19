#eg:3
'''
def profile(name,age,place):
    txt="my name is {},iam {} years old,iam from {}."
    print(txt.format(name,age,place))
profile("yamuna","20","JMD")
'''
#eg:4
#function with return statement
#return
#1.a variable declared inside the function can be accessed outsde the function using return
#2.return does not print anything
#3.we cannot write any code below return statement
'''
def f1()
    z=8
f1()
print(z) #error-->cannot use outside the function

def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)
def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

#123
def Palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
         print(n,"palindrome")
    else:
        print("not palindrome")
a = int(input("enter the value: "))
palindrome(a)

#based on the declaration of parameter and args
#functions are divided into 3 categories

#positional args
#keyword args
#default args
#variable length args
#keyword variable length args

#(1)positional args
#the position of parameter have to be same as position as arguments
#eg:1
def profile(name,phone,mark):
    txt="my name is {},my number is {},i got {} marks."
    print(txt.format(name,phone,mark))
profile("latha",9878776767,100)

#(2)keywords
#eg:1
#to overcome the disadvantage of position args,we use keyword arg
#it is the process of initialising the parameter with the args while calling the function
def profile(name,phone,mark):
    txt="my name is {},my number is {},i got {} marks."
    print(txt.format(name,phone,mark))
profile(name="latha",phone=9878776767,mark=100)

#todo-->exception of keyword args function
def profile(name,phone,mark):
    txt="my name is {},my number is {},i got {} marks."
    print(txt.format(name,phone,mark))
#profile(name="latha",9878776767,mark=100)#error-->positional args follow keyword args
#profile(9878776767,name="latha",mark=100)#error -->name has multiple values
profile("layha",mark=100,phone=9878776767)

#(3)default args
def profile(name,phone,place="kadapa"):
    txt="my name is {},my phone number is {},i am from {}."
    print(txt.format(name,phone,place))
profile("sid",9876543210,"guntur")

#eg:1
def profile(name,phone,place="kadapa"):
    if (place!="kadapa"):
        print("you are not eligible to signup")
    else:
        txt="my name is {},my phone number is {},i am from {}."
        print(txt.format(name,phone,place))
profile("sid",9876543210,"guntur")

#exception
def profile(name,place="kadapa",phone): #error -->coz default args should not follow positional parameter
    if (place!="kadapa"):
        print("you are not eligible to signup")
    else:
        txt="my name is {},my phone number is {},i am from {}."
        print(txt.format(name,phone,place))
profile("sid",9876543210,"guntur")

#(4)variable length parameters
#eg:1
#to pass more than 1 arg to a parameter means we use variable length args
#to convert normal parameter to variable length parameter,add * to their prefix of parameter
def profile(*name):
    for val in name:
        print("my name is",val)
profile("sid","satya","cutie")

#eg:2
def profile(*name,age):
    for val in name:
        print("my name is",val,"my age is",age)
profile("sid",'name2','name3',28)#error-->age has no args
def profile(age,*name):
    for val in name:
        print("my name is",val,"my age is",age)
profile(28,"sid",'name2','name3')

#keyword variable length args
#which is used to provide the args in the form of key value pair
#eg:1
def price(**price_list):
    print(price_list)
price(shirt=1000, iphone=800000)

#n=5
#{1:1, 2:4, 3:9, 4:16, 5:25}

n=int(input("enter the number:"))
d1={}
for val in range(1,n+1):
    d1[val]=val**2
print(d1)

def dict1(n):
    d1={}
    for val in range(1,n+1):
        d1[val]=val**2
    print(d1)    
dict1(5) 

#--->object oriented programming
#the paradigms of objects orinted programming are
#class
#objects
#inheritance
#polymorphism
#anstraction
#encapsulation

#class is a blue print of an object
#eg:1
class c1:
    name1="yamuna"
    print(name1)

#eg:2
class person:
    name="yamuna"
c=person() # c as object
#the process of creation of an object is called as initialisation
print(c.name)

#eg:3
#create of a method
#when the function is created with a class is called as method
#method without parameter
class person:
    def display(person):
        print("hello welcome to yamuna")
p=person()
p.display()

#eg:4
#method with parameter
class person:
    def display(person,name,age):
        print(name,age)
p=person()
p.display("yamuna",20)

#eg:5
class person1:
    frame="yamuna"#attribute or static variable
    lname="P"
    def first_name(self):
        print(self.frame)
    def full_name(self):
        print(self.frame+" "+self.lname)
p=person1()
p.first_name()
p.full_name()
'''
#eg:6
#constructors-->__init__()
#this is a special method which has the ability to execute itself without
#calling it manually through the process of instantiation
class profile:
    def __init__(self): # constructor method
        print("hey")
p=profile() # execution of constructor through this process











































