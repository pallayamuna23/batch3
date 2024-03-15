#day-5
#--->common funtions for list
'''
l1 = [6,7,8,9,0]
print(len(l1))
print(max(l1))
print(min(l1))
l1 = [6,8,9,"p","u"]
print(max(l1)) #-->error coz its a combination of list and string
print(min(l1)) #-->error coz its a combination of list and string
cprint(max(l1)) #-->error coz its a combination of list and string
'''
'''
l1 = [6,7,8,9,0,8.89,-5,0.78]
#index()#-->to get index value of specific element
print(l1.index(9))

l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
#count()#-->how many num of times an element is repeated
print(l1.index(6))
#some funtions which is  specifically used for list
#to add element inside list
#insert(index_value,element)-->to add element at specific index posit
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
l1.insert(2,"cars")
print(l1)

#to delete element from list
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
#pop()-->last element wiill be deleted
l1.pop()
print(l1)
'''
'''
#pop(index_value)-->used to delete element at specific index
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
l1.pop(4)
print(l1)
#remove(element)--> used to delete element directly
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
l1.remove(8.89)
print(l1)
'''
'''
#del--> to delete the list
#del l1 #or del(l1)
print(l1)
'''
'''
#-->join 2 lists
l1 = [9,0,8]
l2 = ["p","o","t",34]
print(l1+l2)
#or
#extend()--> to combine 2 lists
l1.extend(l2)
print(l1)
#-->copy ()
l1 = [6,7,8,9,3]
l2 = l1.copy()
print(l2)
print(l1)
print(id(l1))
print(id(l2))
#diff between shallow copy and deep copy
#shollow copy
import copy
l1 = [8,9,0,[5,7],[3,2,1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)
#deep copy---> used to copt the list with nested list
import copy
l1 = [8,9,0,[5,7],[3,2,1]]
print(l1[-1][1])
l2 = copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
'''
'''
#sort---> arrange elements in list in asending or descending order
l1 = [9,7,45,-6,5,12]
l1.sort()
print(l1)
l1.sort(reverse=true)
print(l1)
l1 = ['z','i','o','p',9]
l1.sort()
print(l1)
'''
'''
#list constructor
#list()--> to conver other collection datatype to list
l3 = ((8,9,0))
print(list(13))
l4 = (8,9)
print(list(l4))

#-->nested list
l1 = [8,9,[0,8,7],["p","o","y"],[8,'t']]
print(l1[-2][1])
print(l1[1:4])
print(l1[1:-1])
#to delete "t" from l1
l1[-1].remove('t')
print(l1)
'''
'''
#combine these ["p","o","y"],[8,'t'] lists in l1 to ["p","o","y",8,'t']
l1 = ["p","o","y",8,'t']
print(l1)
#--->tuple
#char of tuple
#1.)tuple have to be surounded by()
#2.) the elements inside tuple are not changable
#3.)the elements inside tuple are indexed
#4.)the elements will execute in order
#5.)it is heterogenous
#6.)it allow duplicate elements

#eg-1
t1 = (8,8,9,6,5.78,[9,0],"hey sneha",9+6j)
print(t1)
print(type(t1))
#indexing, slicing are all same as list
l1 = (8)
print(type(l1))
l1 = (8,)
print(type(l1))
t1 = 8,9
print(type(t1))
t2 = 8,
print(type(t2))
len(),min(),max(),index(),count()
'''
'''
#to add element inside tuple
#cannot delete any element from tuple
#jpin 2 tuples
t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)
#to add all element inside list
#sum()
l1 = (8,9,7,6)
print(sum(l1))
'''
'''
#sort tuple
t1 = (8,9,0,89,70)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=true)))
'''
'''
#iterate l;ist and tuples
l1 = [9,8,0,6,5]
for i in l1:
    print(i)
#iterate based on index value
l1 = [9,8,0,6,5,8,56]  
for i in range(0,len(l1)):
    print(i)

print(l1[2])
'''
'''

#--->strings
s1 ='0'
print(type(s1))
s1 = "u"
print(type(s1))
s1 = "hello world"

#to access string
print(s1)
#indexing and slicing-->same as list and tuple
#print(s1[0,5])
#common functions
#len(),min(),max(),index(),count()
s1 = "hello world"
print(len(s1))
print(max(s1))
print(min(s1))
#ord()---->used to find the ASCII value of a charcter
s1 = 'u'
print(ord(s1))
#functions of string
s1 = "hello world"
#to convert all charters to upper case
print(s1.upper())
#to conver to lower case
s1 = "HFREDiou"
print(s1.lower())
'''
'''
#strip()---> to elimante the space in beginning and end of string
s1 = "how are you rio bangaram"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())
s1 = " hey bidda"
print(s1.split("r"))
#replace()--> to replace a specific char in the string
s1 = "sneha bangaram"
print(s1.replace('r','&&'))
#swapcase()--> to convert capital to small and small to capital at
s1 = "rey"
print(s1.swapcase())
#title()-->to write the string in format of title
s1 = "bujji"
print(s1.title())
#capitlized()
s1 = 'never giveup'
print(s1.capitalize())
#join the string
s1 = "sneha"
s2 = "pavan kalyan"
print(s1+s2)
s1 = '''


'''
#splitlines()-->used to split the string based on lines
print(s1.splitlines())
#find()
s1 = "hello sneha"
print(s1.find('z'))
print(s1.index('z'))
print(s1.index(4))
'''
'''
#join()-->
l1 = ["hey","there"]
print(" ".join(l1))
print("$".join(l1))
s1 = "welcome to all"
print(s1.endswith('1'))
print(s1.startswith('w'))
'''
#print the string in reverse manner
s1 = "welcome to all"
print(s1[::-1])
#---.eg-1
#wap to find the number of lower case letters
s1 = "hey there you are"
count=0
for i in s1:
    if i.islower():
        count+=1
print("the total num of lower case letters:",count)
#--->eg-2 r-->"$"
s1 = 'restarter'
s1 = "IMAGIN"
fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst,"$")
print(fst+txt)
#--->eg-3
s1 = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
char = len(s1)
print(char)
words = s1.split(" ")
print(len(words))
sentenses = s1.split('.')
for val in senteses:
    if val =='':
        index = senteses.index('')
        sentenses.pop(index)
print(len(senteses))


                                       


