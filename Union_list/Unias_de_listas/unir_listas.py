cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
abrev_cid = ['BA', 'SP', 'MG', 'RJ']
cidades_estados = []

def zipper(lista1, lista2):
    def retorna_resultado(lista1, lista2):
        for i in range(len(lista1)):
            cid_abrev = lista1[i], lista2[i]
            cidades_estados.append(cid_abrev)
    return retorna_resultado

resultado = zipper(cidades, abrev_cid)
resultado(cidades, abrev_cid)
print(cidades_estados)