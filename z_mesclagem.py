

def mesclar(rota, index_nome, index_igual, index_versao, qtd):
    with open(rota, 'r') as doc:
        index = 0
        linhas = list(str(doc.read()).split('\n'))
        while index < qtd:
            print(linhas[index_nome - 1] + linhas[index_igual - 1] + linhas[index_versao - 1])
            index_nome += 1
            index_igual += 1
            index_versao += 1
            index += 1

if __name__ == '__main__':
    mesclar(rota='/home/lucas/PycharmProjects/recursos/txt.txt', index_nome=1, index_igual=42, index_versao=83, qtd=41)
