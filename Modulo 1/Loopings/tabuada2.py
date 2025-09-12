while True:
    numero = int(input("Digite o número: "))
    i = int(input("Digite o número que deve começar: "))
    final = int(input("Até onde a tabuada vai: "))
    sair = input("sair do programa? Y/N: ")
    while i <= final:
        print(f"{i} X {numero} = {i * numero}")
        i += 1  

