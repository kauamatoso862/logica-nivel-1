# Pedir senha até que seja digitada a correta

senha_correta = "1212"

while True:

    senha = input("Digite a senha: ")

   
    if senha == senha_correta:
        print("Senha correta!")
        break  
    else:
        print("Senha incorreta!")
