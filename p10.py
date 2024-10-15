'''
Escreva um programa que leia a quantidade de fitas que uma locadora de video possui
e o valor que ela cobra por cada aluguel, e mostre as informacoes pedidas a seguir:
– Sabendo que um terco das fitas sao alugadas por mes, exiba o faturamento da
locadora;
– Quando o cliente atrasa a entrega, e cobrada uma multa de 10% sobre o valor do
aluguel. Sabendo que um decimo das fitas alugadas no mes sao devolvidas com
atraso, calcule o valor ganho com multas por mes;
– Sabendo ainda que 2% das fitas se estragam ao longo do ano, e um decimo desse
total e comprado para reposicao, exiba a quantidade de fitas que a locadora tera no
final do ano.
'''

quantidade_fitas = int(input())
valor_fita = int(input())

quantidade_fitas_mes = quantidade_fitas / 3
faturamento = quantidade_fitas_mes * valor_fita

multa = valor_fita * 10/100
multa_mes = multa * (quantidade_fitas_mes * 1/10)

fitas_estragadas = quantidade_fitas * 2/100
fitas_estragas_total = quantidade_fitas * 98 / 100

reposicao = fitas_estragadas * 1/10
quantidade_fitas_final_ano = fitas_estragas_total + reposicao
quantidade_fitas_final_ano_int = int(quantidade_fitas_final_ano)


print(f'{faturamento:.4f}')
print(f'{multa_mes:.4f}')
print(f'{quantidade_fitas_final_ano_int}')