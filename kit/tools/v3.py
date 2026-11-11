"""Padrão v3 — foto em toda lâmina, Poppins, caixas empilhadas, cartão de vidro, logo centralizado."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from icons import icon

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POS = {"fachada-01": "center 18%", "fachada-02": "center 25%", "maquinas-tabela-01": "center 70%",
       "maquinas-tabela-02": "center 70%", "salao-interno-01": "center 55%", "entrada-vitrine-01": "center 45%"}

def img(nome):
    return f"../img/ia/{nome[3:]}.jpg" if nome.startswith("ia:") else f"../img/fotos/{nome}.jpg"

def bg(nome, pos=None):
    return f'<div class="bg" style="background-image:url({img(nome)});background-position:{pos or POS.get(nome, "center")}"></div>'

def hd():
    return ('<div class="hd"><span>Lavanderia</span><div class="lg"><b>LAVE &amp; PEGUE</b><i>LAVANDERIA</i></div>'
            '<span>Boa Vista · RR</span></div>')

def dots(i, n):
    return '<div class="dots">' + "".join(f'<span class="{"on" if k == i else ""}"></span>' for k in range(1, n + 1)) + "</div>"

WAVE = ('<svg class="wave" viewBox="0 0 1080 230" preserveAspectRatio="none"><path d="M0 120 C 260 40 520 210 1080 70 L1080 230 L0 230Z" fill="#12C6E3" opacity=".9"/>'
        '<path d="M0 170 C 300 110 600 240 1080 140 L1080 230 L0 230Z" fill="#A3237E"/></svg>')

def s(i, n, foto, overlay, body, pos=None, wave=False):
    return (f'<section class="s">{bg(foto, pos)}<div class="fade-top"></div><div class="{overlay}"></div>'
            f'{WAVE if wave else ""}{hd()}{body}{dots(i, n)}</section>')

def boxes(*linhas):
    """linhas: (classe, html) ex.: ('cr', 'texto'), ('mg big', 'chegou.')"""
    return '<div class="boxes">' + "".join(f'<span class="bx {c}">{t}</span>' for c, t in linhas) + "</div>"

def ilist(itens, numerada=False):
    out = '<ul class="ilist">'
    for k, it in enumerate(itens, 1):
        if numerada:
            out += f'<li><span class="n">{k}</span><span>{it}</span></li>'
        else:
            out += f'<li><span class="ic">{icon(it[0])}</span><span>{it[1]}</span></li>'
    return out + "</ul>"

def cta(n, foto, titulo_html):
    body = (f'<div class="area" style="top:300px">{titulo_html}'
            f'<div class="btn" style="margin-top:64px"><div class="bi">{icon("chat")}</div>Clique no botão Enviar mensagem</div>'
            '<p class="lead" style="margin-top:50px">ou chama no WhatsApp</p><div class="wpp">(95) 98115-2711</div></div>'
            '<div class="foot"><span>Posto Trevo · Av. Venezuela, 16 — São Vicente</span><span class="h24">Aberta 24h</span></div>')
    return s(n, n, foto, "veil-mag", body)

def pagina(t, slides):
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{t}</title>'
            f'<link rel="stylesheet" href="../v3.css"></head><body>{"".join(slides)}</body></html>')

def salvar(nome, slides):
    p = os.path.join(KIT, "modelos", f"{nome}.html")
    open(p, "w").write(pagina(nome, slides))
    return p
