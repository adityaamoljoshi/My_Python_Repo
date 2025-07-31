a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("You can't divide by Zero")
else:
    print("You ran program successfully")
finally:
    print("Thanks for using this program")