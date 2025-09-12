try:
    #área de inputs
    print("------------------------------")
    print("--------PROGRAMA IMC--------- ")
    print("------------------------------")
    name=input("digite seu nome: ")
    print("------------------------------")
    peso=float(input("digite seu peso: "))
    print("------------------------------")
    Altura=float(input("Digite sua altura: "))
    imc= peso/ (Altura*Altura)

    #área de salvamento de arquivo
    with open ("IMC.txt","a") as arquivo:
        arquivo.write(f"|{imc:.2f}|")
except:
    print('Digite um valor valído (Use "." em vez de ",")')