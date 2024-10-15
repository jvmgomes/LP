'''
Escreva um programa que leia um numero inteiro de 3 digitos que representa o numero
de uma conta corrente e imprima seu o digito verificador, o qual e calculado da seguinte
forma:
– Numero: 235
– Somar o numero da conta com seu inverso: 235 + 532 = 767
– Multiplicar cada digito pela sua ordem posicional e somar esses resultados: 7*1 +
6*2 + 7* 3 = 40
– O ultimo digito desse resultado e o digito verificador da conta: 0
''' 

numero = input()
numero_int = int(numero)
numero_inverso_string = numero[::-1]
numero_inverso_int = int(numero_inverso_string)

soma = numero_int + numero_inverso_int
soma_str = str(soma)

soma_str_1 = soma_str[0]
soma_str_2 = soma_str[1]
soma_str_3 = soma_str[2]


soma_int_1 = int(soma_str_1)
soma_int_2 = int(soma_str_2)
soma_int_3 = int(soma_str_3)


multiplicacao = soma_int_1 * 1 + soma_int_2 * 2 + soma_int_3 * 3
multiplicacao_str = str(multiplicacao)

digito_verificador = multiplicacao_str[-1]

print(digito_verificador)