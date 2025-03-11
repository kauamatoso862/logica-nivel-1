#Implemente um programa que na primeira linha faça um print perguntando o nome do usuário e, na linha 2, chame a função input() para capturar o valor do teclado e armazenar na memória do computador.

nome = input("Qual o seu nome?")
print("Olá,", nome)

idade = input(f"{nome}, Qual a sua idade? ")
print(idade,)

residencia = input(f"{nome}, Qual o número da sua residencia?")
print(residencia)

cep = input(f"{nome},Qual é o seu CEP")
print (cep)

dados_usuario = {
    "Nome": nome,
    "Idade": idade,
    "Residencia": residencia,
    "CEP": cep
}

print("\nCadastro do usuário:")
for chave, valor in dados_usuario.items():
    print(f"{chave} = {valor}")
