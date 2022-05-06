import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
j=math.sqrt((s*(s-a)*(s-b)*(s-c)))
print("%.2f"%j)