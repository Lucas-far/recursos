

def infos():
    """
    Uso:
        @poo (programação orientada a objetos)

    Contexto:
        print

    Objetivo:
        criar um dicionário que retorna as classes especificadas nos parâmetros em função
        criar um dicionário que retorna as classes especificadas nos atributos de instância em POO
    """

# Usando o método [ .__annotations__ ] em uma função normal (precisa haver tipagem nos parâmetros)
def dados(nome: str, idade: int, calvice: bool):

    if calvice:
        calvice = 'Sim'
    else:
        calvice = 'Não'

    return \
        f"""
        Dados:
        1. Nome: {nome}
        2. Idade: {str(idade) + ' anos'}
        3. Possui calvice? {calvice}
        """

dados('Lucas', 28, False)
print(dados.__annotations__)  # {'nome': <class 'str'>, 'idade': <class 'int'>, 'calvice': <class 'bool'>}

# Usando o método [ .__annotations__ ] em uma classe (programação orientada a objetos)
class Dados:
    # Método de instância com decorador, não aceita o método
    @property
    def nome(self) -> str:
        return self.__nome

    # Atributos de instância aceitam o método...se há tipagem tipagem especificada
    def __init__(self, nome: str, idade: int, calvice: bool):
        self.__nome = nome
        self.__idade = idade
        self.__calvice = calvice

    # Métodos de instância sem decorador, aceitam o método...se há tipagem especificada
    def exibir_nome(self) -> str:
        return self.__nome

pessoa = Dados('Lucas', 28, False)

print(pessoa.__init__.__annotations__)     # {'nome': <class 'str'>, 'idade': <class 'int'>, 'calvice': <class 'bool'>}
print(pessoa.exibir_nome.__annotations__)  # {'return': <class 'str'>}

# Exemplo errado
"print(pessoa.nome.__annotations__)"
# AttributeError: 'str' object has no attribute '__annotations__'
