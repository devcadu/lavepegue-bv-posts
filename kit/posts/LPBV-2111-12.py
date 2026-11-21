"""LPBV-2111-12 — Dica de Lavagem (peças grandes): de quanto em quanto tempo lavar a roupa de cama — sáb 21/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
FONTE = '<p class="lead" style="margin-top:26px;font-size:22px;opacity:.85">Fonte: Canaltech</p>'
sl = [
    # 1 — capa
    s(1, N, "salao-interno-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Lençol, edredom, travesseiro…"), ("mg big", "De quanto em"), ("mg big ind1", "quanto tempo?"))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">O calendário da sua cama</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — toda semana
    s(2, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Toda semana</span>'
      '<h2 class="h md" style="margin-top:14px">Lençol e <em>fronha</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("nose", "Pegam <b>suor e oleosidade</b> de toda noite"),
               ("spark", "Suou muito ou ficou doente? <b>Lave antes</b>"),
               ("dryer", "<b>Seque bem</b> antes de forrar de novo")])
      + "</div>" + FONTE + "</div>"),
    # 3 — a cada 2 semanas
    s(3, N, "fachada-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">A cada 2 semanas</span>'
      '<h2 class="h md" style="margin-top:14px">Cobertor e <em>capa</em> de edredom</h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("closet", "Seguram <b>poeira do quarto</b>"),
               ("person", "Tem pet que sobe na cama? <b>Toda semana</b>")])
      + "</div>" + FONTE + "</div>"),
    # 4 — a cada poucos meses
    s(4, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">De tempos em tempos</span>'
      '<h2 class="h md" style="margin-top:14px">O <em>enchimento</em> também suja</h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("calendar", "<b>Edredom:</b> a cada 3 a 4 meses"),
               ("calendar", "<b>Travesseiro:</b> a cada 4 a 6 meses, se a etiqueta deixar")])
      + "</div>" + FONTE + "</div>"),
    # 5 — virada loja
    s(5, N, "entrada-vitrine-01", "veil",
      '<div class="area" style="top:380px"><span class="script">chegou a hora?</span>'
      + boxes(("cy", "Edredom não cabe"), ("pl big", "na sua"), ("pl big", "máquina?"))
      + '<p class="lead" style="margin-top:48px">Aqui lava em cerca de <b>30&nbsp;min</b> e seca em até <b>45&nbsp;min</b>, com OMO e COMFORT inclusos.</p></div>', wave=True),
    # 6 — CTA
    cta(N, "fachada-01", '<h2 class="h xl">Roupa de cama no dia? <em>Vem lavar.</em></h2>'),
]
print(salvar("LPBV-2111-12", sl))
