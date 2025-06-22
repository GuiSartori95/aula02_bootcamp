import math
# #### Inteiros (`int`)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#numero_01 = int(input("Inserir um número inteiro"))
#numero_02 = int(input("Inserir outro número inteiro"))
#resultado = numero_01 // numero_02
#print(resultado)

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio_do_circulo= float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2

print(f"{area_do_circulo:.2f})