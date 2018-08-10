num = int(input("enter a number: "))
temp=1
acum =[]
for i in range(1, num+1):
    temp= temp*i
    acum.append(i)
    print(i)

dfgfd=sum(acum)
print(dfgfd)
print(acum)
print(temp)
'''

factorial = 1
if num < 0:
    print("please enter a positive integer")
elif num == 0:
    print("the factorial of 0 is 1")
else:

    print("The factorial of", num, "is", factorial)'''