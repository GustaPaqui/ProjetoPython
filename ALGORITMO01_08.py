#Declarar
P=0
mês=1
#inicio
P = float(input("Qual o valor depositado na poupança?"))   
P = P * (1 + 0.13)**mês
print("O valor do dinheiro após ",mês," mês é: ",P)
#fim