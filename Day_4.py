#!--> common functions for list
#L1=[6,7,8,9,0]
#print(len(L1))
#print(max(L1))
#L1=[6,8,9,"p","u"]
#print(max(L1)) #-->error cozmits a combation of list and string
#print(min(L1)) #-->error cozmits a combation of list and string
#l1=[6,7,8,9,0,8.89,-5,0.78]
#index()-->to get index value of specific element
#print(l1.index(9))
#l1=[6,7,8,9,0,8.89,-5,0.78,8,6,9,60]
#count()-->how many num of times an element is repeated
#print(l1.count(6))
#!some functions which is specifically used for list
#to add element inside list
#?insert()-->to add element at specific index position
'''
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
l1.insert(8,"cars")
print(l1)

#? to delete element from list
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
#pop()
l1.pop()
print(l1)

#pop(index_value)-->used to delete element at specific index
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
l1.pop(4)
print(l1)


#remove(element)-->used to delete element directly
#l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
#l1.remove(8.89)
#print(l1)
#clear()-->to complete delete all element in list
#l1.clear()
#print(l1)
#del-->to delete the list
#del (l1) # or del l1
#print(l1)
#?-->join 2 lists
l1=[9,0,8]
l2=["p","o","t",45]
#print(l1+l2)

#or

#extend()-->to combine 2 lists
l1.extend(l2)
print(l1)
'''
#?--->copy()
#l1=[6,7,8,9,3]
#l2=l1.copy()
#print(l2)
#print(l1)

#print(id(l1))
#print(id(l2))
'''
#! diff b/w shallow copy dep copy
#shallow copy
import copy
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

#deep copy
import copy
l1=[8,9,0,[5,6],[3,2,1]]
#print(l1[-1][1])-->ndex nested list

l2=copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
'''
'''
#sort-->ararnge elements in list in ascending or descending order
l1=[9,7,45,0,-6,5,12] #to arange in acscending order
print(l1)
'''
'''
l1=[9,7,45,0,-6,5,12]
l1.sort(reverse=True) #to arange in descending order
print(l1)

l1=['z','i','o','p',9]
l1.sort()
print(l1) #-->error

#list construct
#list ()-->to convert other collection datatype to list
#l3=((8,9,0))
#print(list(l3))

l4=(8,9)
print(list(l4))
'''
#-->nested list
#l1=[8,9,[0,8,7],["p","o",'y'],[8,'t']]
#print(l1[-2][1])
'''
print(l1[3][1])
print(l1[1:4])
print(l1[1:-1])
'''
# to delete "t" from l1
#print(l1[-1]).remove('t')
#print(l1)
#combine these 2 lists ['p','o','y'],[8,'t'] lists in l1 to ['p','o','y',8,'t']
#l1[-2].extend(l1[-1])
#l1.pop(-1)
#print(l1)
#!-->tuple
#char of tuple
#1.tuple have to be surrounded by()
#2.the elements inside tuple are not changable
#3.the elements inside tuple are indexed
#4.the element will execute in order
#5.it is heterogeous
#6.it allo duplicate elements
'''
#eg:
t1=(8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))
'''
#?indexing slicing are all same as list
'''
l1=(8)
print(type(l1)) #int

l1=(8,)
print(type(l1)) #tuple

t1=8,9
print(type(t1)) #tuple

t1=8,
print(type(t1)) #tuple
'''
#len(),min(),max(),index(),count()-->all same as list
#to add element inside tuple--->cannot add
#cannot delete any element from tuple
#join 2 tuples
'''
t1=(8,9,0)
t2=(6,7,8)
print(t1+t2)

#to add all element inside list
#sum
l1=(8,9,6,7)
print(sum(l1))
'''
#sort tuple
#l1=(8,9,7,6)
#print(tuple(sorted(l1)))
#print(tuple(sorted(l1,reverse=True)))
'''
# iterate list and tuples
l1=[9,8,0,6,5]
for i in l1:
    print(i)

#iterate based on index value
l1=[9,8,0,6,5]
for i in range(0,len(l1)):
    print(l1[i])
    #print(l1[0])

#!-->strings
s1='o'
print(type(s1))

s1="hello world"
#to access string
print(s1)
#indexing and slicing-->same as list and tuple
print(s1[0:5])

#--> common functions
#len(),min(),max(),index(),count()
s1="hello world"
print(len(s1))
print(max(s1))
print(min(s1))

#ord-->used to find the ASCII value of a character
s1='a'
print(ord(s1))

#function of string
s1="hello world"
#to convert all characters to upper case
print(s1.upper())

#to convert to lower case
s1="YAMUNA"
print(s1.lower())


#strip()--> to eliminate the space in begining and end of string
s1=" where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

#split()-->to split the words in string based on a character
s1= "where are you?"
print(s1.split())
print(s1.count('e'))

#replace()--> to replace a specific char in the string
s1= "where are you?"
print(s1.replace('r','&&'))

#swapcase()--> to convert capital to small and small to capital at a time
s1= "HEY there"
print(s1.swapcase())

#title()-->to write the string in format of title
s1= 'never giveUP'
print(s1.title())

#capitalize()
s1='never giveUP'
print(s1.capitalize())

#join the strings
#s1="hello"
#s2="world"
#print(s1+s2)
'''
s1= '''how are you
iam fine
hey there
'''
# splitlines()--> used to split the string based on lines
#print(s1.splitlines())
'''
#find()-->to find the index based ona character
s1="hello world"
print(s1.find('z'))
print(s1.index('h'))

#join()-->
l1= ["hey", "there"]
print(" ".join(l1))

l1= ["hey", "there"]
print(" ".join(l1))
print("".join(l1))

s1= "Welcome to all"
print(s1.endswith('l'))
print(s1.isdigit())

s1="67"
print(type(s1))
print(s1.isdigit())

#print the string in reverse manner
s1= "Welcome to all"
print(s1[ : :-1])

#eg:1
# wap to find the number of lower case letters
s1= "HEY there you aRE"
count = 0
for i in s1:
    if i.islower():
        count+=1
print("The total num of lower case letters:",count)

#eg:2 r--->"$"
s1= 'restarter'
fst=s1[0]
bal=s1[1:]
txt=bal.replace(fst,"$")
print(fst+txt)
'''
s1="Lorem Ipsum is simply dummy text of the printing and type setting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,but also the leap into electronic type setting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,and more recently with desktop publishing software like Aldus Page Maker including versions of Lorem Ipsum."
characters=len(s1)
print(characters)
words=s1.split(" ")
print(len(words))
sentenses=s1.split('.')
for val in sentenses:
    if val=='':
        index=sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))
#print(s1.count(" "))
space=0
for val in s1:
     if val ==" ":
         space=space+1
print(space)











