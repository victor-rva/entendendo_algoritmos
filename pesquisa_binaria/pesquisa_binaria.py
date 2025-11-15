def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            print(f"Item {item} encontrado na posição {meio}.")
            return meio
        if chute > item:
            alto = meio - 1
            print(f"Procurando na metade inferior: {lista[baixo:alto+1]}")
        else:
            baixo = meio + 1
            print(f"Procurando na metade superior: {lista[baixo:alto+1]}")
    print(f"Item {item} não encontrado na lista.")
    return None

pesquisa_binaria([1, 3, 5, 7, 9], 3)