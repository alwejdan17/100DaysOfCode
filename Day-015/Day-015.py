

#a >>it is list
lan=["Arabic","English","Urdu","Hindi","Korean","Persian"]
#-------------1.len(a)-------------
print("------List #1------\n\n",lan)
print("Length = ",len(lan))

#-------------2.a.append(item)-------------
lan.append("Chinese")
lan.append("English")
#-------------3.a.insert(index,item)-------------
lan.insert(1,"Arabic")
print("After insert items into list :\n",lan)
#-------------4.a.remove(item)-------------
lan.remove("Persian")
print("After remove item (Persian) from list :\n",lan)
#-------------5.a.pop()>>remove last item OR a.pop(index)>>remove specific item-------------
lan.pop(1)
print("After pop item (by using index) from list :\n",lan,"\n")
# ---------Copy a list------------
#a2=a>>a2 refrence to a <so if I do any change on a ,a2 will be change
print("------Copy a list Using copy function or list constructor------")
#-------------6.a2=a.copy()-------------
lan2=lan.copy()
print("------List #2 by using copy function------\n\n",lan2,"\n")
#-------------7.list() Using list constructor-------------
lan3=list(lan)
print("------List #3 by using list constructor------\n\n",lan3,"\n")
#---------8.a.clear() Remove all items ----------
lan2.clear()
print("------Remove all items in list#2------\n",lan2)
#------9.list(a3) >>Create List Using list constructor-------
print("------Create list using list constructor------")
list_items=("Arabic","English")
lan4=list(list_items)
print("------List #4-----\n\n",lan4)
#-------------10.a.count(item) >return number which is match with (item)-------------
print("Number of English words in list#1 =",lan.count("English"))
#-------------11.a.revere()>>reverse list and update it-------------
lan.reverse()
print("Reverse items in list#1: ",lan)
#-------------12.a.sort()>>sort the list and update it-------------
lan.sort()
print("Sort items in list#1: ",lan)