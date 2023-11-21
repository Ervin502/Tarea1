num1=int(input("Ingrese un numero: "));
num2=int(input("Ingrese otro numero: "));
num3=int(input("Ingrese otro numero: "));
if num1 > num2 and num1 > num3:
    mayor = num1;
elif num2 > num1 and num2 > num3:
    mayor = num2;
else:
    mayor = num3
print("El numero mayor es:", mayor);