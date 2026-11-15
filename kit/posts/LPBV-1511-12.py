"""LPBV-1511-12 — Delivery (último dia do Combo) — dom 15/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa: porta da loja + caixas empilhadas + selo
    s(1, N, "entrada-vitrine-01", "fade-bot",
      '<div class="seal" style="right:64px;top:190px"><small>COMBO</small><b>R$49<sup>,90</sup></b><i>só hoje</i></div>'
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Último dia do Combo Delivery"), ("mg big", "É hoje,"), ("mg big ind1", "até as 19h."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Domingo, 15/11 · 14h às 19h</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — o que entra: salão + cartão de vidro
    s(2, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Num pedido só</span>'
      '<h2 class="h md" style="margin-top:14px">Tudo isso <em>resolvido</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "Lavagem com OMO"), ("dryer", "Secagem completa"), ("person", "Atendente cuida de tudo"), ("scooter", "Volta pra sua casa")])
      + "</div></div>"),
    # 3 — preço: máquinas + preço gigante
    s(3, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:360px"><span class="script">última chance por</span>'
      '<div class="price" style="margin-top:24px"><span class="rs">R$</span><span class="n">49</span><span class="c">,90</span></div>'
      f'<div class="pills" style="margin-top:56px"><span class="pill">{icon("calendar")}Só hoje, 15/11</span>'
      f'<span class="pill w">{icon("clock")}Das 14h às 19h</span></div></div>', wave=True),
    # 4 — antes de chamar: cesto + lista
    s(4, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Perfeito pra</span>'
      '<h2 class="h md" style="margin-top:14px">Fechar o domingo <em>em dia</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("closet", "A roupa da semana <b>acumulada</b>"), ("fold", "Toalhas e lençóis <b>de uma vez</b>"), ("calendar", "Começar a segunda <b>com tudo limpo</b>"), ("spark", "Domingo livre <b>pra descansar</b>")])
      + "</div></div>"),
    # 5 — como pedir: máquinas + numerada
    s(5, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Como pedir hoje</span>'
      '<h2 class="h md" style="margin-top:14px">Em <em>3 passos</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["Chame no <b>WhatsApp</b> ou no direct", "Faça o pedido <b>entre 14h e 19h</b>", "Receba a roupa <b>limpa e seca</b>"], numerada=True)
      + "</div></div>"),
    # 6 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Último dia: <em>bora aproveitar?</em></h2>'),
]
print(salvar("LPBV-1511-12", sl))
