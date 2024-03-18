'''
#code:1
d1={'ten':10,'twenty':20,'thirty':30,}
d2={'thirty':30,'fourty':40,'fifty':50}
d1.update(d2)
print(d1)

#code:2
set1={'python','java','data science'}
set2={'ML','AI','R Language','python'}
set3={'data analytics','robotics','deep learning'}
c=0
flag=0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break
    if c==3:
        for val in set3:
            if val in set2 or val in set1:
                flag=1
                break
if flag==0:
    print("disjoint")
else:
    print("joint")

#code:3
list1=["m","na","i","ke"]
list2=["y","me","s","lly"]
l3=[]
for val in range (len(list1)):
    ans=list1[val]+list2[val]
    l3.append(ans)
print(l3)

#using while loop
list1=["m","na","i","ya"]
list2=["y","me","s","mmi"]
l3=[]
i=0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)

#hacker rank--->caesar cipher
#functions
#def
#functions is a block of code which is used to perform a specific functionality
#function can be created using def keyword
#function has 3 parts
#function declaration
#function definition
#function call
#eg:1
def greet(): #function definition
    print("welcome yamuna")
greet()
greet()
greet()
greet()
greet()
greet()
greet()
greet()
greet()
greet() #function calling
'''
#eg:2
#function eith parameter
def greeting(name):
    print("welcome",name)
for val in range(3):
    username=input("enter the name:")
    greeting(username)






















