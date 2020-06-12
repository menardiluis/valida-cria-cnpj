from random import randrange
novo_cnpj = str(randrange(100000000000, 999999999999))

def digito():
    j, soma = len(novo_cnpj) - 7, 0
    for i in range(len(novo_cnpj)):
        if j < 2:
            j = 9
        op = int(novo_cnpj[i]) * j
        soma += op
        j -= 1
    if 11 - (soma % 11) > 9:
        digito = 0
    else:
        digito = 11 - (soma % 11)
    return str(digito)

novo_cnpj = novo_cnpj + digito()
novo_cnpj = novo_cnpj + digito()

print(novo_cnpj)
