while True:
    print("-----------------------")
    print("1-Sistema de impar e par: ")
    print("2-Saiba se você é de maior: ")
    print("3-Faça a media da sua nota: ")
    print("4-Login de usuario: ")
    print("5-Multiplição: ")
    print("6-Soma dos numeros de 1 a 100 : ")
    print("7-Numeros de 1 a 100 : ")
    print("8-Numeros pares de 2 a 50 : ")
    print("0-sair do programa: ")
    print("-----------------------")

    opção= input("Digite uma das opções: ")

#Sitema de impar e par
    if opção =="1":
        numero = float(input("digite o numero desejado: "))
    
        if numero % 2==0:
            print("Ele é par")
    
        else:
            print("Ele e impar")
#Sitema de Maioridade 
    if opção == '2':
     Idade = int(input("Digite sua idade: "))

     if  Idade >=18:
         print("Boa você e de maior 😁😁😁")
     else: 
            print("espere mais um pouco")
#Nota escolar
    if opção == "3":
          
        nome=input("Digite seu nome: ")
        nota1=float(input("digite sua nota: "))
        nota2=float(input("digite sua nota: "))
        nota3=float(input("digite sua nota: "))
        nota4=float(input("digite sua nota: "))
        
        media = float (nota1*nota2*nota3*nota4)/4

        if media >=7:
            print(f"{nome} você passou 😁😁😁")
        elif media >4:
            print(f"Sinto muito {nome},mas você está de recuperação")
        else:
            print(f"{nome} você reprovou 😭😭")

#login
    if opção =="4":
        print("-------------------------------------------")
        print("--------Login--de--Usuario-----------------")
        print("-------------------------------------------")
        Usuario= input("🧑Digite seu usuario: ")
        print("-------------------------------------------")
        Senha= input("🔑 Digite sua senha: ")
        print("-------------------------------------------")

        if Usuario =="Miguel09" and Senha=="Michael":
         print("Logado com sucesso 😃😃😃")
         print("-------------------------------------------")
        else:
            print("Senha ou usuario incorretos😔😔😔")
            print("-------------------------------------------")
#uso do na multiplicação for
    if opção == "5":
     print("multiplicação")
     numero= int(input("Digite um número: "))

     for i in range (1,11):
         print(f"{i}X {numero} = {i * numero}")
#soma dos numeros 
    if opção =="6":
      print("Soma de números de 1 a 100")
      for some in range (1,101):
       print(f"{some} + {some} = {some+some}")
#numeros de um a 100
    if opção =="7":
     print("Números de 1 a 100")
     for num in range (1,101):
      print(f"{num}")
#numeros pares 
    if opção =="8":
     print("numeros pare de um a 50")
     for num2 in range (1,51,):
       if num2 % 2==0:
        print(f'{num2}') 
#if and for
    if opção == "9":
       import random
    
       numero_sorteado = random.randint(1,10)
       acertou = False
       print("Jogo de adidivinhação de 1 a 10.")
       for tentativa in range(1,2): #3tentativas
          chute = int(input(f"Tentativa {tentativa}: digite a tentativa: "))
    if chute == numero_sorteado:
          print("parabéns você acertou 😁😁😁")
          acertou = False
          break
    else:
        print("Errou! 😹😹😹")
    if not acertou:
         print(f"O número era {numero_sorteado}")