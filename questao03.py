# indicando o "cofre"
print("cofre")
# a senha do programa será 2002
senha = 2002
# a variavel será tentativa, int podendo ser colocado só números inteiros, digite qual senha você acha que é
tentativa = int(input("digite a senha: "))
# enquanto a tentativa for diferente da senha, será incorreta
while tentativa != senha:
    # indicando: print("senha incorreta")
    print("senha incorreta")
    # variável = número inteiro
    tentativa = int(input("digite a senha"))
# se a senha estiver correta, será um acesso válido, indicando: print("acesso válido")
print("acesso valido")