

a="Please, I want {} sandwishes and {} donutes "
print("String before modification :",a,"\n")
#1. use replace function
a=a.replace("I","We")
print("String after replace I with We :",a,"\n")
#2. Use format function
print("String after formatting :",a.format(5,7),"\n")
# 3. Capitalize "a"
a=a.replace("a","A")
print("String after capitalize letter a :",a.format(5,7),"\n")