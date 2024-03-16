#--->1) fst and last capitalise letter
'''
s1='hi yamuna'
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)
#-->2)
n = 128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    print(rem)
    check= temp % rem
    if check!=0:
       f1 = 1
    n = n//10
if f1==0:
    print("yes")
else:
    print("no")

#--->3)
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[]
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)
'''
#-->set
#characterstics of set

#1.set can be created string()
#2.the elements inside set are not indexed
#3.does not allow duplicate values
#4.it ordered
#5.heterogeous
#6.mutable or changable
'''
#eg:1
s1={9,9,89,7,76,8+7j,(8,7,5),"truck",'e'}
print(s1)
#eg:2
s2={5,8,98,[9,0]}
print(s2)#-->error

#eg:3
#min(),max(),len()
s1={8,78,67,'u'}
#add()
s1.add(43)
print(s1)

#update()
s1={8,78,67,'u'}
s1.update([9,0])
print(s1)

#to delete element inside set
#pop()-->to delete one element randomly
s1={8,78,67,'u'}
#s1.pop()
#print(s1)
#remove()
#s1.remove(78)
#print(s1)
#discard()-->the num don't into the set then also it will be execute automatic the set values include 
#s1.discard(976)
#print(s1)

#clear()
l1={}
print(type(l1)) #-->datatype is dict

s1=set() #to create empty set
print(type(s1))

s1={8,9,0}
s1.clear()
print(s1)

del s1
print(s1)

# join the 2 sets
s1={9,8,0}
s2={9.90,"yamuna",'p',3}
#union(-->to combine 2 sets
s3=s1.union(s2)
print(s3)

#intersection()-->to get common elements inside set
s1={4,5,6}
s2={5,6,7,8}
print(s1.intersection(s2))

#difference()--->to get unique element in any set
s1={4,5,6}
s2={5,6,7,8}
#print(s1.difference(s2))
#print(s2.difference(s1))
#print(s1.symmetric_difference(s2))

#isdisjoint(),issubset(),issuperset()
s1={8,9,0}
s2={6,7,5,8,9,0}
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s2.isdisjoint(s1))

#-->prblm-1
s1={1,2,3,4,5,}
s2={3,2,7,8,9}
for val in s1:
    if val in s2:
        str1="its joint set"
print(str1)
'''
#-->dictionary
#eg:1
#d1={1:1000,'a':200,4.5:"hello"}
#marks_stdu1=[english": 76, "maths": 90, "physics": 45}
#print(d1)
#print(len(d1))

#char of dictionary
#1.have to be surrounded by{}
#2.it have to be in the form of key,value pair
#3.it is mutable
#4.duplicate keys are not allowed,duplicate values allowed
#5.it is unindexed
#6.it is ordered
#7.key does not allow muutable datatypes,values allow mutable datatyes
'''
d1={1:100, 2:200, 3:300, 4:400}
#to access element in dictionary
print(d1)
#or
#to access the values,have to use key
print(d1[3])# o/p-->300
 
#sum common functons
#len(),max(),min()
d1={1:100, 2:200, 3:300, 4:400}
print(min(d1))
print(max(d1))
#to find min,max based on values
print(min(d1.values()))
print(max(d1.values()))

#dictionary based functions
#to add element(key and value pair)in dict
d1={1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)

#to replace a value in dictionary
d1={1:100, 2:200, 3:300, 4:400}
d1[2]='mango'
print(d1)

# delete element from dictionary
d1={1:100, 2:200, 3:300, 4:400}
#popitem()-->to deletemlast key vallue pair in dict
d1.popitem()
print(d1)

#pop()
d1={1:100, 2:200, 3:300, 4:400}
d1.pop(2)
print(d1)

#clear(),del
#join 2 dictionay's
#update
d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple", "b":"banana", "c":"cat", "d":"doll"}
d1.update(d2)
print(d1)

#get()-->used to get value from key
d1={1:100, 2:200, 3:300, 4:400}
print(d1.get(90))

#to print all the keys
d1={1:100, 2:200, 3:300, 4:400}
print(d1.keys())
print(type(d1.keys()))

# to print all the values
d1={1:100, 2:200, 3:300, 4:400}
print(d1.values())


#iterating dictionary
d1={1:100, 2:200, 3:300, 4:400} #o/p-->1,2,3,4-->keys
for val in d1:   #o/p-->1,2,3,4
   print(val)

for val in d1.values():  #o/p-->100,200,300,400-->values
    print(val)

#to get both key and values
d1={1:100, 2:200, 3:300, 4:400}
for key,val in d1.items():
    print(key,val)

#prblm-1
n=int(input("enter num of times:"))
integer=[]
float_value=[]
string=[]
for val in range(n):
    value=eval(input("enter the values:"))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print("pls provide data in int,float,string")
print(integer)
print(float_value)
print(string)

#-->prblm-2 return a set of elements present in set A or B,but not both
set1={10,20,30,40,50}
set2={30,40,50,60,70}

print(set1.symmetric_difference(set2))
#or
l1=set1^set2
print(l1)
#or
set3=set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)
'''
#--->prblm-3
l1=[1,2,3,4]#key
l2=["a","b","c","d"]#value

d1={}
d1[l1[0]]=l2[0]
d1[l1[1]]=l2[1]
d1[l1[2]]=l2[2]
d1[l1[3]]=l2[3]
print(d1)
#or
d1={}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)

























