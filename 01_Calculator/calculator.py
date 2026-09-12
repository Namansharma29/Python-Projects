def add(a,b):
    return a+b
def subtract(a,b):
    return a+b

num1 = int(input("Enter frist number: "))
num2 = int(input("Enter second number: "))

print("1, add")
print("2, subtract")

choice  = int(input("Choice"))

if choice ==1:
    print("result =" ,add(num1,num2))
elif choice == 2:
    print("reuslt =", subtract(num1,num2))+
