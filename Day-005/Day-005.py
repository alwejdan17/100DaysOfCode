

x,y,z="apple","orange","limon"

basket=x+y+z

print("String before spliting  : ",basket)


print("String after spliting  : ",basket[0:len(x)],",",basket[len(x):len(basket)-len(z)],",",basket[len(basket)-len(z):len(basket)])