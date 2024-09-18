import math 

def calculator (In1, In2, AWP):
    if AWP == "+":
        return(In1 + In2)
    if AWP == "-":
        return(In1 + In2)
    if AWP == "/":
        return(In1 + In2)
    if AWP == "*":
        return(In1 + In2)
    
In1 = float(input("Enter the first number: "))
In2 = float(input("Enter the second number: "))
AWP = input("Enter an operation (+, -, *, /): ")

result = calculator(In1, In2, AWP)
print("The result is:", result)
