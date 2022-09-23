a=int(input())
b=int(input())
# a,b=map(int,input().split())
temp=a
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
        
if sum==b:
    print("Amicable")
else:
    print("Not Amicable")
    