# Titulo: Simulação/calculadora 

import random

# Erro 1: n_1 = int(input (erro/randint)('informe o  PRIMEIRO número: '))
# Erro 2: n_2 = int(input('informe o SEGUNDO número: '))                                                              

n_1 = random.randint(1, 10)
n_2 = random.randint(1, 10)
n = random.randint(1, 10)


def soma(n1, n2):
    exp1 = n1 + n2
    print(exp1)
    return exp1


def sub(n1, n2):
    exp2 = n1 - n2
    print(exp2)
    return exp2


def multi(n1, n2):
    exp3 = n1 * n2
    print(exp3)
    return exp3


def div(n1, n2):
    exp4 = n1 / n2
    print(exp4)
    return exp4


while True:
    soma(n_1, n_2)
    sub(n_1, n_2)
    multi(n_1, n_2)
    div(n_1, n_2)
    break
