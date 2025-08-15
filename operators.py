#interpolatiohonn 
name="jassi"
session="fsd python"
time= 3
print (f"myself {name} is attending {session} session at {time}")
#here in interpolation we use "f"string to combine string and integer, where the placeholder is replaced by actual value.
# if we dont use "f" string, the placeholder remains same will not be replaced by actual value 
print ("myself {name} is attending {session} session at {time}")


#operators (special symbols used to perform operations on variables)
#7 types in operators
#1. arithmatic operators(+,-,*,/,%,//,**)
# +
num1=2
num2=5
print(num1+num2)
#-
print(num1-num2)
#*
print(num1*num2)
#/(quotient)
print(num1/num2)
#%(remainder)
print(num1%num2)
#//(quotient is round off)
print(num1//num2)
#**(square of)
print(num1**num2)

# 2.compound assignment operators(combines assignment operator("=") with arithmatic operations)
# =,+=,-+,*= (we use this for shorter syntax)
num=15
num+=15
print(num)
num-=10
print(num)
num*=1
print(num)

#comparision/relational operators
#used to compare values and returns boolean 
#(==,!=,>,<,>=,<=)
num1=10
num2=15
isEqual=num1==num2
print(isEqual)
isnotEqual=num1!=num2
print(isnotEqual)#isnotEqual
print(num1>num2)#isGreater
print(num1<num2)#isSmaller
print(num1>=num2)#isGreatEqual
print(num1<=num2)#isSmallEqual

num3=10
num4=11
isGreater=num3>num4
print(isGreater)
isSmaller=num3<num4
print(isSmaller)
isGreatEqual=num3>=num4
print(isGreatEqual)
isSmallEqual=num3<=num4
print(isSmallEqual)

# 4.logical operators
#(AND,OR,NOT)
num1=1
num2=2
num3=3
num4=4
print(num1>num3&num2<num4)#AND
print(num1>num3^num2<num4)#OR

# 5. membership operators
#checks if sequence is present or not(in,notin)
text="jagjeeth kaur"
isjpresent='j' in text
print(isjpresent)
islnotpresent="l" not in text
print(islnotpresent)

# 6.identity operators
#compares the objects(is, isnot)
num1=20
num2=40
print(num1 is num2)
print(num1 is not num2)
num2="jassi"
num3="deepu"
print(num3 is num4)
print(num3 is not num4)

# 7. bitwise operators
#used to perform operations on binary bits
#AND,OR,XOR,NOT,<<left shift,>>right shift
a=5
b=3
result=a & b
print(result)
c=1
d=3
result2=a|b
print(result2)
e=10
f=2
result3=a^b
print(result3)
g=3
h=5
result4=a>>b
result5=a<<b
print(result4)
print(result5)