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


# ===== Capas variadas (27/11/2026) =====
# Regra: o feed não pode ficar igual. Alternar os modelos de capa e NUNCA repetir
# a mesma imagem de capa em 14 dias. Ver GUIA §5.1.
#   capa_foto   — foto real da loja, caixas embaixo (o modelo antigo; no máx. 1x por semana)
#   capa_topo   — imagem temática de IA em tela cheia, título grande no topo
#   capa_cartao — fundo creme, título escuro, imagem em cartão inclinado
#   capa_cor    — fundo de cor cheia (mg / cy / pl), título enorme, imagem em círculo

def _swipe(txt):
    return f'<span class="swipe">{txt} {icon("arrow")}</span>'

def capa_foto(n, foto, gancho, linha1, linha2, rodape, pos=None):
    return s(1, n, foto, "fade-bot",
             '<div class="area" style="bottom:120px">'
             + boxes(("cr", gancho), ("mg big", linha1), ("mg big ind1", linha2))
             + '<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center">'
               f'<span class="lead" style="font-size:28px">{rodape}</span>{_swipe("Arrasta")}</div></div>', pos=pos)

def capa_topo(n, foto, tag, titulo_html, sub, pos=None):
    return (f'<section class="s cap-topo">{bg(foto, pos)}<div class="fade-top-big"></div>{hd()}'
            f'<div class="area" style="top:200px"><span class="tag">{tag}</span>'
            f'<h1 class="h" style="margin-top:30px">{titulo_html}</h1><span class="ul"></span>'
            f'<p class="lead" style="max-width:820px">{sub}</p></div>'
            f'<div class="area" style="bottom:110px;text-align:right">{_swipe("Arrasta")}</div>{dots(1, n)}</section>')

def capa_cartao(n, foto, tag, titulo_html, sub, pos=None):
    return (f'<section class="s creme cap-cartao"><div class="blob"></div>'
            f'<div class="card" style="background-image:url({img(foto)});background-position:{pos or POS.get(foto, "center")}"></div>'
            f'<div class="hd dk"><span>Lavanderia</span><div class="lg"><b>LAVE &amp; PEGUE</b><i>LAVANDERIA</i></div><span>Boa Vista · RR</span></div>'
            f'<div class="area" style="top:190px"><span class="tag mg">{tag}</span>'
            f'<h1 class="h" style="margin-top:26px">{titulo_html}</h1><p class="sub">{sub}</p></div>'
            f'<div style="position:absolute;left:64px;bottom:150px;z-index:6">{_swipe("Arrasta")}</div>'
            f'{dots(1, n).replace("class=\"dots\"", "class=\"dots dk\"")}</section>')

def capa_cor(n, foto, cor, tag, titulo_html, sub, pos=None):
    """cor: 'mg' (magenta), 'cy' (ciano) ou 'pl' (ameixa)."""
    tg = "pl" if cor == "cy" else ""
    lead = 'color:var(--plum)' if cor == "cy" else ''
    return (f'<section class="s cor-{cor} cap-cor">'
            f'<div class="circ" style="background-image:url({img(foto)});background-position:{pos or POS.get(foto, "center")}"></div>'
            f'{hd() if cor != "cy" else hd().replace("class=\"hd\"", "class=\"hd dk\"")}'
            f'<div class="area" style="top:200px"><span class="tag {tg}">{tag}</span>'
            f'<h1 class="h" style="margin-top:28px">{titulo_html}</h1>'
            f'<p class="lead" style="margin-top:26px;max-width:560px;{lead}">{sub}</p></div>'
            f'<div class="sw">{_swipe("Arrasta")}</div>'
            f'{dots(1, n).replace("class=\"dots\"", "class=\"dots dk\"") if cor == "cy" else dots(1, n)}</section>')
