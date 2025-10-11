#•	Basic Calculator CLI – Take two numbers and an operator (+, -, *, /), output result.
def calculator(num1,num2,operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Division with 0 is not possible."
            else:
                return num1 / num2
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operator=input("Enter the operator(+, -, *, /): ")
result= calculator(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

#•	Build a simple calculator using Python.
'''
def calculator(num_1, num_2, operator):
    match operator:
        case "+":
            return (num_1 + num_2)
        case "-":
            return (num_1 - num_2)
        case "*":
            return (num_1 * num_2)
        case "/":
            if num_2 == 0:
                return False
            else:
                return (num_1 / num_2)
        case _:
            return False
            

equation = list(map(str, input("Enter the equation: ").split()))
result = calculator(int(equation[0]), int(equation[2]), equation[1])
if result:
    print(f"{equation[0]} {equation[1]} {equation[2]} = {result} ")
else:
    print("Please enter the valid equation.")
'''       