

"""
Módulo >>> grid.py

Objetivo:
         determinar o tamanho de um objeto do template (tag) ocupa em uma linha em um tamanho de janela
"""

"OBS"   # A construção baseia-se em três grupos de divs:   [ container / row / col ]
"OBS2"  # Das três divs, a que define o tamanho do objeto: [ col ]
def tamanhos():
    """
    col-xm- / col- = 576px menos       (extra pequena)
    col-sm-        = 576px até 768px   (pequena)
    col-md-        = 768px até 992px   (média)
    col-lg-        = 992px até 1200px  (grande)
    col-xl-        = 1200px até 1920px (extra grande)

    EXEMPLO:
            <div class="container">
                <div class="row">
                    <div class="col col-sm- col-md- col-lg- col-xl-">
                        <tag>Conteúdo</tag>
                    </div>
                </div>
            </div>
    """
