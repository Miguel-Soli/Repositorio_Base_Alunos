print("___________SISTEMA DE USUÁRIOS__________--")
print("___________SEJA BEM VINDO__________--")

def cadastrar(usuario):
      novo_usuario = input("Digite o nome do usuário: ") 
      usuario.append(novo_usuario)
      print(f"{novo_usuario} Adicionado com sucesso.")
      print("-----------------------")

def listar(usuarios):
      for i, usuarios in enumerate(usuarios, start=1):
            print(f"{i}. {usuarios}")



usuarios = []
while True:
    print("-----------------------")
    print("1-Cadastra usuario: ")
    print("2-Listar usuario: ")
    print("3-Remover usuario: ")
    print("0-sair do programa: ")
    print("-----------------------")

    opção= input("Digite uma das opções: ")
    
    if opção == "1":
        cadastrar(usuario)

    elif opção=="2":
        listar(usuarios)
        
    elif opção =="3":
        remover_usuarios= input("Digite o nome do usuario: ")
        usuarios.remove(remover_usuarios)
        print(f"{remover_usuarios} removido com sucesso!")
    elif opção=="0":
        break