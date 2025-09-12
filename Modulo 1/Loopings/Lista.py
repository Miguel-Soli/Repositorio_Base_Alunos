lista = [1,2,3,4,5,6,7,8,9,10]
#Adicionar

def adicionar(lista):
     adicionar_numero = int(input("Digite o número na lista: "))
     lista.append(adicionar_numero)
     print(f"{adicionar_numero} Adicionado com sucesso.")


#listar
def listar(lista):
      for i, lista in enumerate(lista, start=1):
            print(f"{i}. {lista}")

#Mover
def mover(lista):
         posição = int(input("Em qual posiçâo? : "))
         num_Q = int(input("Qual número vai colocar? : "))
         lista.remove(num_Q)
         lista.insert(posição-1,num_Q)

#SOMA
def soma(lista):
         soma = 0
         for i in lista:
          soma += i
         print(f"A soma é {soma}")
        
def Maior_menor(lista):
       maior = max(lista)
       menor = min(lista)
       print(f"O menor é {menor} e o maior é {maior}")


try:
  while True:
        print("-----------------------")
        print("1-Adicionar números: ")
        print("2-Listar números: ")
        print("3-Remover número: ")
        print("4-Mover: ")
        print("5-Soma de todos da lista: ")
        print("6-Maior e menor: ")
        print("0-sair do programa: ")
        print("-----------------------")
        opção= input("Digite uma das opções: ")
    
        if opção == "1":
          adicionar(lista)

        elif opção=="2":
          listar(lista)
        
        
        elif opção =="3":
          remover_lista= int(input("Digite o número desejado: "))
          lista.remove(remover_lista)
          print(f"{remover_lista} removido com sucesso!")
       
        elif opção == "4":
          mover(lista)
          
        elif opção == "5":
          soma(lista)

        elif opção == "6":
          Maior_menor(lista)

        elif opção=="0":
             break
except:
    print("Digite um valor incorreto ❎")