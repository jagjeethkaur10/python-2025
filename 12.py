#type conversions and type casting 
#implicit tconversion  & explicit tcasting
#no data loss            data loss may occur 
#implicit t conversion(automatically)
h=100
m=(float(h))
print(m)
#explicit tcasting
a=10
b=12.05
c=(a+b)
print(int(c))
print(type(c))

# statements
# 1. conditional statements (decision making statements)
# decison--> true/false 
# if statements 
num=100
if num>=150:
    print("valid value")
#if_else 
num=100
if num>=150:
    print("valid value")
else:
    print(" invalid value")
#input() function 
#used for interaction with program
name=input("enter ur name:")
print(f"welcome: {name}")
age=int(input("enter ur age:"))
print(f"your age is: {age}")
if age<18:
    print("ur age is less than the required age for voting")
else:
    print("ur eligible for voting")
print("thank you!")
#ternary operator
#conditional operator , used to conside if else statements
#syntax= value_if_true if condition else value_if_true
name=input("enter ur name:")
print(f"welcome: {name}")
age=int(input("enter ur age:"))
print(f"your age is: {age}")
voting_status= "ur age is less than the required age for voting" if age<18 else "ur eligible for voting"
print(voting_status)
#elif ladder/ statement
#used for multiple conditions 
marks=int(input("enter ur marks:"))
if marks>=90:
    print("A GRADE")
elif marks>=80:
    print("B GRADE")
elif marks>=70:
    print("C GRADE")
elif marks>=60:
    print("D GRADE")
elif marks>=50:
    print("E GRADE")
else:
    print("fail")
