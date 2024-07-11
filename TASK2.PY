
print("CALCULATOR\n\n'+' for Addition\n'-' for Subtraction\n'*' for Multiplication\n'/' for Division\n'%'for Modulo\n'**' for Exponantial")

def task2():
    num1 = eval(input("Enter First number : "))
    num2 = eval(input("Enter second number : "))
    operator = input("Enter the Operation you want to perform : " )

    match operator:
        case _ if operator == "+":
            print(f"{num1} + {num2} = {num1+num2}" )
    
        case _ if operator == "-":
            print(f"{num1} - {num2} = {num1-num2}" )
    
        case _ if operator == "*":
            print(f"{num1} * {num2} = {num1*num2}" )
    
        case _ if operator == "+":
            print(f"{num1} / {num2} = {num1/num2}" )
    
        case _ if operator == "%":
            print(f"{num1} % {num2} = {num1%num2}" )
    
        case _ if operator == "**":
            print(f"{num1} ** {num2} = {num1**num2}" )
    
        case _:
            print("Invalid Operator")


while True:
    task2()
    print("Enter 'ok' if you want to use Again")
    res = input().lower()
    if res != "ok":
        break

print("THANK YOU")