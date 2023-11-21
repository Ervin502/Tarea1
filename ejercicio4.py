num1=int(input("Ingrese un numero: "));
num2=int(input("Ingrese otro numero: "));
num3=int(input("Ingrese otro numero: "));
suma=num1+num2+num3;
total=suma//3;

if total%2==0:
    mensaje="El promedio de los numeros es par: ",total;
else:
    mensaje = "El promedio de los numeros es impar: ", total;
print(mensaje);

