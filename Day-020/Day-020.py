
#In this lesson we learned about Sets in python
"""
------Set----------
A set is a collection which is "unordered" and "unindexed".
In Python sets are written with curly brackets {}.
----Change Items in sets----
Once a set is created, you cannot change its items, but you can add new items

"""
"""
1.How to create empty set
2.How to create set contained on values
3.How to access Items
4.How to add Item/Update Items

"""
#----------1.Create Empty set-----------
thisset={}
print("1.Empty set: {}".format(thisset))
#----------2.Create set contained on values-----------
thisset={"apple","banana","cherry"}
print("2.Create set contained on values: {}".format(thisset))
#Another Example
thisset={"Wejdan","Maram",24}
print("2.Another Example on create set contained on values: {}".format(thisset))
#----------3.Access Items-----------
"""
Because cannot access items in a set by referring to an index, since sets are unordered the items has no index.
but can use loop through the set items using a for loop, 
or ask if a specified value is present in a set, by using the "in" keyword.
"""
print("3.Access to Items using loop:")

for item in thisset:
    print(item)
print("3.Access to Items using in keyword to check specific item:")
print("If Wejdan is present in the set: {}".format("Wejdan" in thisset))

#----------4.How to add Item/Update Items-----------
print("4.How to add Item/Update Items")
thisset.add("Sahar")
print("The set after add new item:{}".format(thisset))

#To add multiple items we use update and we use square brackets []
thisset.update(["Lamar","Raneem",8,7])
print("The set after add new items:{}".format(thisset))



