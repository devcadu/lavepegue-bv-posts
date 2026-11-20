"""LPBV-2011-12 — Na Loja: como separar a roupa em casa e lavar as pilhas lado a lado na loja — sex 20/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa
    s(1, N, "entrada-vitrine-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Roupa branca ficando cinza?"), ("mg big", "O segredo"), ("mg big ind1", "tá no cesto."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Como separar antes de vir</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — 3 pilhas
    s(2, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Antes de sair de casa</span>'
      '<h2 class="h md" style="margin-top:14px">Separe em <em>3 pilhas</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["<b>Brancas e claras</b> juntas", "<b>Coloridas</b> em outra", "<b>Escuras e jeans</b> por último"], numerada=True)
      + "</div></div>"),
    # 3 — quem vai separado
    s(3, N, "salao-interno-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Atenção redobrada</span>'
      '<h2 class="h md" style="margin-top:14px">Essas vão <em>à parte</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("spark", "Peça colorida nova: <b>pode soltar tinta</b>"),
               ("fold", "Toalhas: <b>soltam fiapo</b> nas outras roupas"),
               ("closet", "Delicadas: <b>confira a etiqueta</b> antes")])
      + "</div></div>"),
    # 4 — na loja: uma pilha por máquina
    s(4, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Aqui na loja é fácil:"), ("pl big", "uma pilha"), ("pl big", "por máquina."))
      + '<p class="lead" style="margin-top:40px">As lavadoras ficam lado a lado: as pilhas lavam <b>ao mesmo tempo</b>, em cerca de 30 min.</p></div>'),
    # 5 — resultado
    s(5, N, "fachada-01", "veil",
      '<div class="area" style="top:380px"><span class="script">e o resultado:</span>'
      + boxes(("cy", "Separou certo?"), ("pl big", "Branco segue"), ("pl big", "branco."))
      + '<p class="lead" style="margin-top:48px">E a camiseta escura não volta cheia de fiapo de toalha.</p></div>', wave=True),
    # 6 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Separou as pilhas? <em>Vem lavar.</em></h2>'),
]
print(salvar("LPBV-2011-12", sl))
