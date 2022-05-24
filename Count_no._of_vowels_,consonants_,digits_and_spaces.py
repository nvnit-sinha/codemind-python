n=input()
a=0
b=0
c=0
d=0
v="AEIOUaeiou"
for i in n:
    if i.isdigit():
        a=a+1
    elif i==" ":
        b=b+1
    elif i in v:
        c=c+1
    else:
        d=d+1
print("Vowels:",c)
print("Consonants:",d)
print("Digits:",a)
print("White spaces:",b)