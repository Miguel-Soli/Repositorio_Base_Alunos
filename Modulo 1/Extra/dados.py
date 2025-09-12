name = input("Digite o seu nome: ")
email = input("Digite o seu email: ")

with open("pessoa.txt","a") as arquivo:
    arquivo.write(f"| {name} | {email}|")