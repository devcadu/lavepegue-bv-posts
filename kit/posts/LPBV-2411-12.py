"""LPBV-2411-12 — Dica de Lavagem: roupa preta e colorida desbotando — ter 24/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa
    s(1, N, "fachada-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Roupa preta ficando desbotada?"), ("mg big", "Tem jeito"), ("mg big ind1", "de evitar!"))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">4 cuidados que salvam a cor</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — por que desbota
    s(2, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Por que desbota</span>'
      '<h2 class="h md" style="margin-top:14px">O vilão é o <em>atrito</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "Peça <b>esfregando</b> em peça solta a tinta do tecido"),
               ("rain", "<b>Água quente</b> ajuda a cor a sair"),
               ("spark", "<b>Sol forte</b> no varal queima a cor")])
      + "</div></div>"),
    # 3 — antes de lavar
    s(3, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Antes de lavar</span>'
      '<h2 class="h md" style="margin-top:14px">Vire tudo do <em>avesso</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("closet", "O lado de fora fica <b>protegido</b> do atrito"),
               ("fold", "Escuras e jeans <b>juntos</b>, longe das claras")])
      + "</div></div>"),
    # 4 — na lavagem e secagem
    s(4, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:280px"><span class="eyebrow">Na lavagem</span>'
      '<h2 class="h md" style="margin-top:14px">Menos é <em>mais</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "<b>Não lote</b> a máquina: a roupa precisa de espaço"),
               ("spark", "Sabão <b>na medida</b>, sem exagero"),
               ("dryer", "Nada de <b>sol forte</b>: seque à sombra ou na secadora, seguindo a etiqueta")])
      + "</div></div>"),
    # 5 — virada loja
    s(5, N, "entrada-vitrine-01", "veil",
      '<div class="area" style="top:380px"><span class="script">sem sol na roupa</span>'
      + boxes(("cy", "Lava e seca"), ("pl big", "longe do"), ("pl big", "sol forte"))
      + '<p class="lead" style="margin-top:48px">Aqui lava em cerca de <b>30&nbsp;min</b> e seca em até <b>45&nbsp;min</b>, com OMO e COMFORT inclusos.</p></div>', wave=True),
    # 6 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Cor viva por <em>mais tempo.</em></h2>'),
]
print(salvar("LPBV-2411-12", sl))
