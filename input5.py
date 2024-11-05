names=[]
list=[]
for i in range(5):
 name=input("Enter the name:")
 names.append(name)
 for name in names:
     if (name[0]=="A" or name[0]=="a"):
      list.append(name)
      names.remove(name)
print("name start with A :",list)
print(names)
