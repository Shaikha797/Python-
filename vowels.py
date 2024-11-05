vowels='AEIOUaeiou'
y=[]
a=input("Enter the word")
for i in a:
    if i in vowels:
        y.append(i)
print(y)
