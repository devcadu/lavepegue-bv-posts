"""Renderiza cada <section class="slide"> de um HTML em JPG 1080x1350 e gera a folha de contato.

Uso: python3 render.py modelos/arquivo.html saida/pasta
Também confere: texto cortado/fora do slide, texto perto do rodapé (zona de 110px) e palavra órfã em títulos.
"""
import sys, os, json
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

CHECK_JS = r"""
(sec) => {
  const R = sec.getBoundingClientRect(), out = [];
  const SAFE = 110;  // rodapé livre (exceto elementos do rodapé fixo)
  const walker = document.createTreeWalker(sec, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    if (!n.textContent.trim()) continue;
    const el = n.parentElement;
    if (el.closest('.ph')) continue;  // rótulos do espaço reservado
    const rg = document.createRange(); rg.selectNodeContents(n);
    for (const r of rg.getClientRects()) {
      const b = r.bottom - R.top, l = r.left - R.left, rr = r.right - R.left, t = r.top - R.top;
      if (l < 0 || rr > R.width + 1 || t < 0 || b > R.height)
        out.push('CORTADO: ' + n.textContent.trim().slice(0, 40));
      else if (b > R.height - SAFE + 30 && !el.closest('.foot,.handle,.swipe,.panel'))
        out.push('PERTO DO RODAPÉ: ' + n.textContent.trim().slice(0, 40));
    }
  }
  // sobreposição de texto com espaço reservado de imagem
  const phs = [...sec.querySelectorAll('.ph.round,.ph.bleed')].map(p => p.getBoundingClientRect());
  sec.querySelectorAll('.content, .area').forEach(c => {
    const cr = c.getBoundingClientRect();
    phs.forEach(p => { if (cr.bottom > p.top + 2) out.push('TEXTO EM CIMA DA IMAGEM (' + Math.round(cr.bottom - p.top) + 'px)'); });
  });
  // palavra órfã: última linha de título com uma só palavra
  sec.querySelectorAll('h1,h2,p').forEach(h => {
    const rg = document.createRange(); rg.selectNodeContents(h);
    const lines = {};
    const w = document.createTreeWalker(h, NodeFilter.SHOW_TEXT); let t;
    while ((t = w.nextNode())) {
      const words = t.textContent.split(/\s+/).filter(Boolean);
      let idx = 0;
      for (const word of words) {
        const i = t.textContent.indexOf(word, idx); idx = i + word.length;
        const r2 = document.createRange(); r2.setStart(t, i); r2.setEnd(t, idx);
        const top = Math.round(r2.getBoundingClientRect().top / 10);
        (lines[top] = lines[top] || []).push(word);
      }
    }
    const ks = Object.keys(lines).map(Number).sort((a, b) => a - b);
    if (ks.length > 1 && lines[ks[ks.length - 1]].length === 1 && lines[ks[ks.length - 1]][0].length < 10)
      out.push('ÓRFÃ: "' + lines[ks[ks.length - 1]][0] + '" em ' + h.tagName);
  });
  return out;
}
"""

def render(html, outdir):
    os.makedirs(outdir, exist_ok=True)
    files, problems = [], {}
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(html))
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        for i, sec in enumerate(pg.query_selector_all("section.slide, section.s"), 1):
            png = os.path.join(outdir, f"{i:02d}.png")
            sec.screenshot(path=png)
            jpg = png[:-4] + ".jpg"
            Image.open(png).convert("RGB").save(jpg, quality=92)
            os.remove(png)
            files.append(jpg)
            issues = sec.evaluate(CHECK_JS)
            if issues:
                problems[f"{i:02d}"] = issues
        b.close()
    sheet(files, os.path.join(outdir, "folha.jpg"))
    return files, problems

def sheet(files, out, w=360):
    h = int(w * 1350 / 1080); gap = 24; lab = 40
    W = len(files) * (w + gap) + gap; H = h + gap * 2 + lab
    im = Image.new("RGB", (W, H), "#2b2b2b"); d = ImageDraw.Draw(im)
    try:
        f = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 22)
    except Exception:
        f = None
    for k, fp in enumerate(files):
        x = gap + k * (w + gap)
        im.paste(Image.open(fp).resize((w, h)), (x, gap + lab))
        d.text((x, gap + 6), f"{k+1:02d}", fill="#fff", font=f)
    im.save(out, quality=88)

if __name__ == "__main__":
    files, problems = render(sys.argv[1], sys.argv[2])
    print(len(files), "slides ->", sys.argv[2])
    print(json.dumps(problems, ensure_ascii=False, indent=1) if problems else "checagem: ok")
