# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Evitar divisão por zero
if num2 != 0:
    divisao = num1 / num2
    resto = num1 % num2
else:
    divisao = "Não é possível dividir por zero"
    resto = "Indefinido"

# Saída
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Resto:", resto)