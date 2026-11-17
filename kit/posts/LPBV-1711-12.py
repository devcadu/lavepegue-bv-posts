"""LPBV-1711-12 — Dica de Lavagem — ter 17/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa: fachada-02 + caixas empilhadas
    s(1, N, "fachada-02", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Toalha áspera e durinha?"), ("mg big", "Dá pra deixar"), ("mg big ind1", "fofinha de novo."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Dicas pra toalha macia</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — por que fica dura
    s(2, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Por que acontece</span>'
      '<h2 class="h md" style="margin-top:14px">O vilão é o <em>resíduo</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "<b>Sabão demais</b> fica preso nas fibras"), ("spark", "<b>Amaciante em excesso</b> faz a toalha secar menos"), ("fold", "<b>Máquina lotada</b> não enxágua direito"), ("clock", "<b>Sol forte</b> por horas resseca os fios")])
      + "</div></div>"),
    # 3 — na lavagem
    s(3, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Na lavagem</span>'
      '<h2 class="h md" style="margin-top:14px">Lave do <em>jeito certo</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["Lave as toalhas <b>separadas</b> das outras roupas", "<b>Não lote</b> a máquina: elas precisam girar", "Sabão e amaciante <b>na medida</b>, sem exagero"], numerada=True)
      + "</div></div>"),
    # 4 — na secagem
    s(4, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Na secagem</span>'
      '<h2 class="h md" style="margin-top:14px">Seque até o <em>fim</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("spark", "<b>Sacuda</b> a toalha antes de secar"), ("dryer", "A <b>secadora</b> deixa os fios soltinhos"), ("nose", "Nunca guarde <b>úmida</b>: dá cheiro"), ("fold", "Dobre só quando estiver <b>bem seca</b>")])
      + "</div></div>"),
    # 5 — na Lave & Pegue
    s(5, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Na Lave &amp; Pegue</span>'
      '<h2 class="h md" style="margin-top:14px">Sabão e amaciante&nbsp;<em>inclusos</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "Lavadora <b>R$ 17</b>, cerca de 30 min"), ("dryer", "Secadora <b>R$ 17</b>, até 45 min"), ("spark", "<b>OMO e COMFORT</b> já no ciclo"), ("clock", "<b>Aberta 24h</b> e climatizada")])
      + "</div></div>", wave=True),
    # 6 — CTA
    cta(N, "fachada-01", '<h2 class="h xl">Bora deixar a toalha <em>fofinha?</em></h2>'),
]
print(salvar("LPBV-1711-12", sl))
