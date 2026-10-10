#!/usr/bin/env python3
"""Bot guloso para o tanque 1 (ideia #055). Compra sempre a opcao de menor tempo de retorno.
Marcos de cardume: x2 de renda da especie em 25, 50 e 100 copias (ideia #014).
Uso: python3 sim_economia.py [especies.csv]"""
import csv, sys

MARCOS = (25, 50, 100)
DINHEIRO_INICIAL = 10.0  # presente para comprar o primeiro lebiste

def carregar(caminho):
    with open(caminho, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r["tanque_id"] == "agua_doce_01"]

def custo(r, n):  return float(r["custo_base"]) * float(r["razao_custo"]) ** n
def renda(r, n):  return float(r["renda_base_por_seg"]) * n * 2 ** sum(n >= m for m in MARCOS)

def simular(especies, limite_s=48 * 3600):
    qtd = {r["id"]: 0 for r in especies}
    t, dinheiro, log = 0.0, DINHEIRO_INICIAL, []
    desbloqueada = {especies[0]["id"]}
    while t < limite_s:
        total = sum(renda(r, qtd[r["id"]]) for r in especies)
        melhor = None
        for r in especies:
            i, n = r["id"], qtd[r["id"]]
            if i not in desbloqueada or n >= int(r["cota_max"]): continue
            ganho = renda(r, n + 1) - renda(r, n)
            c = custo(r, n)
            retorno = c / ganho if ganho > 0 else float("inf")
            if melhor is None or retorno < melhor[0]: melhor = (retorno, r, c)
        if melhor is None: break
        _, r, c = melhor
        espera = max(0.0, (c - dinheiro) / total) if total > 0 else (0 if dinheiro >= c else float("inf"))
        if espera == float("inf"): break
        t += espera; dinheiro += espera * total - c
        qtd[r["id"]] += 1
        for nxt in especies:
            req = nxt["libera_apos_ter"]
            if req:
                a, b = req.split(":")
                if qtd.get(a, 0) >= int(b): desbloqueada.add(nxt["id"])
        if qtd[r["id"]] in (1, 10, 25, 50, 100):
            log.append((t, r["id"], qtd[r["id"]]))
    return t, qtd, log

if __name__ == "__main__":
    esp = carregar(sys.argv[1] if len(sys.argv) > 1 else "species.csv")
    t, qtd, log = simular(esp)
    for tt, i, n in log: print(f"{tt/3600:7.2f} h  {i:15s} x{n}")
    print(f"\nFim: {t/3600:.2f} h  cópias: {qtd}")
