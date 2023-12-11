# descobirir o valor do aumento usando, print para anunciar oque deverá ser feito
print("descubra o valor do seu aumento")
# float podendo ser usado números quebrados, mostrando qual seu salario
salario = float (input("qual seu salario: "))
# while, serve para: enquanto seu salario for menor que 0
while salario < 0:
    # digite um valor valido na tabela
    print('\ndigite um valor valido')
    salario = float(input("qual seu salario: "))
# if, se seu salario for menor ou igual a 400
if salario <= 400:
    # será acresentado um aumento de 15%
    print(f"novo salario: {salario+(salario*(15/100)):.2f} \nreajuste ganho: {salario*(15/100):.2f} \npercentual: 15 % ")
# se for maior que 400 e menor ou igual a 800
elif salario > 400 and salario <= 800:
    # será acresentado um aumento de 12%
    print(f"novo salario: {salario+(salario*(12/100)):.2f} \nreajuste ganho: {salario*(12/100):.2f} \npercentual: 12 % ")
# se for maior que 800 e menor ou igual a 1200
elif salario > 800 and salario <= 1200:
    # será acresentado um aumento de 10%
    print(f"novo salario: {salario+(salario*(10/100)):.2f} \nreajuste ganho: {salario*(10/100):.2f} \npercentual: 10 % ")
# se for maior que 1200 e menor ou igaul que 2000
elif salario > 1200 and salario <= 2000:
    # será acresentado um aumento de 7%
    print(f"novo salario: {salario+(salario*(7/100)):.2f} \nreajuste ganho: {salario*(7/100):.2f} \npercentual: 7 % ")
# se for falsa será um aumento de 4%
else:
    print(f"novo salario: {salario+(salario*(4/100)):.2f} \nreajuste ganho: {salario*(4/100):.2f} \npercentual: 4 % ")               