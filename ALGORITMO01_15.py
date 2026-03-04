#Declarar
cat1=0
cat2=0 
cat3=0
#inicio
cat1 = float(input("Qual o valor do cateto 1?"))
cat2 = float(input("Qual o valor do cateto 2?"))
cat3 = ((cat1**2) + (cat2**2))
cat3 = cat3**(1/2)
print("O valor da hipotenusa é: ",cat3)
#fim