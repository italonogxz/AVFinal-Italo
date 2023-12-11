# Configure para quanto de imposto o cliente ira pagar
print("quanto de imposto você tem que pagar?")
# Abaixo o usuario tera que digitar seu salario
salario = float(input("digite seu salario: "))
# coloque while para repetir a função de if, elif e else
while salario < 0:
    print("\nDigite um salario válido")
# aqui o usuario ira digitar seu salario valido
# usando o (float) para que o resultado possa ser em números quebrados
    salario = float(input("digite seu salario: "))
# aqui usará if(se),para se o salario do usuario for menor ou igual a 2000, será insento
if salario <= 2000:
    print('insento')
# usa-se o elif para verificar se a validação do if se for falsa
# se o salario do usuario for maior que 2000 e menor que 3000.1, terá taxa de 8%
# assim multiplicando o salario do usuario por 8 e dividindo por 100
elif salario > 2000 and salario < 3000.01:
    print(f"R$ {salario*(8/100):.2f}")
# salario acima de 3000 e menos que 4500, será o salario multiplcado por 18 e dividido por 100
elif salario > 3000 and salario < 4500.01:
    print(f"R$ {salario*(18/100):.2f}")
# (else) se o codigo if, for verdadeira (else) será falsa, e vice-versa
else:
    print(f"R$ {salario*(28/100):.2f}")