def tabela_verdade(conectivo):

    valores_logicos = [(True, True), (True, False), (False, True), (False, False)]

    titulo = 'p | q | ' + conectivo
    print(titulo)
    print('-' * (len(titulo) + 1))

    for valor in valores_logicos:
        p, q = valor

        if conectivo == 'p ^ q':
            result = p and q
        elif conectivo == 'p v q':
            result = p or q
        elif conectivo == 'p → q':
            result = (not p) or q
        elif conectivo == 'p ↔ q':
            result = p == q
        elif conectivo == 'p ⊻ q':
            result = p != q

        linha = ' | '.join(["V" if p else "F", "V" if q else "F", "V" if result else "F"])
        print(linha)

print("\n[ Conjunção ]\n")
tabela_verdade('p ^ q')

print("\n[ Disjunção  ]\n")
tabela_verdade('p v q')

print("\n[ Condicional ]\n")
tabela_verdade('p → q')

print("\n[ Bicondicional ]\n")
tabela_verdade('p ↔ q')

print("\n[ Ou Exclusivo ]\n")
tabela_verdade('p ⊻ q')
