a=input("Enter the string")
b=()
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
        print("count of characters",str(b))
            
