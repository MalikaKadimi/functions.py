#functions in python
#string  transform functions
#capitalize
message = "hi, how are you?"
print(message.capitalize())

#title
name = "malika kadimi29"
print(name.title())

#upper
name = "malika kadimi29"
print(name.upper())

#lower
name = "malika kadimi29"
print(name.lower())

#casefold
name = "MALIKA"
print(name.casefold())

#swapcase
name = "MALIKA"
print(name.swapcase())

name = "MALIKA"
print(name.swapcase())

#string check functions

#isnumeric
a = "12234"
print(a.isnumeric())

#isalnum
a = "malika29"
print(a.isalnum())
b = "kadimi"
print(b.isalnum())

#isdigit
a = "235"
print(a.isdigit())

#isasscii
a = "G4G"
print(a.isascii())

#isupper
a = "malika kadimi29"
print(a.isupper())

#islower
a = "malika kadimi2"
print(a.islower())

#isspace
a = "malika kadimi2 "
print(a.isspace())

b = "malika"
print(b.isspace())

#isidentifier
a = "malika kadimi29"
print(a.isidentifier())

#isprintable
a = "malika kadimi2"
print(a.isprintable())

#istitle
a = "Hello, Welcome!"
print(a.istitle())

#string len function
name = "malika kaimi229"
print(len(name))

#string search functions

#index
email = "malika29"
print(email.index("2"))
print(email.index("9"))

#rindex
email = "malika kadimi25@gmail.com"
print(email.rindex("5"))
print(email.rindex("@"))

#find
email = "malika kadimi25@gmail.com"
print(email.find("3"))
print(email.find("b"))

email = "malika kadimi2m@gmail.com"
print(email.find("2"))
print(email.find("@"))

#rfind
email = "malika kadimi2@gmail.com"
print(email.rfind("2"))
print(email.rfind("@"))

#startswith
email = "malika kadimi2@gmail.com"
print(email.startswith("malika"))
print(email.startswith("25"))

#endswith
email = "malika kadimi25@gmail.com"
print(email.endswith("maliaka"))
print(email.endswith(".com"))

#CRUD functions
#create/add data
#append
lst = []
lst.append("malika")
lst.append("25")
print(lst)

#insert
names = ["a", "b", "c"]
names.insert(2, "malika")
print(names)

#read
names = ["a", "b", "c"]
print(names.index("b"))

#count
names = ["a", "b", "c", "a"]
print(names.count("a"))

#extend
names = ["a", "b", "c"]
num = ["1", "2", "3"]
names.extend(num)
print(names)

#remove
names = ["malika", "priyam", "25"]
names.remove("priyam")
print(names)

#pop with index
names = ["priyam", "mali", "25"]
names.pop(2)
print(names)

#pop without index
names = ["malika", "priyam", "25"]
names.pop()
names.pop()
print(names)

#clear
names = ["bhavya", "malika", "25"]
names.clear()
print(names)

#sort
num = [8, 3, 5, 2, 6, 1]
num.sort()
print(num)

#reverse
num = [8, 3, 5, 2, 6, 1]
num.reverse()
print(num)