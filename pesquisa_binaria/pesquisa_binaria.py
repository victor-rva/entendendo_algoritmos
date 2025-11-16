def pesquisa_binaria(lista, item):
    """Realiza uma busca binária em uma lista ordenada para encontrar o índice de um item específico."""
    baixo = 0 # índice inicial da lista
    alto = len(lista) - 1 # índice final da lista

    while baixo <= alto:
        meio = (baixo + alto) // 2 # O operador // realiza uma divisão inteira, por isso é utilizado, pois os índices devem ser inteiros. 
        # meio é o índice do elemento do meio da lista
        print(f"Índices atuais - Baixo: {baixo}, Alto: {alto}, Meio: {meio}")
        chute = lista[meio] # valor do meio da lista
        print(f"Chute atual: {chute}")
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