"""LPBV-2211-12 — Dica de Lavagem: mancha amarela de suor e desodorante na axila — dom 22/11, 12h. Padrão v3.
(Domingo = Quem Usa Aprova; sem texto real de avaliação copiado no kit, virou Dica de Lavagem, como manda a grade.)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa
    s(1, N, "fachada-02", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Camiseta branca com axila amarela?"), ("mg big", "Dá pra"), ("mg big ind1", "evitar!"))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Suor + desodorante no calor</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — por que acontece
    s(2, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Por que acontece</span>'
      '<h2 class="h md" style="margin-top:14px">É a <em>mistura</em> que mancha</h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("nose", "Suor junta com o <b>resíduo do desodorante</b>"),
               ("spark", "Lavagem após lavagem, <b>vai acumulando</b> no tecido"),
               ("rain", "No calor de Boa Vista a gente <b>sua mais</b>")])
      + "</div></div>"),
    # 3 — antes de vestir
    s(3, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Antes de vestir</span>'
      '<h2 class="h md" style="margin-top:14px">Espere o desodorante <em>secar</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("clock", "Dê <b>uns minutinhos</b> antes de pôr a camiseta"),
               ("spark", "<b>Menos produto</b> já resolve")])
      + "</div></div>"),
    # 4 — na lavagem
    s(4, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:280px"><span class="eyebrow">Na lavagem</span>'
      '<h2 class="h md" style="margin-top:14px">Não deixe a camiseta <em>esperando</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("closet", "Suada no cesto por dias? <b>Lave logo</b>"),
               ("washer", "Lave do <b>avesso</b> pra limpar bem a axila"),
               ("dryer", "Ainda manchada? <b>Trate antes</b> de secar no calor")])
      + "</div></div>"),
    # 5 — virada loja
    s(5, N, "entrada-vitrine-01", "veil",
      '<div class="area" style="top:380px"><span class="script">semana suada?</span>'
      + boxes(("cy", "Lave tudo"), ("pl big", "de uma"), ("pl big", "vez só"))
      + '<p class="lead" style="margin-top:48px">Aqui lava em cerca de <b>30&nbsp;min</b> e seca em até <b>45&nbsp;min</b>, com OMO e COMFORT inclusos.</p></div>', wave=True),
    # 6 — CTA
    cta(N, "fachada-01", '<h2 class="h xl">Camiseta suada? <em>Lava logo.</em></h2>'),
]
print(salvar("LPBV-2211-12", sl))
