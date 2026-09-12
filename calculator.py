def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def Division(a,b):
    return a/b

num1 = int(input("Enter frist number: "))
num2 = int(input("Enter second number: "))

print("1, addition")
print("2, subtraction")
print("3, multiplication")
print("4, Division")

choice  = int(input("Choice"))

if choice ==1:
    print("result =" ,add(num1,num2))
elif choice == 2:
    print("reuslt =", subtract(num1,num2))
elif choice ==3:
    print("result =", multiplication(num1,num2))
else:
    print("result=",Division(num1,num2))
