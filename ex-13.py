# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
anos = int(input("Digite a idade em anos: "))
meses = anos * 12
dias = anos * 365

print(f"A idade da pessoa em meses é: {meses}.")
print(f"A idade da pessoa em dias é: {dias}")
