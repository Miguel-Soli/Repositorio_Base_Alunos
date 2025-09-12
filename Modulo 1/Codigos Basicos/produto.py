print("----------------------------------------------------------------")
print("----------------Calculadora de descontos------------------------")
print("----------------------------------------------------")
nome_do_produto = input("Digite o nome do produto: ")
print("----------------------------------------------------")
produto_porcentagem= float(input("Digite a porcentagem de desconto do produto: "))
print("---------------------------------------------------------------")
produto_preco= float(input("Digite o valor: "))
print("---------------------------------------------------------------")

valor_final = produto_preco*produto_porcentagem/100
print("---------------------------------------------------------------")
print(f"Seu produto é: {nome_do_produto} \n O desconto é: {produto_porcentagem}% \n O valor final é: {valor_final}")
print("---------------------------------------------------------------")