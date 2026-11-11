"""Ponte com o GitHub (devcadu/lavepegue-bv-posts).

1) baixar(url, nome, formato)  -> pede ao robô "baixar-imagens" para trazer uma imagem de um site que este
   ambiente não acessa (ex.: export do Canva/ElevenLabs), espera chegar e recorta:
   retrato 1080x1440 · paisagem 1080x810 · original (sem recorte). Salva em img/ia/<nome>.jpg.
2) subir_slides(pasta_local, pasta_repo) -> copia os JPGs para lpbv/<pasta_repo>/, faz push e confere
   que cada URL pública responde 200 + image/jpeg. Devolve a lista de URLs na ordem.

Uso:
  python3 tools/baixar_imagens.py baixar "<url>" capa-0611 retrato
  python3 tools/baixar_imagens.py subir saida/2026-11-12_12 2026-11-12_12
"""
import os, sys, time, glob, shutil, subprocess, urllib.request
from PIL import Image

REPO_DIR = os.environ.get("LPBV_REPO", "/home/claude/lavepegue-bv-posts")
RAW = "https://raw.githubusercontent.com/devcadu/lavepegue-bv-posts/main/"
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def git(*args):
    subprocess.run(["git", "-C", REPO_DIR, *args], check=True)

def commit_push(msg):
    git("add", "-A")
    subprocess.run(["git", "-C", REPO_DIR, "-c", "user.name=Claude", "-c", "user.email=noreply@anthropic.com",
                    "commit", "-qm", msg], check=False)
    git("pull", "-q", "--rebase", "origin", "main")
    git("push", "-q", "origin", "HEAD:main")

def status(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url + f"?t={int(time.time())}", method="HEAD"), timeout=20) as r:
            return r.status, r.headers.get("Content-Type", "")
    except Exception as e:
        return getattr(e, "code", 0), ""

def esperar(url, limite=300):
    t0 = time.time()
    while time.time() - t0 < limite:
        c, ct = status(url)
        if c == 200:
            return True
        time.sleep(8)
    return False

def recortar(src, dst, formato):
    im = Image.open(src).convert("RGB")
    if formato in ("retrato", "paisagem"):
        W, H = (1080, 1440) if formato == "retrato" else (1080, 810)
        r = max(W / im.width, H / im.height)
        im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
        x, y = (im.width - W) // 2, (im.height - H) // 2
        im = im.crop((x, y, x + W, y + H))
    im.save(dst, quality=92)

def baixar(url, nome, formato="retrato"):
    destino = f"lpbv/_ia/{nome}.jpg"
    os.makedirs(os.path.join(REPO_DIR, "pedidos"), exist_ok=True)
    with open(os.path.join(REPO_DIR, "pedidos", f"{nome}.txt"), "w") as f:
        f.write(f"{destino}|{url}\n")
    commit_push(f"Pedido de imagem: {nome}")
    if not esperar(RAW + destino):
        raise SystemExit(f"Imagem {nome} não chegou em 5 min (ver Actions do repositório).")
    git("pull", "-q", "--rebase", "origin", "main")
    os.makedirs(os.path.join(KIT, "img/ia"), exist_ok=True)
    out = os.path.join(KIT, "img/ia", f"{nome}.jpg")
    recortar(os.path.join(REPO_DIR, destino), out, formato)
    print(out)
    return out

def subir_slides(pasta_local, pasta_repo):
    jpgs = sorted(f for f in glob.glob(os.path.join(pasta_local, "[0-9][0-9].jpg")))
    if not jpgs:
        raise SystemExit("Nenhum slide 01.jpg… na pasta.")
    alvo = os.path.join(REPO_DIR, "lpbv", pasta_repo)
    os.makedirs(alvo, exist_ok=True)
    for j in jpgs:
        shutil.copy(j, alvo)
    commit_push(f"Slides {pasta_repo}")
    urls = [f"{RAW}lpbv/{pasta_repo}/{os.path.basename(j)}" for j in jpgs]
    for u in urls:
        if not esperar(u, 180):
            raise SystemExit(f"URL não respondeu 200: {u}")
        c, ct = status(u)
        if "image/jpeg" not in ct:
            raise SystemExit(f"Tipo errado ({ct}): {u}")
    print("\n".join(urls))
    return urls

if __name__ == "__main__":
    if sys.argv[1] == "baixar":
        baixar(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "retrato")
    elif sys.argv[1] == "subir":
        subir_slides(sys.argv[2], sys.argv[3])
