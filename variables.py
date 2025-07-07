#variables

value_num = 10
value_rating= 4.5
value_name = "jassi"
#we use id to get the memory location of the particular value which we are finding 
#id=unique identity , memory address 
#variables follow the same identifiers rules 

print(id(value_name))
print(id(value_rating))
print(id(value_num))

value_newrating= 4.5
print(id(value_newrating))

#if the value is same the memory address is also same , it doesn't hold a new memory address for same values.
#so variables in python are immutable type of data (num, decimal, digits,simple text)

#muttable type of data are 
#:lists
#lists are mutiple no. values 

list1=[1,2,3]
list2=[1,2,3]
list3=[6,4,5]
print(id(list1))
print(id(list2))
print(id(list3))

#lets see which datatypes are the values 
#type function defines what type of data type is the particular value 

print(type(value_num))
print(type(value_rating))
print(type(value_name))

#python is 100% object oriented language becz python follows all :
#1.classes
#2.objects
#3.methods
#4.polymorphism
#5.inheritance
#6.encapsulation
#7.abstraction

#ouput variables (simply just giving the output value)

msg="python is great"
print(msg)

x="python" #string
y="is" #string
z="great" #string
# this term is called concatenation where strings are added ,using operator "+"
print(x+y+z)

 # this cannot be done becz concatenation is done between strings only not string nd int 
#print(x+y+z+version)

version= 3
version_new= 5
print(version+version_new)

#we can make this work by using comma 
print(msg,version_new)