"""LPBV-1411-12 — Dica de Lavagem (edredom e peças grandes): 4 cuidados pra lavar edredom sem estragar — sáb 14/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 7
sl = [
    # 1 — capa
    s(1, N, "maquinas-tabela-02", "fade-bot",
      '<div class="area" style="bottom:110px">'
      + boxes(("cr", "Vai lavar o edredom?"), ("mg big", "4 cuidados pra"), ("mg big ind1", "não estragar."))
      + '<div style="margin-top:40px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">E ele voltar fofinho pra cama</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — etiqueta
    s(2, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Cuidado 1</span>'
      '<h2 class="h md" style="margin-top:14px">Leia a <em>etiqueta</em> antes</h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("closet", "Veja se pode ir na <b>máquina</b>"),
               ("dryer", "Confira se pode ir na <b>secadora</b>"),
               ("spark", "Pluma e pena pedem ciclo <b>delicado</b>")])
      + "</div></div>"),
    # 3 — um por vez
    s(3, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Cuidado 2</span>'
      '<h2 class="h md" style="margin-top:14px">Um edredom <em>por vez</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "Ele precisa de espaço pra <b>girar</b> e enxaguar"),
               ("nose", "Máquina lotada lava mal e deixa <b>cheiro</b>"),
               ("fold", "Peças grandes: nada de socar no cesto")])
      + "</div></div>"),
    # 4 — sabão na medida
    s(4, N, "entrada-vitrine-01", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Cuidado 3"), ("pl big", "sabão na"), ("pl big", "medida certa"))
      + '<p class="lead" style="margin-top:40px">Sabão demais fica preso no enchimento e deixa a peça dura. '
        'Aqui o <b>OMO</b> e o <b>COMFORT</b> já vêm inclusos no ciclo.</p></div>'),
    # 5 — secar até o fim
    s(5, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Cuidado 4 · o mais importante</span>'
      '<h2 class="h md" style="margin-top:14px">Seque <em>até o fim</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("rain", "Enchimento úmido pega <b>cheiro de guardado</b>"),
               ("dryer", "Apalpe o miolo: úmido? Mais um ciclo"),
               ("spark", "Bolinhas de tênis limpas ajudam a <b>afofar</b>")])
      + "</div></div>"),
    # 6 — virada Lave & Pegue
    s(6, N, "fachada-02", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cr", "Na Lave & Pegue"), ("mg big", "lava e seca"), ("mg big ind1", "numa ida só."))
      + '<p class="lead" style="margin-top:40px">Lavagem em cerca de <b>30 min</b> e secagem em até <b>45 min</b>. '
        'Tem atendente pra ajudar.</p></div>'),
    # 7 — CTA
    cta(N, "fachada-01", '<h2 class="h xl">Edredom fofinho, <em>sem sufoco.</em></h2>'),
]
print(salvar("LPBV-1411-12", sl))
