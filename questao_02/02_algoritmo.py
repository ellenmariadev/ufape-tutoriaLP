num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

# Objetivo: encontrar o maior número que pode dividir dois números sem deixar resto = MÁXIMO DIVISOR COMUM (MDC).
# A função calculcar_mdc realiza uma série de divisões entre os dois números (a e b). A cada iteração, (a) assume o valor de (b) e o resto da divisão é atribuído a (b). Essas atribuições ocorrem até (b) se tornar 0. Quando (b) assume o valor de 0, o valor final de (a) corresponde ao MDC que procuramos.

# [ Exemplo: ]

# O valor de (a) é 75 e o valor de (b) é 45. 
# Na primeira iteração, (a) se torna 45 (o valor original de b) e (b) se torna 30 (o resto de 75 dividido por 45).
# Na próxima iteração, (a) se torna 30 (o valor antigo de b) e (b) se torna 15 (o resto de 45 dividido por 30).
# Na terceira iteração, (a) se torna 15 (o valor antigo de b) e (b) se torna 0 (o resto de 30 dividido por 15).
# Como (b) é 0, o loop termina e o algoritmo retorna (a), que é 15. Portanto, encontramos o MDC de 75 e 45 que é 15. 

def calcular_mdc(a, b):
    a = abs(a) # O MDC é sempre um número >= 0.
    b = abs(b) 
    while b != 0: 
        resto = a % b 
        a = b 
        b = resto 
    return a

# Objetivo: encontrar o menor número que é múltiplo comum dos dois números.
# A função calcular_mmc retorna o MMC dos números (a) e (b). O produto de (a) * (b) divido pelo MDC de (a) e (b) resulta no MMC.

def calcular_mmc(a, b):
    return abs (a * b) // calcular_mdc(a, b) # O MMC é sempre um número >= 0.

print("MDC:", calcular_mdc(num1, num2))
print("MMC:", calcular_mmc(num1, num2))



# Casos de Teste
testes = [
    (11, 11), # MDC: 11, MMC: 11
    (12, 18), # MDC: 6, MMC: 36
    (56, 48), # MDC: 8, MMC: 168
    (8, 24),  # MDC: 8, MMC: 24
    (84, 36), # MDC: 12, MMC: 252
    (75, 45),  # MDC: 15, MMC: 225
    (-48, 18), # MDC: 6, MMC: 144
    (56, -48), # MDC: 8, MMC: 168
    (-77, -22), # MDC: 11, MMC: 154
]

print(f"\n----- CASOS DE TESTE -----")
for num1, num2 in testes:
    mdc = calcular_mdc(num1, num2)
    mmc = calcular_mmc(num1, num2)
    print(f"\nPara os números {num1} e {num2}:")
    print(f"MDC: {mdc}")
    print(f"MMC: {mmc}")

    