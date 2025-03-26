# Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

ordem = sorted([num1, num2, num3])

print(f"A ordem dos número é: {ordem}")
