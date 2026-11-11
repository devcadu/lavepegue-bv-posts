"""LPBV-1111-12 — Mito x Verdade — qua 11/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 7

def selo(txt, cls):
    return boxes((cls, txt))

sl = [
    # 1 — capa
    s(1, N, "maquinas-tabela-02", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Você ainda acredita nisso?"), ("mg big", "Mito ou"), ("mg big ind1", "verdade?"))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">4 crenças sobre lavar roupa</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — sabão
    s(2, N, "salao-interno-01", "veil",
      '<div class="area" style="top:290px">' + selo("MITO", "mg big")
      + '<h2 class="h md" style="margin-top:30px">Mais sabão, roupa <em>mais limpa</em></h2>'
      '<div class="glass" style="margin-top:40px"><p class="lead">Sabão demais não sai no enxágue. '
      'Fica <b>resíduo</b> no tecido, a roupa fica áspera e a escura ganha <b>marcas brancas</b>.</p></div></div>'),
    # 3 — lotar a máquina
    s(3, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:290px">' + selo("MITO", "mg big")
      + '<h2 class="h md" style="margin-top:30px">Lotar a máquina <em>compensa</em></h2>'
      '<div class="glass" style="margin-top:40px"><p class="lead">A roupa precisa de <b>espaço pra girar</b>. '
      'Apertada demais, a água e o sabão não circulam e a sujeira fica.</p></div></div>'),
    # 4 — avesso
    s(4, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:290px">' + selo("VERDADE", "cy big")
      + '<h2 class="h md" style="margin-top:30px">Lavar do avesso <em>protege</em></h2>'
      '<div class="glass" style="margin-top:40px"><p class="lead">Virar a peça do avesso diminui o atrito do lado de fora: '
      '<b>a cor dura mais</b> e estampas e jeans sofrem menos.</p></div></div>'),
    # 5 — bolsos e zíper
    s(5, N, "entrada-vitrine-01", "veil",
      '<div class="area" style="top:290px">' + selo("VERDADE", "cy big")
      + '<h2 class="h md" style="margin-top:30px">Bolsos e zíper <em>antes</em></h2>'
      '<div class="glass" style="margin-top:40px">'
      + ilist([("coin", "Esvazie os bolsos"), ("closet", "Feche zíperes e botões"), ("fold", "Separe as peças delicadas")])
      + "</div></div>"),
    # 6 — virada Lave & Pegue
    s(6, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Aqui você não precisa medir sabão"), ("pl big", "OMO e COMFORT"), ("pl big", "já inclusos."))
      + '<p class="lead" style="margin-top:40px">Lava em cerca de <b>30 min</b> e seca em até <b>45 min</b>. '
        'Ambiente climatizado e <b>aberta 24h</b>.</p></div>'),
    # 7 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Bora lavar <em>do jeito certo?</em></h2>'),
]
print(salvar("LPBV-1111-12", sl))
