"""LPBV-1911-12 — Delivery (serviço, sem preço) — qui 19/11, 12h. Padrão v3.
Tema: 4 sinais de que é hora de chamar o delivery."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa: fachada + caixas empilhadas
    s(1, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Roupa suja acumulando?"), ("mg big", "Tá na hora"), ("mg big ind1", "do delivery."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">4 sinais pra ficar de olho</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — sinais 1 e 2
    s(2, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Sinais 1 e 2</span>'
      '<h2 class="h md" style="margin-top:14px">O cesto <em>transbordou</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("closet", "A roupa da semana <b>virou montanha</b>"), ("clock", "O dia acaba e <b>não sobra tempo</b>")])
      + "</div></div>"),
    # 3 — sinais 3 e 4
    s(3, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Sinais 3 e 4</span>'
      '<h2 class="h md" style="margin-top:14px">Falta <em>espaço</em> em casa</h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("fold", "Toalha e lençol <b>pedindo troca</b>"), ("rain", "Apê pequeno, <b>sem lugar pra secar</b>")])
      + "</div></div>"),
    # 4 — o que a gente faz
    s(4, N, "entrada-vitrine-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Você chama, a gente resolve</span>'
      '<h2 class="h md" style="margin-top:14px">Do cesto à <em>sua porta</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "Lavagem com <b>OMO e COMFORT</b>"), ("dryer", "Secagem <b>completa</b>"),
               ("person", "Atendente <b>cuidando de tudo</b>"), ("scooter", "Roupa <b>de volta em casa</b>")])
      + "</div></div>", wave=True),
    # 5 — virada emocional
    s(5, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:380px"><span class="script">e o melhor:</span>'
      + boxes(("cy", "Enquanto a roupa lava,"), ("pl big", "seu tempo"), ("pl big", "fica com você."))
      + '<p class="lead" style="margin-top:48px">Sem fila, sem varal, sem pilha no canto do quarto.</p></div>'),
    # 6 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Bateu um dos sinais? <em>Chama a gente.</em></h2>'),
]
print(salvar("LPBV-1911-12", sl))
