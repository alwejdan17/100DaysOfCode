

#-------------- String before Casting ---------------------
x="5.5"
type_x=type(x)
y="5"
type_y=type(y)
#-------------- int before Casting ------------------------
z=10
type_z=type(z)
#-------------- float before Casting ------------------------
h=10.8
type_h=type(h)
#----------------print all variables before Casting -----------------------------
print("-------- Before Casting ------ \n")
print("X is ",x,"and Type of X is :",str(type_x))
print("Y is ",y,"and Type of Y is :",str(type_y))
print("Z is ",z,"and Type of Z is :",str(type_z))
print("H is ",h,"and Type of H is :",str(type_h),"\n")

#----------------- 1.Casting String to float ---------------------
x1=float(x)
type_x1=type(x1)

print("---- 1.Casting string to float ----\n")
print("X is ",x,"and Type of X is :",str(type_x))
print("X1 is ",x1,"and Type of X1 is :",str(type_x1),"\n")

#----------------- 2.Casting String to int ---------------------
y1=int(y)
type_y1=type(y1)
print("---- 2.Casting string to int ----\n")
print("Y is ",y,"and Type of Y is :",str(type_y))
print("Y is ",y1,"and Type of y1 is :",str(type_y1),"\n")


#----------------- 3.Casting int to str ---------------------
z1=str(z)
type_z1=type(z1)
print("---- 3.Casting int to str ----\n")
print("Z is ",z,"and Type of Z is :",str(type_z))
print("Z1 is ",z1,"and Type of Z1 is :",str(type_z1),"\n")

#----------------- 4.Casting int to float ---------------------
z2=float(z)
type_z2=type(z2)
print("---- 4.Casting int to float ----\n")
print("Z is ",z,"and Type of Z is :",str(type_z))
print("Z2 is ",z2,"and Type of Z2 is :",str(type_z2),"\n")

#----------------- 5.Casting float to int ---------------------
h1=int(h)
type_h1=type(h1)
print("---- 5.Casting float to int ----\n")
print("H is ",h,"and Type of H is :",str(type_h))
print("H1 is ",h1,"and Type of H1 is :",str(type_h1),"\n")


#----------------- 6.Casting float to str ---------------------
h2=str(h)
type_h2=type(h2)
print("---- 6.Casting float to str ----\n")
print("H is ",h,"and Type of H is :",str(type_h))
print("H2 is ",h2,"and Type of H2 is :",str(type_h2),"\n")

#----------------------------------------------------------







