"""LPBV-2711-12 — Na Loja: aberta 24h, a lavanderia que cabe no seu horário — sex 27/11, 12h. Padrão v3."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
from icons import icon

N = 6
sl = [
    # 1 — capa
    s(1, N, "entrada-vitrine-01", "fade-bot",
      '<div class="area" style="bottom:120px">'
      + boxes(("cr", "Sem tempo durante o dia?"), ("mg big", "A loja"), ("mg big ind1", "não fecha."))
      + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
        '<span class="lead" style="font-size:28px">Aberta 24h, todo dia</span>'
        f'<span class="swipe">Arrasta {icon("arrow")}</span></div></div>'),
    # 2 — horários
    s(2, N, "maquinas-tabela-02", "veil",
      '<div class="area" style="top:300px"><span class="eyebrow">Você escolhe a hora</span>'
      '<h2 class="h md" style="margin-top:14px">4 horários que <em>cabem</em> na rotina</h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("clock", "<b>Cedo</b>, antes do trabalho"),
               ("spark", "<b>Depois do expediente</b>, sem correria"),
               ("calendar", "<b>Na folga</b> ou no fim de semana"),
               ("closet", "<b>No fim do turno</b>, até de madrugada")])
      + "</div></div>"),
    # 3 — climatizado
    s(3, N, "salao-interno-01", "veil",
      '<div class="area" style="bottom:150px"><span class="eyebrow">Fugindo do calor</span>'
      '<h2 class="h md" style="margin-top:14px">Lá fora sol. Aqui, <em>climatizado.</em></h2>'
      '<p class="lead" style="margin-top:40px">Enquanto a máquina trabalha, você espera no ar-condicionado. E a criançada tem o <b>espaço kids</b>.</p></div>'),
    # 4 — tempo
    s(4, N, "maquinas-tabela-01", "veil",
      '<div class="area" style="bottom:150px">'
      + boxes(("cy", "Quanto tempo leva?"), ("pl big", "Cabe numa"), ("pl big", "pausa."))
      + '<p class="lead" style="margin-top:40px">Lava em cerca de <b>30 min</b> e seca em até <b>45 min</b>. Sabão OMO e amaciante COMFORT já inclusos.</p></div>'),
    # 5 — atendente e delivery
    s(5, N, "fachada-01", "veil",
      '<div class="area" style="top:330px"><span class="script">sem tempo nem pra isso?</span>'
      '<h2 class="h md" style="margin-top:14px">A gente <em>dá uma mão</em></h2>'
      '<div class="glass" style="margin-top:44px">'
      + ilist([("person", "Serviço de atendente: <b>cuida da lavagem pra você</b>"),
               ("scooter", "Delivery: <b>pede pelo WhatsApp</b>")])
      + "</div></div>", wave=True),
    # 6 — CTA
    cta(N, "fachada-02", '<h2 class="h xl">Seu horário, <em>sua lavanderia.</em></h2>'),
]
print(salvar("LPBV-2711-12", sl))
