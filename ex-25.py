#  Somar números positivos digitados pelo usuário até que ele digite um número negativo
soma = 0

while True:
    
  numero = float(input("Digite um número (negativo para parar): "))

  if numero < 0:
        break  
    else:
  soma += numero  

print(f"A soma dos números positivos digitados é: {soma}")
