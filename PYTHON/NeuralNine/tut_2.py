

"""
Fonte:
    https://www.youtube.com/watch?v=bYLU02QhlUM

Canal:
    NeuralNine

Título:
    Convert Python To Exe Files
"""

# Para Windows
def tutorial():
    """
    1. pip install pyinstaller

    2. criar um diretório em algum lugar desejado, que inicialmente, armazenará dois módulos principais:
       2.1 módulo .py    (algoritmo)
       2.2 módulo imagem (serve como ícone do executável do algoritmo)
       2.3 no diretório, botão direito em uma área vazia e escolher: open in terminal
       2.4 pyinstaller --onefile -w -i imagem.formato módulo_python.py

    3. um conjunto de diretórios será criado no mesmo local
    4. dentre eles, o executável encontra-se no diretório: [ dist ]
    """
