n=int(input("Enter the current year"))
n2=int(input("Enter the final year"))
for i in range(n,n2):
    if i%4==0 or i%400==0 and i%100!=0:
     print("the year are",i)
