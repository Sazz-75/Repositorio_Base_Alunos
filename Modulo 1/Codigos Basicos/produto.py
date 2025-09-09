nome_produto = input("digite o nome do produto: ")
Preco = float(input("digite o preço do produto: "))
desconto = float(input("digite o percentual do desconto: "))
valor_desconto = Preco * desconto / 100
preco_final = Preco - valor_desconto
print(f"Produto: {nome_produto} - preco final: R$ {preco_final}")