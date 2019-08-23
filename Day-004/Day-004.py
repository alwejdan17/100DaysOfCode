import random as ran

#-------------------------------1.integer numbers in python----------------------------------
"""
a=100
b=-100

"""
nums=[130,160,190,150,180]

total=0
for num in nums:
    print("number =",str(num))
    total+=num

print("total=",str(total),"and Type of this numbers is",str(type(total)))

#-------------------------------2.float numbers in python----------------------------------
"""
a=100.55
b=-100.33

"""
avg=total/len(nums)

print("avg=",str(avg),"and Type of this avg is",str(type(avg)))

#-------------------------------3.complex numbers in python----------------------------------
"""
a=100.55+2j
b=-100.33-2j

"""
complex_num=25+2j
print("complex number=",str(complex_num),"and Type of this  complex_num is",str(type(complex_num)))

#-------------------------------4.convert numbers from int to float and vice versa in python----------------------------------
"""
a=100.55
b=int(a)
c=b
d=float(c)
"""
a=24
b=float(a)
print("convert integer ",str(a)," to float ",str(b))
#---
a=25.3
b=int(a)
print("convert float ",str(a)," to integer ",str(b))
a=25.5
b=int(b)
print("convert float ",str(a)," to integer ",str(b))
#-------------------------------- 5.Generate random numbers between 1 to 5  -------------------------
i=0
while i<=5:
    ran_num=random_nums=ran.randrange(1,6)
    print("random number =",str(ran_num))
    i+=1




