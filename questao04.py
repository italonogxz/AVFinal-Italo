# Descubrir de qual cidade é o seu DDD
print("descubra de onde é seu DDD\n")
# int para responder com números inteiros,usa-se "f" para poder ser colocado uma variável dentro da string
#obs: não utilizar espaço e nem linhas ao digitar seu DDD
numero = int(input(f"digite seu numero de telefone(brasileiro) \nObs: nao utilize espaços e nem sinais: "))
# salav os dois primeiros digitos do número de telefone na variável número
numero = int(str(numero)[:2])
#compara os dois primeiros digitos do número de telefone e identifica e descobre seu DDD
if numero == 61:
    print("Brasilia")
elif numero == 71:
    print("Salavdor")
elif numero == 11:
    print("Salvador")
elif numero == 21:
    print("Rio de Janeiro")
elif numero == 32:
    print("Juiz de Fora")
elif numero == 19:
    print("Campinas")
elif numero == 27:
    print("Vitoria")
elif numero == 31:
    print("Belo Horizonte")
else:
    print("DDD não cadastrado ou invalido")