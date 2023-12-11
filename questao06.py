# Explicação
print("descubra a média dos valores positivos")
#lista dos "numeros" e da variável "positivo"
numeros = []
positivo=0
# Repete a ação 5 vezes
for i in range(0,5):
    # pede um valor para ser colocado na váriavel "numero"
    numero = float(input(f'digite o {i+1}° numero: '))
    # se o número for maior que 0 adicionar "1" na variável "positivo, e colocar na lista de "numeros
    if numero>0:
        positivo = positivo+1
        numeros.append(numero)
# soma os números da lista "numeros"
soma = sum(numeros)
# mostra a quantidade de valores postivos
print(f"{positivo} valores positivos")
# mostra a média da lista "numeros"
print(f"{soma/5}")