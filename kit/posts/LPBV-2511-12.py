"""LPBV-2511-12 — Mito x Verdade: roupa nova precisa lavar antes de usar? — qua 25/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 7
FONTE = '<p class="lead" style="margin-top:26px;font-size:22px;opacity:.85">Fonte: Correio Braziliense</p>'

def selo(txt, cls):
    return boxes((cls, txt))

sl = [
    # 1 — capa
    s(1, N, "salao-interno-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Roupa nova pode usar direto?"), ("mg big", "Mito ou"), ("mg big ind1", "verdade?"))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">4 crenças sobre a 1ª lavagem</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — já vem limpa
    s(2, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:290px">' + selo("MITO", "mg big")
      + '<h2 class="h md" style="margin-top:30px">Roupa nova já vem <em>limpa</em></h2>'
      '<div class="glass" style="margin-top:40px"><p class="lead">Antes de chegar em você, a peça passou por '
      '<b>fábrica, transporte e loja</b>. E muita gente pode ter <b>provado</b>.</p></div></div>'),
    # 3 — química
    s(3, N, "fachada-02", "veil",
      '<div class="area" style="top:290px">' + selo("VERDADE", "cy big")
      + '<h2 class="h md" style="margin-top:30px">Pode ter <em>química</em> no tecido</h2>'
      '<div class="glass" style="margin-top:40px"><p class="lead">Restos de <b>corante, fixador e resina anti-amassado</b> '
      'podem dar <b>coceira e vermelhidão</b>, principalmente em pele sensível.</p></div>' + FONTE + '</div>'),
    # 4 — só íntima
    s(4, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:290px">' + selo("MITO", "mg big")
      + '<h2 class="h md" style="margin-top:30px">Só peça íntima precisa <em>lavar</em></h2>'
      '<div class="glass" style="margin-top:40px">'
      + ilist([("closet", "Vale lavar <b>tudo que encosta na pele</b>"),
               ("fold", "Camiseta, pijama, <b>lençol e toalha</b> novos também")])
      + "</div></div>"),
    # 5 — 1ª lavagem com cuidado
    s(5, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:290px">' + selo("VERDADE", "cy big")
      + '<h2 class="h md" style="margin-top:30px">A 1ª lavagem pede <em>cuidado</em></h2>'
      '<div class="glass" style="margin-top:40px">'
      + ilist([("washer", "Colorida nova vai <b>separada</b>: pode soltar tinta"),
               ("closet", "<b>Do avesso</b> e sem lotar a máquina"),
               ("spark", "Sabão <b>na medida</b> e olho na <b>etiqueta</b>")])
      + "</div></div>"),
    # 6 — virada Lave & Pegue
    s(6, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Comprou roupa nova?"), ("pl big", "Estreia"), ("pl big", "lavadinha."))
      + '<p class="lead" style="margin-top:40px">Aqui lava em cerca de <b>30&nbsp;min</b> e seca em até <b>45&nbsp;min</b>, '
        'com <b>OMO e COMFORT</b> inclusos. <b>Aberta 24h</b>.</p></div>'),
    # 7 — CTA
    cta(N, "entrada-vitrine-01", '<h2 class="h xl">Roupa nova, <em>pronta pra usar.</em></h2>'),
]
print(salvar("LPBV-2511-12", sl))
