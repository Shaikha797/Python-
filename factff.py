first=0
second=1
N=int(input("Enter the number"))
for a in range(1,N):
    third=first+second
    print(third)
    first,second=second,third
