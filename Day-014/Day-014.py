

List_1=["Python","R","Matlab","Java","C#"]
#1.return 3 items from list
print("programming languages which used in AI,ML,DL :",List_1[:3]) 

#2.check if item exists
if "Python" in List_1:
    print("Python the best language for AI,ML,DL :)")
else:
    print("all these language good for AI,ML,DL but not the best :(")
#3. repeat items in list
List_2=["Python"]*2
print("List #2",List_2)

#4.combine two lists together
list_3=List_1+List_2
print("List #3",list_3)
#--------------------------
lis1=[1,2,3,4,5,6,7]
lis2=[1.2,3.4,5.5,6.6,10.4]
lis3=lis1+lis2
print("combine two lists together",lis3)