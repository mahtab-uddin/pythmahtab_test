def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x / y
print("Select Operation!->1 for add-> 2 for subtract -> 3 for Multiply ->4 for Devide")
choice = input("Enter your choice between 1/2/3/4: ")
while True:
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter your 1st Number: "))
        num2 = float(input("Enter your 2nd Number: "))
        if choice == '1':
            print(num1, "+", num2,"=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
         print("Invalid Input, please choice between 1-4")
         print("Select Operation!->1 for add-> 2 for subtract -> 3 for Multiply ->4 for Devide")
         choice = input("Enter your choice between 1/2/3/4: ")
         while True:
             if choice in ('1', '2', '3', '4'):
                 num1 = float(input("Enter your 1st Number: "))
                 num2 = float(input("Enter your 2nd Number: "))
                 if choice == '1':
                     print(num1, "+", num2, "=", add(num1, num2))
                 elif choice == '2':
                     print(num1, "-", num2, "=", subtract(num1, num2))
                 elif choice == '3':
                     print(num1, "*", num2, "=", multiply(num1, num2))
                 elif choice == '4':
                     print(num1, "/", num2, "=", divide(num1, num2))
                 break
print("welcome from GitHub")

