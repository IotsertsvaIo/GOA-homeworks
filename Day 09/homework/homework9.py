num = int(input("Please enter your number: "))

if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")

num = int(input("please enter number: "))

print(num % 2 == 0 and num % 4 == 0)


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)
