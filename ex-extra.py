# Outros exercicios:
#Classificação de Idade - Peça ao usuário sua idade e classifique da seguinte forma:
#Menor de 12 anos: Criança
#Entre 12 e 17 anos: Adolescente
#Entre 18 e 59 anos: Adulto
#60 anos ou mais: Idoso

idade = int(input("Qual a sua idade?"))
if idade < 12:
    faixaetaria = "Criança"
elif 12 <= idade <= 17:
    faixaetaria = "Adolescente"
elif 18 <= idade <= 59:
    faixaetaria = "Adulto"
else:
    faixaetaria = "Idoso"

print(f"Você é classificado como: {faixaetaria}")
