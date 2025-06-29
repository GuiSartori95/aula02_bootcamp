import math
# #### Inteiros (`int`)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# #RESOLUÇÃO
# numero_01 = int(input("Digite o primeiro número: "))
# numero_02 = int(input("Digite o segundo número: "))

# resultado = numero_01 + numero_02
# print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#RESOLUÇÃO
# numero_usuario = int(input("Insira um número aqui: "))
# resultado = numero_usuario // 5
# print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# #RESOLUÇÃO
# numero_01 = int(input("Informe um número aqui: "))
# numero_02 = int(input("Informe outro número aqui: "))

# resultado = numero_01 * numero_02
# print(f"O resultado é {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# #RESOLUÇÃO
# try:
#     Numero_01 = int(input("Insira um número inteiro: "))
#     Numero_02 = int(input("Insira outro número inteiro: "))
#     resultado = Numero_01 // Numero_02
#     print(f"O resultado desta divisão é: {resultado}")
# except ZeroDivisionError:
#     print("integer division ot modulo by zero")
# except KeyboardInterrupt:
#     print("Acho que tu não quis apertar ai")
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# try:
#     numero_01 = int(input("Inserir um número inteiro"))
#     numero_02 = int(input("Inserir outro número inteiro"))
#     resultado = numero_01 // numero_02
#     print(resultado)
# except ZeroDivisionError:
#     print("integer divisio or modulo by zero ")
# except KeyboardInterrupt:
#     print("acho que tu não quis apertar ")

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# #RESOLUÇÃO
# numero_01 = float(input("Insira um número aqui: "))
# numero_02 = float(input("Insira outro número aqui: "))
# resultado = numero_01 + numero_02
# print(f"O resultado da soma é: {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# #RESOLUÇÃO
# num01 = float(input("Insira um número aqui: "))
# num02 = float(input("Insira outro número aqui: "))
# resultado = num01 + num02
# Média = resultado // 2
# print(f"A média entre {num01} e {num02} é: {Média}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# #RESOLUÇÃO
# base = float(input("Insira a base aqui: "))
# expoente = float(input("Insira o exepoente aqui: "))
# resultado = base ** expoente

# print(f"O resultado é {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
##RESOLUÇÃO
# celsius = float(input("Informe aqui a temperatua em graus C: "))
# fahrenheit = (9/5 * celsius) + 32
# print(f"A temperatura de {celsius}C corresponde a {fahrenheit} F")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio_do_circulo= float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
#area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)

#print(area_do_circlo_formatada)

# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# #RESOLUÇÃO
# texto = str(input("Escreva algo neste lugar: "))
# maiusculo = texto.upper()
# print(maiusculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# #RESOLUÇÃO
# nome_usuario = str(input("Escreva seu nome neste lugar: "))
# minusculo = nome_usuario.lower()
# print(minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços.
# #RESOLUÇÃO
# frase = str(input("Insira uma frase aqui: "))
# frase_sem_espaco = frase.replace(" ","")
# print(frase_sem_espaco)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o mês por extenso.
# #RESOLUÇÃO
# data_do_usuario = input("Insira uma data no formato dd/mm/aaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 é o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 é o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 é o: {lista_de_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# #RESOLUÇÃO 1
# palavras = ["Meu", "amigo", "é", "gremista"]
# unificada = " ".join(palavras)
# print(unificada)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# #RESOLUÇÃO 1
# num01 = 20
# num02 = 30
# comparacao = num01 > num02
# print(comparacao)

# #RESOLUÇÃO 2
# Esporte = str(input("Digite o esporte que você deseja praticar nesta quadra de futebol: ")) == "futebol"
# material = str(input("Você tem tênis? (sim/não): ")).strip().lower() == "sim"
# pode_jogar = Esporte and material
# print(pode_jogar)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# #RESOLUÇÃO
# Casaco1 = str(input("Hoje está frio, você vai usar 2 casacos?(sim/não): ")) == "sim"
# Casaco2 = str(input("E você vai usar pelo menos 1 casaco? (sim/não): ")) == "sim"

# Pode_sair_na_rua = Casaco1 or Casaco2
# if Pode_sair_na_rua:
#     print("Pode sair na rua!!")
# else:
#     print("Não pode sair de casa")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# #RESOLUÇÃO
# pergunta1 = str(input("Você gosta de mentir? (sim/não): ")) == "não"
# resposta = not pergunta1
# print(resposta)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# #RESOLUÇÃO
# numero1 = int(input("Insira um número: "))
# numero2 = int(input("Insira outro número: "))
# comparativo = numero1 == numero2
# print(comparativo)


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# #RESOLUÇÃO
# numero1 = int(input("Insira um número: "))
# numero2 = int(input("Insira outro número: "))
# comparativo = numero1 != numero2
# print(comparativo)


# #### try-except e if

# 21: Conversor de Temperatura
# #RESOLUÇÃO
# try:
#     celsius = float(input("Digite a temperatura: "))
#     Fahrenheit = (celsius * 1.8) + 32
#     print(f"A tempeatura convertida é {Fahrenheit}")
# except:
#     print("Bah, tu não digitou uma tempratura tchê!!!")

# 22: Verificador de Palíndromo
# #RESOLUÇÃO
# try:
#     #não precisa de str(input..) pois o input já retorna str, então fica reduante e não cumpre o propósito
#     texto = input("Digite uma palavra para verificar se é um políndromo: ")
#     #item necessário para tratar entrada vazia
#     if not texto:
#         raise ValueError("Você não digitou nada.")
#     #Variável para padronizar a entrada do usuário
#     texto_formatado = texto.strip().lower()
#     #Condicional que dirá se é ou não um políndromo
#     if texto_formatado == texto_formatado[::-1]:
#          print("✅ É um palíndromo!")
#     else:
#         print("❌ Não é um palíndromo.")
# #aqui evitará um erro do tipo Valor (valuerror)        
# except ValueError as erro:
#     print(f"Erro: {erro}")
# #aqui evita qualquer tipo de erro, utilziando a variável {e}, ela que vai trazer a mensagem do motivo do erro
# except Exception as e:
#     print(f"Ocorreu um erro inesperado: {e}")

# 23: Calculadora Simples
##RESOLUÇÂO
# try:
#     numero01 = float(input("Digite um número: "))
#     operador = input("Digite um operador (+,-,/,*): ")
#     numero02 = float(input("Digite outro número: "))
#     if operador == "+":
#         resultado = numero01 + numero02
#     elif operador == "-":
#         resultado = numero01 - numero02
#     elif operador == "/":
#         if numero01 == 0:
#             raise ZeroDivisionError("Não é possível divir com zero")
#         resultado = numero01 / numero02
#     elif operador == "*":
#         resultado = numero01 * numero02
#     else:    
#         raise ValueError("operador inválido")

#     print(f"Resultado: {resultado}")
# # Tratamento de erros
# except ValueError as erro:
#     print(f"❌ Erro de valor: {erro}")
# except ZeroDivisionError as erro:
#     print(f"🚫 Erro matemático: {erro}")
# except Exception as e:
#     print(f"⚠️ Erro inesperado: {e}")

# 24: Classificador de Números
# RESOLUÇÃO
# try:
#     numero = float(input("Digite um número: "))

#     if numero > 0:
#         print("✅ O número é positivo.")
#     elif numero < 0:
#         print("🚫 O número é negativo.")
#     else:
#         print("⚪ O número é zero.")

# except ValueError:
#     print("❌ Erro: você deve digitar um número válido.")

# 25: Conversão de Tipo com Validação
#RESOLUÇÃO
try:
    valor = input("Digite um número inteiro: ")

    # Validação: tenta converter o valor para inteiro
    numero_inteiro = int(valor)

    print(f"✅ Conversão bem-sucedida: {numero_inteiro} é um inteiro.")

except ValueError:
    print("❌ Erro: o valor digitado não é um número inteiro válido.")