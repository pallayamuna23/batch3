#----->swapping of variables
a=7
b=5
'''
temp=a
a=b
b=temp
print(a,b)
a=a*b
b=a/b
a=a/b
print(int(a),int(b))
'''
'''
a=a+b
b=a-b
a=a-b
print(a,b)
'''
#id()-->used to find the memory address of the variable
'''
a=7
print(a)
print(id(a))
'''
#---->keywords
#keywords are reserved words which provides special meaning to
#compiler or interpretor
'''
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))
#To check if the string is keyword or not
print(keyword.iskeyword("sid"))
'''
#if = 8
#print(if)
#-->literals
# literal is the constant value assigned to a variable
#A variable is considers to be constant when it is defines in caps
#a=78 # a is variable
#A=78 #A is constant
#hash()--> it creates a hash values for constant datatypes and provides
#error for constant datatypes
'''
n1=89+7j
print(hash(n1))
f1=[7,8,9]
print(hash(f1))#error-->list is non-constant or mutable datatype
'''
'''
a=9
b=9
print(id(a))
print(id(b))
'''
#-->operators
#operates are symbols which is used to preform various operations
#between 2 or more operands
#Arithmatic
#Assegment
#Logical
#Relational or comparison
#Bitwise
#Identity
#membership
#-->Arithmatic are +,-,*,/,%,**,//
'''
#eg:1
a=8
b=6
c=9
print(a+b+c)
#input()--->used to get the runtime input
#eval()-->used to get the runtime values of all datatype
n1=eval(input("enter the value:"))
print(type(n1))
a=4
b=2
print(a/b)# is used to get the quotient value
print(a%b)#is used to get remainder value
'''
'''
#//-->floor devision
a=765433
b=19
print(a//b)
#**-->used for power of a number
print(2**4)
#Assignment---> =,+=,-=,/=,*=,//=,**=,&=
a==8,a==2
print(a)
a=30
a-=5
print(a)
#bitwise operator-->&,|,^,~,<<,>>
a=7
b=4
print(a&b)
AND
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1

2^4 2^3 2^2 2^1 2^0
8 4 2 1
0 1 1 1 #-->7
0 1 0 0 #-->4&
-------------
0 1 0 0 #-->4


# comparison-->==,>,<,!=,<=,>=
a=8
b=7
print(a>b)
a=9
b=5
print(a==b)

#~-->tillday
a=5
print(~a)
a=9
128 64 32 16 8 4 2 1
 0   0  0  0 1 0 0 1 #-->9
 1   1  1  1 0 1 1 0 #-->-10
 0   0  0  0 1 0 1 0 #-->10
 1   1  1  1 0 1 0 1 ->1s compliment of 10
                   1 ->2s compliment
---------------------
 1   1  1  1 0 1 1 0 ->-10

 256 128 64 32 16 8 4 2 1
  0   0   0  0  0 0 1 0 1 3<
  0   0   0  1  0 1 0 0 0 -->40
  107

  #<<,>>
  print(5>>1)
  16>4
  '''
#logical-->and,or,not(used to compare the expressions)
'''
print(a>3 and a<10)
print(a>7 or a<30)
print(not(a>8 and a<10)
'''
#identity operator-->is,is not
#it is used to compare the memory location are stored
'''
a=8
b=8
print(a is b)
print(a==b)

a=[1,2,3]
b=[1,2,3]
print(a is b)
'''
#membership operator-->in,not in
'''
11=[7,8,9,0,4,5]
num=44
print(num in 11)

num=678
print(8 in num) # error
'''
# ! conditional statement
#if elif,else
# python syntax
# if condition:
'''
Eg:1
a=6
if a: print("hello")

Eg:2
a=6
if a>3:
    print("hey")
else:
    print("no")

Eg:3
if 7>8:
    print("yes")
else:
    print("no")

Eg:4
a=0
a=None
a=False
#a=""
if a:
    print("yes")
else:
    print("no")
  '''
# a number is even or odd
n=int(input("enter the number:"))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")
    
    




















