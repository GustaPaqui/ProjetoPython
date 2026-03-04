#Declarar
horas=0
valorh=0   
desconto=15
descendentes=0
salariobruto=0
salarioliquido=0
#inicio
horas = float(input("Quantas horas foram trabalhadas?"))
valorh = float(input("Qual o valor da hora trabalhada?"))
descendentes = int(input("Quantos descendentes tem?"))
salariobruto = horas * valorh
salarioliquido = salariobruto - desconto + (descendentes * 100)
print("O salario bruto é: ",salariobruto)   
print("O Salario liquido é: ",salarioliquido)
#fim