 # As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

quantidade = int(input("Quantas maçãs?"))
if (quantidade > 12):
    print(quantidade * 1.30)
else:
    print(quantidade * 1.00)
    
