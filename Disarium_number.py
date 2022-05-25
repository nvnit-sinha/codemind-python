n=int(input())      #n=175          
r=0      
temp=n
p=len(str(n))       #p=3            
while n>0:                          #n=17>0
    rem=n%10        #rem=5          #rem=7
    s=rem**p        #s=5**3         #s=7**2
    r=r+s           #r=0+125        #r=174
    n//=10          #n=17           #
    p=p-1           #p=2
if temp==r:
    print("True")
else:
    print("False")