"""LPBV-2611-12 — Delivery (serviço, sem preço) — qui 26/11, 12h. Padrão v3.
Tema: quanto tempo a casa (e a roupa) leva da sua semana — o delivery devolve esse tempo.
Dado: IBGE, PNAD Contínua 2022 (outras formas de trabalho), via SBT News — pesquisado em 26/11/2026."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
FONTE = '<p class="lead" style="margin-top:26px;font-size:22px;opacity:.85">Fonte: IBGE (PNAD 2022), via SBT News</p>'

sl = [
    # 1 — capa: fachada + caixas empilhadas
    s(1, N, "fachada-02", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Quanto tempo a roupa leva da sua semana?"), ("mg big", "Esse tempo"), ("mg big ind1", "pode ser seu."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">A conta que ninguém faz</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — o dado
    s(2, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:290px"><span class="eyebrow">O tamanho da conta</span>'
      '<div class="price" style="margin-top:24px"><span class="n">21</span><span class="c">,3 horas</span></div>'
      '<div class="glass" style="margin-top:40px"><p class="lead">por semana: foi o tempo que as mulheres no Brasil '
      'gastaram com <b>afazeres de casa</b> em 2022. Os homens, <b>11,7 horas</b>. '
      'E <b>cuidar da roupa</b> entra nessa conta.</p></div>' + FONTE + '</div>'),
    # 3 — onde o tempo da roupa vai
    s(3, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Lavar em casa é mais que lavar</span>'
      '<h2 class="h md" style="margin-top:14px">Pra onde vai o seu <em>tempo</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "Separar, <b>lavar e enxaguar</b>"), ("clock", "<b>Esperar</b> a máquina terminar"),
               ("rain", "Estender e <b>torcer pra não chover</b>"), ("fold", "Recolher, <b>dobrar e guardar</b>")])
      + "</div></div>"),
    # 4 — como fica com o delivery
    s(4, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Com o delivery</span>'
      '<h2 class="h md" style="margin-top:14px">Sua parte fica <em>pequena</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["Junte a roupa no <b>cesto ou na sacola</b>", "Chame a gente no <b>WhatsApp</b>",
               "Receba tudo <b>lavado e seco</b> em casa"], numerada=True)
      + "</div></div>", wave=True),
    # 5 — virada
    s(5, N, "entrada-vitrine-01", "veil",
      '<div class="area" style="top:380px">'
      + boxes(("cy", "E o tempo que sobra?"), ("pl big", "Descanso,"), ("pl big", "família, você."))
      + '<p class="lead" style="margin-top:48px">Aqui a roupa é lavada com <b>OMO e COMFORT</b>, '
        'seca por completo e com <b>atendente</b> cuidando de tudo.</p></div>'),
    # 6 — CTA
    cta(N, "fachada-01", '<h2 class="h xl">Seu tempo vale mais. <em>Chama a gente.</em></h2>'),
]
print(salvar("LPBV-2611-12", sl))
