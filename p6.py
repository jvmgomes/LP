#Escreva um programa que leia o valor da hora aula, o numero
#de horas de aula dadas no mes e o percentual de desconto do
#INSS e imprima o salario lıquido de um professor.

hora_aula = int(input())
horas_por_mes = int(input())
percentual_desconto = int(input())

salario = hora_aula * horas_por_mes
salario_liquido = salario * ((100 - percentual_desconto)/100)

print(f'{salario_liquido:.4f}')