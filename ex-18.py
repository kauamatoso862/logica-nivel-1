# Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numeros = sorted ([num1, num2, num3])
resultado = numeros[1] + numeros[2]

print(f"O resuldado dos dois maiores é: {resultado}")
