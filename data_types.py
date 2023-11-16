  #integer
x=5
  #float
y=8.9
  #complex
z=7+2j
print(x)
print(y)
print(z)
print("Type of x is:",type(x))
print("Type of y is:",type(y))
print("Type of z is:",type(z))

#Strings
str1=("Strings are a part of Sequences")
#string with triple quotes
str2=('''Strings
with
triple
quotes
allow
multiple
lines''')
print(str1)
print(str2)
#Accessing elements in a string
a=str1[0]
print(a)
b=str1[0:5]
print(b)
c=str2[-1]
print(c)

#Lists and accessing elements
list1=[1,2,3,4,5]
print(list1[2])
print(list[-1])
#nested lists
list2=[[1,2],[2,3]]
print(list2)

#Tuples
tup1=('my','name','is','madhav')
#values cannot be changed
#tup1[2]=4 will give an error
#tuple using list
tuplist=[1,2,3,4]
tuple2=tuple(tuplist)
print(tuple2)
#if there are no paranthesis, elements are taken to form a tuple
tup3=1,2,3
print(tup3)
#nested tuples
tup4=(('this','is'),('nested','tuple'))
print(tup4)
print(tup3[2])
print(tup3[-1])

a=0
b=None
c=1
d=20
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))

print(type(true))
print(type(false))

set1={1,2,3,4}
print(set1)
#sets using set() with mixed value
set2=set(1,'mixed',2,'values',3)
print(set2)
#set using list
setlist=[1,2,3,4]
set3=set(setlist)
print(set3)
#indexing not supported in sets have to use loops to access elements
set4=[1,2,3,4,5,6,7]
for i in set4:
  print(i,end=" ")
#checking specific element
print(1 in set4)

dict1={'name':'madhav','major':'ai','lang':'python'}
print(dic1)
#dict with mixed keys
dict2={'key':'value',1:[1,2,3,4]}
print(dic2)
#using dict method
dict3=dict({'key1':'val1','key2':'val2'})
print(dict3)
#dict with each item as pair
dict4={[(1,'one'),(2,'two')]}
print(dict4)
#keys cannot be same
#accessing value fromn key
print(dict1['name'])
#using get function
print(dict2.get(1))
