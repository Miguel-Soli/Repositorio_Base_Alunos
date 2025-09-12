try:
    nome=input("Digite seu nome: ")
    nota1=float(input("digite sua nota: "))
    nota2=float(input("digite sua nota: "))
    nota3=float(input("digite sua nota: "))
    nota4=float(input("digite sua nota: "))

    media= float (nota1+nota2+nota3+nota4)/4

    with open("Media do aluno.txt","a") as arquivo:
        arquivo.write(f"| {nome} | {media}|")

except:
    print("digite um valor valído ")