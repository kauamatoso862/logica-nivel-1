# Verificação de Nota - Peça ao usuário para digitar sua nota (0 a 10) e classifique:
# Nota ≥ 7: Aprovado
# Nota entre 5 e 6.9: Recuperação
# Nota < 5: Reprovado

nota = int(input("Digite a sua nota:"))
if nota > 7:
    notas = "Aprovado"
elif 5 <= nota <= 6.9:
    notas = "Recuperação"
elif nota < 5:
    notas = "Reprovado"

print(f"Você está: {notas}")
