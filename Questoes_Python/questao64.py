# 64. Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

import random
numeros_randomicos = [random.randint(1, 100) for _ in range(10)]
mult_de_3 = [numeros_randomicos[i] for i in range(len(numeros_randomicos)) if numeros_randomicos[i] % 3 == 0]

if mult_de_3:
    print("Números múltiplos de 3 na lista:", mult_de_3)
else: 
    print("Nenhum número é múltiplo de 3.")
