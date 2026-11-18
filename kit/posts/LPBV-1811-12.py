"""LPBV-1811-12 — Mito x Verdade — qua 18/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 7

def selo(txt, cls):
    return boxes((cls, txt))

sl = [
    # 1 — capa
    s(1, N, "entrada-vitrine-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Secadora estraga a roupa?"), ("mg big", "Mito ou"), ("mg big ind1", "verdade?"))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">4 crenças sobre secar roupa</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — estraga tudo
    s(2, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:290px">' + selo("MITO", "mg big")
      + '<h2 class="h md" style="margin-top:30px">Secadora estraga <em>qualquer</em> roupa</h2>'
      '<div class="glass" style="margin-top:40px"><p class="lead"><b>Algodão, poliéster e misturas</b> aguentam bem o calor moderado. '
      'O desgaste vem de <b>temperatura alta</b> e tempo demais.</p></div></div>'),
    # 3 — peças que não vão
    s(3, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:290px">' + selo("VERDADE", "cy big")
      + '<h2 class="h md" style="margin-top:30px">Tem peça que <em>não vai</em></h2>'
      '<div class="glass" style="margin-top:40px"><p class="lead"><b>Seda, lã, renda, bordados e paetês</b> sofrem com o calor. '
      'Na dúvida, olhe a <b>etiqueta</b>: símbolo da secadora com X, não seca nela.</p></div></div>'),
    # 4 — encolhe
    s(4, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:290px">' + selo("MITO", "mg big")
      + '<h2 class="h md" style="margin-top:30px">Toda roupa <em>encolhe</em> na secadora</h2>'
      '<div class="glass" style="margin-top:40px"><p class="lead">Quem encolhe mais são as <b>fibras naturais</b> no calor alto. '
      'Seguindo a etiqueta e <b>sem lotar</b>, dá pra evitar.</p></div></div>'),
    # 5 — tirar logo
    s(5, N, "fachada-02", "veil",
      '<div class="area" style="top:290px">' + selo("VERDADE", "cy big")
      + '<h2 class="h md" style="margin-top:30px">Tirar logo <em>evita</em> amassado</h2>'
      '<div class="glass" style="margin-top:40px">'
      + ilist([("clock", "Acabou o ciclo? <b>Tire na hora</b>"), ("spark", "<b>Sacuda</b> as peças ainda mornas"), ("fold", "<b>Dobre</b> antes de esfriar")])
      + "</div></div>"),
    # 6 — virada Lave & Pegue
    s(6, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Roupa seca sem depender do varal"), ("pl big", "Seca em"), ("pl big", "até 45 min."))
      + '<p class="lead" style="margin-top:40px">Secadora <b>R$ 17</b> o ciclo, ambiente climatizado e '
        '<b>aberta 24h</b>. Lavou aqui? <b>OMO e COMFORT</b> já inclusos.</p></div>'),
    # 7 — CTA
    cta(N, "salao-interno-01", '<h2 class="h xl">Bora secar <em>do jeito certo?</em></h2>'),
]
print(salvar("LPBV-1811-12", sl))
