total = 0
userNumber = float(input("Please enter the first number or a negative " + \
                         " number to quit: "))

while userNumber > -1:
    total = total + userNumber
    userNumber =  float(input("Please enter the first number or a negative " + \
                              " number to quit: "))
print()
print( "The  sum of all the number you entered is",total )