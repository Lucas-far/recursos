
def checar_dependencias(dependencia_projeto, dependencia_pyup):

    # Dependências atualmente no projeto
    with open(dependencia_projeto, 'r') as doc:
        var = sorted(list(str(doc.read()).split('\n')), reverse=True)

    # Dependências atualizadas do projeto, pegas do site Pyup e organizadas em um módulo .txt
    with open(dependencia_pyup, 'r') as doc:
        var2 = sorted(list(str(doc.read()).split('\n')), reverse=True)

    "OBS"  # sorted está sendo usado para ordenar dados para evitar possíveis irregularidades do projeto ou do website Pyup

    var3 = ['pip uninstall -y', ]  # lista de índices que receberá pacote desatualziado a ser desinstalado
    var4 = ['pip install', ]       # lista de índices que receberá cada pacote atualizado a ser instalado

    "Objetivo"  # Se var e var2 são iguais, não há o que atualizar, então apenas imprime-se 'OK' + incremento
    "Objetivo"  # Se não, adicionar em var3, o pacote a ser desintalado, e em var4, o pacote a ser instalado + incremento
    index = 0
    while index < len(var):
        if var[index] == var2[index]:
            print('OK', end=' ')
            index += 1
        else:
            var3.append(var[index])
            var4.append(var2[index])
            index += 1

    print('\n')
    print('Pacotes desatualizados')
    for obj in var3:
        print(obj, end=' ')  # Copia-se o retorno dessa linha e execute ela no terminal do projeto

    print('\n')
    print('Pacotes atualizados')
    for obj in var4:
        print(obj, end=' ')  # Depois, copia-se o retorno dessa linha e execute ela no terminal do projeto

checar_dependencias(
    '/home/lucas/PycharmProjects/recursos/PYTHON/f/requirements.txt',
    '/home/lucas/PycharmProjects/recursos/txt.txt'
)
