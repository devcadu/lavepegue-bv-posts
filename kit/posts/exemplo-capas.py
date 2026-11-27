"""Exemplo dos 4 modelos de capa (27/11/2026). Textos só de demonstração — não é post."""
import sys; import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
from v3 import *
N=6
sl=[
 capa_topo(N,"ia:ia-toalhas-01","Dica de lavagem","Toalha áspera? <em>Tem volta.</em>","3 erros que deixam a toalha dura e como evitar", pos="center 60%"),
 capa_cor(N,"ia:ia-varal-sol-01","mg","Mito x Verdade","Sol forte <em>desbota</em> a roupa?","4 crenças sobre secar roupa no calor de Boa Vista", pos="center 30%"),
 capa_cartao(N,"ia:ia-edredom-cama-01","Edredom e peças grandes","Edredom: de quanto em <em>quanto tempo?</em>","O calendário da sua roupa de cama", pos="center 60%"),
 capa_foto(N,"salao-interno-01","Sem tempo durante o dia?","A loja","não fecha.","Aberta 24h, todo dia"),
 capa_cor(N,"ia:ia-cesto-roupas-01","cy","Delivery","A roupa vai <em>e volta</em> limpinha.","Você chama no WhatsApp, a gente cuida do resto", pos="center 50%"),
 capa_cor(N,"ia:ia-toalhas-01","pl","Como funciona","Primeira vez na <em>self-service?</em>","O passo a passo pra estrear sem dúvida", pos="center 60%"),
]
salvar("exemplo-capas", sl)
