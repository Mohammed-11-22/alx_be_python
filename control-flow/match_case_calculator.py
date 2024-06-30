num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
operation=input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        r=num1+num2
        print(f"the result is : {r}.")
    case "-":
        r=num1-num2
        print(f"the result is : {r}.")
    case "*":
        r=num1*num2
        print(f"the result is : {r}.")
    case "/":
        if num2 != 0:
            r = num1 / num2
            print(f"The result is {r}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation")