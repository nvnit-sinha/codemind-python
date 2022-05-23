s=input()
k=0
for i in s:
    if i.isdigit():
        k=k+1
if k>0:
    print("Contains",k,"digit")
else:
    print("Doesn't contain digit")