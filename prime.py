x=[2,3,4,5]
print("the greatest",max(x))
c=max(x)
f='prime'
print("position:",(x.index(max(x))+1))
for i in range (2,c):
 if(c%i==0):
    f='not prime'
    break
print(f)
