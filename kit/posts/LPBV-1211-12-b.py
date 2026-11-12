"""LPBV-1211-12 (b) — Delivery: como preparar a roupa e pedir — qui 12/11, 12h. Padrão v3.
Arquivo com sufixo -b para não sobrescrever o exemplo aprovado LPBV-1211-12.py (Combo, publicado)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa
    s(1, N, "entrada-vitrine-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Vai pedir o delivery?"), ("mg big", "Prepare a roupa"), ("mg big ind1", "em 2 minutos."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Cuidados rápidos antes de mandar</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — bolsos e zíper
    s(2, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Antes de fechar a sacola</span>'
      '<h2 class="h md" style="margin-top:14px">Esvazie os <em>bolsos</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("coin", "Moedas, chaves e papel fora"), ("closet", "Zíper e botões fechados"),
               ("fold", "Peças do avesso protegem a cor")])
      + "</div></div>"),
    # 3 — separar e avisar
    s(3, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Separe e avise</span>'
      '<h2 class="h md" style="margin-top:14px">Conte o que <em>tem na sacola</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["Brancas <b>separadas</b> das coloridas", "Tem <b>mancha</b>? Diga onde e de quê",
               "Peça <b>delicada</b>? Leia a etiqueta e avise"], numerada=True)
      + "</div></div>"),
    # 4 — rotina
    s(4, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Enquanto isso, você segue"), ("pl big", "trabalhando,"), ("pl big", "estudando, vivendo."))
      + '<p class="lead" style="margin-top:40px">Sabão <b>OMO</b> e amaciante <b>COMFORT</b> já inclusos. Você não precisa levar nada.</p></div>'),
    # 5 — como pedir
    s(5, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Na hora de pedir</span>'
      '<h2 class="h md" style="margin-top:14px">É só <em>mandar um oi</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["Mande mensagem no <b>WhatsApp</b> ou no direct", "Diga <b>quantos cestos</b> e o que vai lavar",
               "Combo Delivery <b>R$ 49,90</b> até 15/11, das 14h às 19h"], numerada=True)
      + "</div></div>"),
    # 6 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Deixa a roupa <em>com a gente.</em></h2>'),
]
print(salvar("LPBV-1211-12-b", sl))
