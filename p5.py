#Escreva um programa que leia o preco
#a prazo de um produto e imprima o seu preco a
#vista, que tem um desconto de 9%.

preco = input()
preco_float = float(preco)
preco_desconto = preco_float * (91/100)

print(f'{preco_desconto:.4f}')