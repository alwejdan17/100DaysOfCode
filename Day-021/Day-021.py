

#Sets-2
"""
1.Get The length of a set
2.Remove Specific Item
3.Remove random item in the set
4.Remove all items in the set
5.Create Set using set() Constructor
6.Remove the set completely
"""
thisset={"apple","banana","orange","cherry","banana","apple"}
print("Set :{}".format(thisset))
#--------1.Get The length of a set---------
print("1.Get The length of a set :{}".format(len(thisset)))

#--------2.Remove Specific Item---------
#------using remove(arg)------
#If the item to remove does not exist, remove() will raise an error!.
print("2.Remove Specific Item")
thisset.remove("banana")
print("The set after remove banana :{}".format(thisset))
#Or Using discard(arg)
#If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banana")
print("The set after remove banana :{}".format(thisset))

#--------3.Remove random item in the set---------
print("3.Remove random item in the set")
removed_item=thisset.pop()
print("The item which removed is {}".format(removed_item))
print("The set after removed item :{}".format(thisset))

#--------4.Remove all items in the set---------
new_set=thisset.copy()
new_set.clear()
print("4.Remove all items in the set:{}".format(new_set))

#--------5.5.Create Set using set() Constructor---------
new_set2=set(("apple","banana","orange"))
print("5.Create Set using set() Constructor :{}".format(new_set2))

#--------5.Remove the set completely---------
print("6.Remove the set completely:")
print("The set before deleting :{}".format(thisset))
print("The set after deleted")
del thisset
print(thisset)

