"""LPBV-2811-12 — Dica de Lavagem (peças grandes): cortina também vai pra máquina — sáb 28/11, 12h. Padrão v3, capa_cartao."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 7
FONTE = '<p class="lead" style="margin-top:26px;font-size:22px;opacity:.85">Fonte: Correio Braziliense</p>'
sl = [
    # 1 — capa (modelo do sábado: capa_cartao, imagem de IA nova)
    capa_cartao(N, "ia:ia-cortina-janela-01", "Peças grandes", "Cortina também <em>vai pra máquina?</em>",
                "Vai, sim. Veja como lavar sem estragar", pos="center 45%"),
    # 2 — de quanto em quanto tempo
    s(2, N, "ia:ia-cortina-janela-01", "veil",
      '<div class="area" style="bottom:150px"><span class="eyebrow">Ela junta mais do que parece</span>'
      '<h2 class="h md" style="margin-top:14px">Poeira, cheiro e <em>sol</em> o dia todo</h2>'
      '<p class="lead" style="margin-top:40px">A recomendação é uma limpeza completa a cada <b>6 meses</b>. '
      'Casa com muito movimento, bicho ou perto de rua movimentada? <b>Antes disso.</b></p>' + FONTE + '</div>',
      pos="center 30%"),
    # 3 — antes de lavar
    s(3, N, "ia:ia-cortina-dobrada-01", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Antes de lavar</span>'
      '<h2 class="h md" style="margin-top:14px">Prepare <em>a cortina</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("closet", "<b>Leia a etiqueta</b>: tecido técnico ou resinado pede outro cuidado"),
               ("spark", "<b>Tire ganchos e argolas</b> pra não rasgar o tecido"),
               ("nose", "<b>Sacuda a poeira</b> e trate a mancha antes")])
      + "</div></div>", pos="center 60%"),
    # 4 — na máquina
    s(4, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Na máquina</span>'
      '<h2 class="h md" style="margin-top:14px">Lave <em>com calma</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist(["<b>Sozinha</b>, sem lotar a máquina", "Ciclo <b>delicado</b> e água fria",
               "Dobrada ou dentro de uma <b>fronha fechada</b>"], numerada=True)
      + "</div></div>"),
    # 5 — secar
    s(5, N, "ia:ia-varal-sol-01", "veil",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "E pra secar?"), ("pl big", "Sem torcer,"), ("pl big", "sem pressa."))
      + '<p class="lead" style="margin-top:40px">Centrifugação leve e nada de torcer. Pendure ainda úmida no varão: '
        'o peso da água ajuda a <b>desamassar</b>. Secadora só se a etiqueta deixar.</p></div>'),
    # 6 — na loja
    s(6, N, "salao-interno-01", "veil",
      '<div class="area" style="top:330px"><span class="script">não cabe na sua máquina?</span>'
      '<h2 class="h md" style="margin-top:14px">Peça grande <em>é com a gente</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("washer", "Sabão OMO e amaciante COMFORT <b>já inclusos</b>"),
               ("clock", "Lava em cerca de <b>30 min</b>"),
               ("person", "Serviço de atendente <b>se precisar</b>"),
               ("calendar", "<b>Aberta 24h</b>, no seu horário")])
      + "</div></div>", wave=True),
    # 7 — CTA
    cta(N, "entrada-vitrine-01", '<h2 class="h xl">Cortina limpa, <em>casa nova.</em></h2>'),
]
print(salvar("LPBV-2811-12", sl))
