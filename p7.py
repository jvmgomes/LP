#Escreva um programa que leia dois numeros reais
# referentes a altura (h) e o raio (r) de
#uma lata de oleo e imprima o 
#seu volume (V = 3.14 · h · r2).

altura = input()
raio = input()
altura_float = float(altura)
raio_float = float(raio)

volume = 3.14 * altura_float * raio_float**2
print(f'{volume:.4f}')