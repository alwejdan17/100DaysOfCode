#4.Logical Operators
#  and, or, not
x=25
y=30
print("--------4.Logical Operators---------\n")
print("x = {0} , and y = {1}\n".format(x,y))
#-----------and -----------
print("-------- and ---------\n")
print("{0}>20 and {1}<50 result is {2}\n".format(x,y,x>20 and y<50))
print("{0}<20 and {1}<50 result is {2}\n".format(x,y,x<20 and y<50))
#-----------or -----------
print("-------- or ---------\n")
print("{0}<20 or {1}>20 result is {2}\n".format(x,y,x<20 or y>20))
print("{0}<25 or {1}<30 result is {2}\n".format(x,y,x<25 or y<30))
#-----------not -----------
print("-------- not ---------\n")
print("reverse of {0}<25 or {1}<30 {2}\n".format(x,y,not(x<25 or y<30)))

#5.Identity Operators
print("--------5.Identity Operators---------\n")
# is, is not
#-----------is -----------
print("-------- is ---------\n")
a=x #a refrence to same location in memory with x
z=25
print("a = {0}, x = {1} ,then a is x ? {2}\n".format(a,x,a is x))
print("z = {0}, x = {1} ,then z is x ? {2}\n".format(z,x,z is x))
print("x = {0}, y = {1} ,then x is y ? {2}\n".format(x,y,x is y))
#-----------is not-----------
print("-------- is not ---------\n")
print("a = {0}, x = {1} ,then a is not x ? {2}\n".format(a,x,a is not x))
print("z = {0}, x = {1} ,then z is not  x ? {2}\n".format(z,x,z is not x))
print("x = {0}, y = {1} ,then x is not y ? {2}\n".format(x,y,x is not y))
#6.Membership Operators
# in ,not in
print("--------6.Membership Operators---------\n")
name="Wejdan Aljadani"
first_n="Wejdan"
last_n="aaa"
print("full name : {0} , first name : {1} ,then {1} in {0} ? {2}\n".format(name,first_n,first_n in name))
print("full name : {0} , last name : {1} ,then {1} in {0} ? {2}\n".format(name,last_n,last_n in name))
#7.Bitwise Operators
#& ,|,^ ,~,>>,<<
print("--------7.Bitwise Operators---------\n")
print("x = {0} ,not x is  ? {1}\n".format(x,~x))
print("x = {0} ,x AND 2 is ? {1}\n".format(x,x&2))
print("x = {0} a ={1} ,x XOR a is ? {2}\n".format(x,a,x^a))
print("x = {0} a ={1} ,x OR a is ? {2}\n".format(x,a,x|a))
print("x = {0} ,x shift left 2 is ? {1}\n".format(x,x<<2))
print("x = {0} ,x shift right 2 is ? {1}\n".format(x,x>>2))