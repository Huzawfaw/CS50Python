expression= input("Expression?")

num1,opr,num2 = expression.split(" ")

if opr == "+":
    print(float(num1) + float(num2))
elif opr == "-":
    print(float(num1) - float(num2))
elif opr == "*":
    print(float(num1) * float(num2))
elif opr == "/":
    print(float(num1) / float(num2))
