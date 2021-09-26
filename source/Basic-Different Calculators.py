# Make a calculator
Number1 = input("Enter a number: ")
Number2 = input("Enter another number: ")
#here need to convert string to number by using int function. int can only be integer
result = int(Number1)+int(Number2)
print(result)
#using float function makes you to be able to use decimals
Number3 = input("Enter X value: ")
Number4 = input("Enter Y value: ")
result = float(Number3)+float(Number4)
print(result)
print("\n")
#Build a better calculator
num1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
elif op == "%":
    print(num1/100)
else:
    print("Invalid operator")
print("\n")