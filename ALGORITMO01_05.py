#Declarar
A=0
B=0
C=0
delta=0
x1=0
x2=0
#inicio
A = float(input("Qual o valor de A?"))
B = float(input("Qual o valor de B?"))
C = float(input("Qual o valor de C?"))  
delta = B*B - 4*A*C
x1 = (-B + delta**0.5)/(2*A)
x2 = (-B - delta**0.5)/(2*A)
print("O valor de x1 é: ",x1)
print("O valor de x2 é: ",x2)