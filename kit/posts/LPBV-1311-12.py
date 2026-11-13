"""LPBV-1311-12 — Na Loja: por dentro da loja (climatizada, máquinas, OMO/COMFORT, 24h, atendente) — sex 13/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
FONTE = '<p class="lead" style="margin-top:22px;font-size:22px;opacity:.85">Fonte: Brasil 61 (previsão para Boa Vista, nov/2026)</p>'
sl = [
    # 1 — capa
    s(1, N, "salao-interno-01", "fade-bot",
      '<div class="area" style="bottom:110px">'
      + boxes(("cr", "Lá fora, máxima de 38 °C."), ("mg big", "Aqui dentro,"), ("mg big ind1", "ar gelado."))
      + '<div style="margin-top:40px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Vem conhecer a loja por dentro</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div>' + FONTE + '</div>'),
    # 2 — máquinas
    s(2, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Máquinas automáticas</span>'
      '<h2 class="h md" style="margin-top:14px">Lava e seca <em>sem complicação</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "Lavagem em cerca de <b>30 min</b>"), ("dryer", "Secagem em até <b>45 min</b>"),
               ("coin", "<b>R$ 17</b> por ciclo, lavar ou secar")])
      + "</div></div>"),
    # 3 — OMO e COMFORT inclusos
    s(3, N, "entrada-vitrine-01", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Pode vir de mãos vazias"), ("pl big", "sabão OMO e"), ("pl big", "amaciante COMFORT"))
      + '<p class="lead" style="margin-top:40px">Já estão <b>inclusos</b> no ciclo. É só trazer a roupa.</p></div>'),
    # 4 — atendente e conforto
    s(4, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Não sabe por onde começar?</span>'
      '<h2 class="h md" style="margin-top:14px">Tem <em>atendente</em> pra ajudar</h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("person", "Serviço de atendente: <b>R$ 10</b> para 2 cestos"),
               ("coin", "A partir do 3º cesto, <b>R$ 5</b> cada"),
               ("spark", "Espaço kids pra criançada esperar")])
      + "</div></div>"),
    # 5 — 24h
    s(5, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cr", "Saiu tarde do trabalho?"), ("mg big", "Aberta 24h."), ("mg big ind1", "Vem quando der."))
      + '<p class="lead" style="margin-top:40px">Você lava no horário que cabe na <b>sua</b> rotina.</p></div>'),
    # 6 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Foge do calor e <em>vem lavar.</em></h2>'),
]
print(salvar("LPBV-1311-12", sl))
