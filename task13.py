num1 = 404
num2 = 404
num3 = 404

if num1 == num2 and num2 == num3 and num3 == num1:
    print(3)
elif num1 == num2 or num2 == num3 or num1 == num3:
    print(2)
else:
    print(0)