"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

excluir = ['.', ',', '-', '/', ' ']

while True:

    def digito():
        j, soma = len(novo_cnpj) - 7, 0
        for i in range(len(novo_cnpj)):
            if j < 2:
                j = 9
            op = int(novo_cnpj[i])*j
            soma += op
            j -= 1
        if 11 - (soma % 11) > 9:
            digito = 0
        else:
            digito = 11 - (soma % 11)
        return str(digito)

    cnpj = input('Entre com o CNPJ')

    for i in cnpj:
        if i in excluir:
            cnpj = cnpj.replace(i, '')
    novo_cnpj = cnpj[:-2]

    novo_cnpj = novo_cnpj+digito()
    novo_cnpj = novo_cnpj+digito()

    sequencia = novo_cnpj == str(novo_cnpj[0]) * len(cnpj)
    if novo_cnpj == cnpj and not sequencia:
        print('\nO CNPJ é válido')
    else:
        print('\nO CNPJ é inválido')
