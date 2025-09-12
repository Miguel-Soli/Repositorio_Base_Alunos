#área de inputs
print("------------------------------")
print("--------PROGRAMA IMC--------- ")
print("------------------------------")
name=input("digite seu nome: ")
print("------------------------------")
peso=float(input("digite seu peso: "))
print("------------------------------")
Altura=float(input("Digite sua altura: "))
Imc= peso/ (Altura*Altura)

#área das condições
print("------------------------------")
if Imc < 18.5:
    print("Abaixo do peso 💀💀💀!!")

elif Imc <24.9:
    print('Peso normal 😁😁😁')
elif Imc < 29.9:
      print("Sobre peso ☹️ ☹️ ☹️")
elif Imc < 34.9:
       print("Obsidade grau I ☹️ ☹️ ☹️")
elif Imc < 39.9:
       print("Obsidade grau II ☹️ ☹️ ☹️")
else:
    print("Obsidade grau III ☹️ ☹️ ☹️")
print("------------------------------")
print(f"{name} Seu IMC {Imc:.4} ")
print("------------------------------")