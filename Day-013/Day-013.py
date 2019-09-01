
list1=[]
print("Create list1:  {}".format(list1))

list1.append("Python")
list1.append("Django")
print("Added items to list1:  {}".format(list1))

list1[1]="C#"
print("Change item #2 in list1:  {}".format(list1))

list1.append("asp.net")
print("Added item to list1:  {}".format(list1))
del list1[2]
print("Delete item from list1:  {}".format(list1))

list2=[1,2,3,5,6,7,8,9,10]
print("Create list2:  {}".format(list2))
print("print first 3 items in list2:  {}".format((list2[0:3])))


list2.append(13.5)
list2.append(20.5)
print("Added  float number to list2:  {}".format(list2))
#used build-in function with list contains on numbers
print("Maximum value in list2:  {}".format(max(list2)))
print("Minimum value in list2:  {}".format(min(list2)))
print("Mean value in list2:  {}".format(sum(list2)/len(list2)))

# print all item in list 
list1.append("Java")
list1.append("Javascript")
print("Added items to list1:  {}".format(list1))
print("print all items in list1")
for item in list1:
    if item=="Python":
        print(item ,"So COOOOOOOL")
    else:
        print(item)


