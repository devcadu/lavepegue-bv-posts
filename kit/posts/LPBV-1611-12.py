"""LPBV-1611-12 — Como Funciona — seg 16/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa: fachada + caixas empilhadas
    s(1, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Primeira vez na self-service?"), ("mg big", "É mais fácil"), ("mg big ind1", "do que parece."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Passo a passo pra estrear</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — antes de sair de casa
    s(2, N, "ia:ia-cesto-roupas-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Antes de sair de casa</span>'
      '<h2 class="h md" style="margin-top:14px">Deixe a roupa <em>pronta</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("closet", "Separe <b>brancas e coloridas</b>"), ("spark", "Esvazie os <b>bolsos</b>"), ("fold", "Feche <b>zíperes e botões</b>"), ("person", "Leve tudo numa <b>sacola ou cesto</b>")])
      + "</div></div>"),
    # 3 — lavar
    s(3, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Na loja</span>'
      '<h2 class="h md" style="margin-top:14px">Lavar em <em>3 passos</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["Coloque a roupa na lavadora <b>sem lotar</b>", "Pague o ciclo: <b>OMO e COMFORT inclusos</b>", "Em cerca de <b>30 min</b> está lavada"], numerada=True)
      + "</div></div>"),
    # 4 — secar + preço
    s(4, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:330px"><span class="script">cada ciclo sai por</span>'
      '<div class="price" style="margin-top:24px"><span class="rs">R$</span><span class="n">17</span><span class="c">,00</span></div>'
      f'<div class="pills" style="margin-top:56px"><span class="pill">{icon("washer")}Lava em ~30 min</span>'
      f'<span class="pill w">{icon("dryer")}Seca em até 45 min</span></div></div>', wave=True),
    # 5 — atendente
    s(5, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Sem tempo de ficar?</span>'
      '<h2 class="h md" style="margin-top:14px">O <em>atendente</em> faz pra você</h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("person", "Serviço de atendente: <b>R$ 10</b>"), ("fold", "Vale para <b>2 cestos</b>"), ("coin", "A partir do 3º cesto, <b>R$ 5 cada</b>"), ("clock", "Loja <b>aberta 24h</b>, climatizada")])
      + "</div></div>"),
    # 6 — CTA
    cta(N, "entrada-vitrine-01", '<h2 class="h xl">Bora fazer <em>a sua estreia?</em></h2>'),
]
print(salvar("LPBV-1611-12", sl))
