"""LPBV-2311-12 — Como Funciona: o roteiro da visita, lavar e secar em cerca de 1h15 — seg 23/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa
    s(1, N, "maquinas-tabela-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Quanto tempo leva?"), ("mg big", "Lavar e secar"), ("mg big ind1", "em cerca de 1h15."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">O roteiro da sua visita</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — antes de sair
    s(2, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Antes de sair de casa</span>'
      '<h2 class="h md" style="margin-top:14px">Chegue com a roupa <em>pronta</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["<b>Esvazie os bolsos</b> (moeda, papel, chave)", "<b>Separe</b> claras de escuras", "<b>Feche zíperes</b> e botões de pressão"], numerada=True)
      + "</div></div>"),
    # 3 — minuto 0
    s(3, N, "fachada-01", "veil",
      '<div class="area" style="bottom:150px"><span class="script">minuto zero</span>'
      + boxes(("cy", "Roupa na lavadora:"), ("pl big", "sabão e"), ("pl big", "amaciante inclusos."))
      + '<p class="lead" style="margin-top:40px">A máquina já usa <b>OMO</b> e <b>COMFORT</b>. Você não precisa trazer nada.</p></div>'),
    # 4 — enquanto lava
    s(4, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Cerca de 30 min lavando</span>'
      '<h2 class="h md" style="margin-top:14px">Enquanto isso, <em>relaxa</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("spark", "Ambiente <b>climatizado</b>, longe do calor"),
               ("person", "<b>Espaço kids</b> pra quem vem com as crianças"),
               ("clock", "Ou aproveita pra <b>resolver algo</b> por perto")])
      + "</div></div>"),
    # 5 — secadora
    s(5, N, "fachada-02", "veil",
      '<div class="area" style="top:330px"><span class="eyebrow">Seca em até 45 min</span>'
      '<h2 class="h md" style="margin-top:14px">Parou a secadora? <em>Tira logo.</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("dryer", "Roupa parada no tambor <b>amassa mais</b>"),
               ("fold", "<b>Dobre ainda morna</b> e leve pronta pra gaveta")])
      + "</div></div>", wave=True),
    # 6 — CTA
    cta(N, "entrada-vitrine-01", '<h2 class="h xl">Lavou, secou, dobrou. <em>Vem testar.</em></h2>'),
]
print(salvar("LPBV-2311-12", sl))
