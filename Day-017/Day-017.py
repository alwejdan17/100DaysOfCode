
#Tuple-2

langs=("Python","PHP","Java","Ruby","C#","C++","R")
#---------- 1.Check if Item Exists -------------
print("1.Check if Item Exists")
if "Python" in langs and "R" in langs:
    print("You can use any one to studying and Practicing on AI and DS:)")
else:
    print(" OHHHH Sorry..... :(")


#---------- 2.Repeat Item -------------
#Because we can not repeat item in tuple after we created it ,but we can create another tuple and repeat item in it

tuple_python=("Python",)*3
print("2.Repeat Item",tuple_python)
#---------- 3.(+) Operator in Tuple -------------

new_tuple=tuple_python+langs
print("3.Combine two tuples together",new_tuple)

#---------- 4.Tuple Length using len(tuplename)-------------
print("4.Length of langs:",len(langs))

#---------- 5.Create Tuple using the tuple() Constructor  -------------

langs2=tuple(("Python","R"))
print("5.Create Tuple using the tuple() Constructor:",langs2)

#---------- 6.Use tuplename.count(argument) function -------------

print("6.Count number of Python in new_tuple:",new_tuple.count("Python"))

#---------- 7.Use tuplename.index(number of index)function -------------
#Search on item or element and return the first or smallest index
print("7.Search on Python and return the fisrt index: {}".format(new_tuple.index("Python")))


#Extra example for combine two tuples together
x=(5,10,15,20,25,30)
print("X ={}".format(x))
x=x+(40,)
print("X after combine x tuple with new tuple ={}".format(x))