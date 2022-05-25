n=int(input())
temp=n
k=0
for i in range(1,n):
    if n%i==0:
        k=k+i
if k>temp:
    print("True")
else:
    print("False")