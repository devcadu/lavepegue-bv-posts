# lavepegue-bv-posts

Hospedagem pública das imagens dos carrosséis da **Lave & Pegue Boa Vista (RR)**.

- `lpbv/<AAAA-MM-DD>_<HH>/01.jpg …` — slides de cada post (URL: `https://raw.githubusercontent.com/devcadu/lavepegue-bv-posts/main/lpbv/...`).
- `pedidos/*.txt` — linhas `destino|url`; a Action **baixar-imagens** baixa cada URL para o destino, apaga o pedido e faz commit.
