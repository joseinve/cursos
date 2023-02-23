for i in range(1, 11):
    print(i)
print("Ingrese dos numeros")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 1: "))
if num1 > num2:
    for i in range(num2, num1):
        print(i)
elif num2 > num1:
    for i in range(num1, num2):
        print(i)
else:
    print("Los numeros deben ser diferentes")