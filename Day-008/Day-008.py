


print("""String functions in python:\n
         1.strip >>removes any whitespace from the beginning or the end
         2.len   >>length of string
         3.lower >>string in lower case
         4.upper >>string in upper case
         5.replace>>replaces a string with another string
         6.split  >>splits the string into substrings if it finds instances of the separator
""")

name=" Wejdan  ALjadani  "
print("----- Name:",name,"-----\n")
print("-----1.strip function-----:","\n")
print("----- Name:",name.strip(),"-----\n")
print("-----2.len function-----:",len(name),"\n")
print("-----3.lower function-----:",name.lower(),"\n")
print("-----4.upper function-----:",name.upper(),"\n")
print("-----5.replace function-----:",name.replace("ALjadani","Alharbi"),"\n")
print("-----6.split function-----:",name.split(" "),"\n")


