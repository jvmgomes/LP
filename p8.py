'''
Escreva um programa que leia dois numeros inteiros referentes a hora atual (ou seja,
hora com os minutos, como por exemplo 13 horas e 30 minutos) e imprima quantos
minutos se passaram desde o inicio do dia
'''

hora_atual_hora = int(input())
hora_atual_minutos = int(input())

minutos_desde_o_inicio_do_dia = hora_atual_hora * 60 + hora_atual_minutos

print(minutos_desde_o_inicio_do_dia)


