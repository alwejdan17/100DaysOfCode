
# In this day we learned about format function in string
#we can format string and combine with numbers using format function
Name="Wejdan"
age=24
major="Computer Science"
print("My name is {},I'm {} years old,and My major is {}\n".format(Name,age,major))
print("My name is {0},I'm {1} years old,and My major is {2}\n".format(Name,age,major))
#-------------------------------------
print("My name is {1},I'm {0} years old,and My major is {2}\n".format(age,Name,major))

#----In another example I used dict 
person_Info={"name":"WEJDAN","age":24,"major":"Computer Science"}
#in this example, I was passed One parameter which is person_Info (dict) 
# then I specified which key I want in each {} 
print("My name is {0[name]},I'm {0[age]} years old,and My major is {0[major]}\n".format(person_Info))


