"""
We learned About Dictionaries
1.Create Empty Dictionary
2.Create Dictionary with values
3.Acess to item
4.Change item
5.Display Elements
"""


#---------------1.Create empty dictionary ---------------
thisdic={}
print("1.Create empty dictionary :{}".format(thisdic))

#---------------2.Create dictionary with values---------------

thisdic={"Name":"Wejdan Aljadani","Major":"Computer Science","Age":24}
print("2.Create dictionary with values:{}".format(thisdic))

#---------------3.Acess to the values in dictionary---------------
print("3.Acess to the values in dictionary:")
#with this way if key does not exit then get the error 
print("Name:{} and Major{}".format(thisdic["Name"],thisdic["Major"]))
#print("Job: {}".format(thisdic["Job"]))
#or with get(key)>>if the key does not exit print massege 
print(" With get function Name:{} and Major{}".format(thisdic.get("Name"),thisdic.get("Major")))
print("Job: {}".format(thisdic.get("Job","Does not Exist")))
#---------------4.Change item in dictionary---------------
print("4.Change item in dictionary:")
thisdic["Age"]=25
print("the dictionary after editing on the age{}".format(thisdic))

#---------------5.Display Elements and Keys of dictionary---------------
print("5.Display Elements and Keys of dictionary")
i=1
for key in thisdic:
    print("Key #{}:{}".format(i,key))
    i+=1
i=1
print("-----------------------")
#We have several ways to acess to items in dictionary
for key,item in thisdic.items():
    print("Key #{}:{}".format(i,key))
    print("item :{}".format(item))
    i+=1

print("-----------------------")
for item in thisdic.values():
    print("item :{}".format(item))
print("-----------------------") 
print(thisdic.values())
print("-----------------------") 
print(thisdic.items())