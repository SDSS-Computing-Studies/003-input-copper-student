#! python3


result = ""
classMembers = ("John","Emily","Harnoor","Bob","Spencer","Catrina")
name = input("Who are you looking for?")
for i in classMembers:
    if name == i:
        result = i
        break

output = result + " is in the class" if result != "" else "They are not in the class"
print(output)
