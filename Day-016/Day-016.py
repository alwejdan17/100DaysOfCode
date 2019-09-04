
#In this lesson we learned about Tuple
"""
******************NOTE*********************
we can not >>Add and changing(editing or remove)items in Tuple  
"""
#-----1. Create Tuple------
Gender=("Female","Male")
#age=(24,)
age=(25,24)
Category=("18-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60 and above")
#-----2.Acess to specific item in Tuple by using index------
print("Gender #1: ",Gender[0])
print("age:",age[0])
#-----3.Acess all items in Tuple by using loop------
for item in Gender:
    print("The gender is:",item)
#-----4.Acess to some items in Tuple by using index------
print("items #1 and #2",Gender[0:2])
print("Category:",Category[1:5])
#-----5.del all items in Tuple by using del------
del Gender 
print(Gender)
