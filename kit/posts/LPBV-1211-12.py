"""LPBV-1211-12 — Delivery (Combo) — qui 12/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa: imagem IA + caixas empilhadas + selo de preço
    s(1, N, "salao-interno-01", "fade-bot",
      '<div class="seal" style="right:64px;top:190px"><small>COMBO</small><b>R$49<sup>,90</sup></b><i>até 15/11</i></div>'
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Sem tempo pra lavar roupa essa semana?"), ("mg big", "A gente lava,"), ("mg big ind1", "seca e entrega."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Combo Delivery · até 15/11</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — o que vem: salão + cartão de vidro
    s(2, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Combo Delivery</span>'
      '<h2 class="h md" style="margin-top:14px">O que vem <em>no combo</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "1 lavagem"), ("dryer", "1 secagem"), ("person", "Atendimento"), ("scooter", "Entrega na sua casa")])
      + "</div></div>"),
    # 3 — preço: máquinas + preço gigante
    s(3, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:360px"><span class="script">tudo isso por</span>'
      '<div class="price" style="margin-top:24px"><span class="rs">R$</span><span class="n">49</span><span class="c">,90</span></div>'
      f'<div class="pills" style="margin-top:56px"><span class="pill">{icon("calendar")}De 05 a 15/11</span>'
      f'<span class="pill w">{icon("clock")}Das 14h às 19h</span></div></div>', wave=True),
    # 4 — onde fica: fachada + caixas
    s(4, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Você pede, a gente leva"), ("pl big", "roupa limpa"), ("pl big", "até a sua casa."))
      + '<p class="lead" style="margin-top:40px">📍 Loja no <b>Posto Trevo, Av. Venezuela, 16</b> — São Vicente. Aberta 24h.</p></div>'),
    # 5 — como pedir: porta + lista numerada
    s(5, N, "entrada-vitrine-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Como pedir</span>'
      '<h2 class="h md" style="margin-top:14px">Pedir é <em>simples</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["Chame no <b>WhatsApp</b> ou no direct", "Peça entre <b>14h e 19h</b>", "Combo válido <b>até 15/11</b>"], numerada=True)
      + "</div></div>"),
    # 6 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Bora deixar a roupa <em>em dia?</em></h2>'),
]
print(salvar("LPBV-1211-12", sl))
