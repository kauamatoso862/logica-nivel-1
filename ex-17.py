#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
#etapas para resolver:
#	1 - peça os 3 valores
#	2 - descobrir e mostrar o maior


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)

print(f"O maior número é: {maior}")
