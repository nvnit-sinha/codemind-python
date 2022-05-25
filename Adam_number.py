def reverse(n):
    rev=0
    while n>0:
        rev=(rev*10)+(n%10)
        n//=10
    return rev
    
def square(n):
    return n*n

s=int(input())
if (square(s)==(reverse(square(reverse(s))))):
    print("True")
else:
    print("False")
    