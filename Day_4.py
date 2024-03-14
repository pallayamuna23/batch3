#while loop
#--->break using while loop
#1.iterate from 20 to 30 and break the loop in 27
#eg:1
'''
i=20
while i<31:
    if i==27:
      break
    print(i)
    i+=1
    
#eg:2
i=20   
while i<31:
     print(i)
     i+=1
     if i==27:
        break
  
#eg:3
i=20   
while i<31:
     print(i)
     if i==27:
        break
     i+=1

#eg:4
i=20
while i<31:
     if i==27:
        print(i)
        break
     i+=1
'''
#!--->continue
#eg:1
'''
i=20
while i<31:
    if i==27:
       continue
    print(i)
    i=i+1
'''
#while to iterate from 12 to 22
#find the sum of all numbers
'''
i=12
sum=0
while i<23:
    sum=sum+i
    print(sum)
    i+=1
  
i=12
sum=0
while i<23:
    sum=sum+i
    i=i+1
print(sum)    

#eg:2 average of 20 to 25
i=20
sum=0
while i<26:
    sum=sum+i
    i=i+1
    average=sum/6
print(average)

#eg:3 average of 20 to 30
i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    i=i+1
    count+=1
print(sum/count)

#!--->nested for loop
#eg:1
for row  in range(1,3+1):
    for col  in range(1,4+1):
        print(row,col)

#eg:2
for  i in range(1,3+1):
    for j  in range(1,4+1):
        print(i,j)

#eg:3
for  row in range(1):
    for col in range(1):
        print("1,2,3 4,5,6 7,8,9 10,11,12",end=" ")
        print()

#to print stars in right triangle
for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()

#eg:4
for row in range(0,6):
    for col in range(row,6):
        print("*",end=" ")
    print()

#eg:5
for row in range(5):
    for col in range(5):
        if col==0 or col==4 or row==0  or row==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    print()

#eg:6
for row in rrange(0,5):
    for col in range(0,6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
            
    print()

#eg:7
for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==0) or (row==0 and(col>=1 and col<=2) or (row==0 and (col>=2 and col<=3) or (row==0 and (col>=3 and col<=4))))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
 
#--->list
#data types
primary
number-->int,float,complex
string
boolean
none
#collection
list
tuple
set
dictionary
'''
#-->list
#1.if the collection of elements are sorrounded by square brackets,it is consired to be  list
#eg:
L1=[4,7,9,9.89,"hello",7+4j,[3,4,5]]
'''
#characteristics of list
1.list have to be sorrounded by[]
2.it is mutable(the elements in the list are changable)
3.every element inside list is indexed
4.the elements inside the list will be ordered format
5.it can be hold duplicate values
6.its heterogenous

#to access the elements in list
L1=[1,4,6,1,7,89,5,4,"Y","G"]
#print(L1)

#-->indexing
in the collection datatypes like list,tuple,string,the elements will be allocated
with predefined unique called index value
we have 2 types of indexing
positive indexing--->start with 0 from left hand side
negative indexing--->with -1 from right hans side

#positive indexing
#print(L1[4])
#-->negative indexing
print(L1[-6])
print(L1[-4])

#-->slicing
#L1=[start_index:end_index:step]
L1=[1,4,6,1,7,89,5,4,"Y","G"]
print(L1[8:10])
print(L1[:10])
print(L1[3:])
print(L1[1:8:2])

#trail=int(input())
#negative index using slicing
L1=[1,4,1,7,89.7,7,7.5,"p","i"]
print(L1[-4:-1])
print(L1[-1:-4])
print(L1[-7:-2:2])
'''
#to insert to add element inside list
#append()
L1=[9,8,0,6]
L1.append("car")
print(L1)





















    
