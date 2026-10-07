n=int(input("Enter the Number: "))
ans=1
if n<0:
    print("Can't determine the factorial for",n)    
else:
    for i in range(2,n+1):
        ans*=i
print("The factorial of",n,"is",ans)

