nome=input("Digite seu nome: ")
nota1=float(input("digite sua nota: "))
nota2=float(input("digite sua nota: "))
nota3=float(input("digite sua nota: "))
nota4=float(input("digite sua nota: "))

media= float (nota1+nota2+nota3+nota4)/4

if media >= 7:
    print("Você passou 😁😁😁")
elif media > 4:
    print("Que coisa recuperação 😢😢😢")
else:
    print("Reprovado 😭😭😭")
print(f"Seu nome é:{nome} Sua media bimestral é: {media:.1f}")

