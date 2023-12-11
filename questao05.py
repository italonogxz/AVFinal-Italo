# contagem de valores pares
print("contagem de valores pares")
#A lista dos "numeros" e da variável "par"
numeros = []
par=0
# Repete a ação fornecida 5 vezes
for i in range (0,5):
    # pede para o usuario digitar um número
    numero = int(input(f'digite o {i+1})° numero: '))
    #se o número for par adicionar "1" a variável "par"
    if numero % 2 == 0:
        par = par+1
# mostra quantos números pares tem na lista
print(f"{par} valores pares")
