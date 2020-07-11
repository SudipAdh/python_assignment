# WAP to take the user input and devide it by certain integer. But what if user input 0 . Handle the exception.

x=int(input("Enter number: "))
y=2

try:
    y/x
except:
    print("Division by 0 is not possible")
else:
    print(y/x)
