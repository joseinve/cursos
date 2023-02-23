print("Ingrese dos numeros")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
if num1 == num2:
    print("Los numeros deben ser diferentes")
elif num1 > num2:
    for i in range(num2, num1):
        if i % 2 != 0:
            print(i)
else:
    for i in range(num1, num2):
        if i % 2 != 0:
            print(i)
