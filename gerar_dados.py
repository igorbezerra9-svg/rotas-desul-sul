"""
gerar_dados.py
----------------
Converte a planilha "CARTEIRA_EM_CAMPO.xlsx" (aba "Planilha1") no arquivo
dados.js usado pelo painel de rotas (index.html).

Como usar:
1. Coloque o novo arquivo exportado do Excel na mesma pasta deste script,
   com o nome "CARTEIRA_EM_CAMPO.xlsx" (ou ajuste o nome abaixo).
2. Rode:  python gerar_dados.py
3. Isso vai sobrescrever o arquivo "dados.js" nesta pasta.
4. Suba (commit + push) o "dados.js" atualizado pro GitHub.

Requisitos: pip install openpyxl --break-system-packages
"""

import json
import os
from datetime import datetime
import openpyxl

ARQUIVO_ENTRADA = "CARTEIRA_EM_CAMPO.xlsx"
ARQUIVO_SAIDA = "dados.js"
ABA = "Planilha1"


def main():
    if not os.path.exists(ARQUIVO_ENTRADA):
        print(f"ERRO: não encontrei o arquivo '{ARQUIVO_ENTRADA}' nesta pasta.")
        print("Coloque o Excel exportado aqui (com esse nome) e rode de novo.")
        return

    wb = openpyxl.load_workbook(ARQUIVO_ENTRADA, data_only=True)
    ws = wb[ABA]
    rows = list(ws.iter_rows(min_row=2, values_only=True))

    out = []
    for r in rows:
        if r[0] is None:
            continue

        venc = r[23]
        venc_iso = None
        if venc:
            try:
                dt = datetime.strptime(str(venc).strip(), "%d/%m/%Y %H:%M")
                venc_iso = dt.strftime("%Y-%m-%dT%H:%M:%S")
            except Exception:
                venc_iso = None

        out.append({
            "cod": r[2],
            "os": r[3],
            "proc": r[4],
            "tipoTdc": r[5],
            "tipoRem": (r[7] or "").strip(),
            "estado": r[8],
            "cliCod": r[9],
            "cliNome": r[10],
            "lon": float(r[12]) if r[12] is not None else None,
            "lat": float(r[13]) if r[13] is not None else None,
            "mun": r[17],
            "bairro": r[18],
            "equipe": r[20],
            "chefe": r[21],
            "endereco": r[22],
            "venc": venc_iso,
        })

    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
        f.write("// Gerado automaticamente por gerar_dados.py — não editar à mão.\n")
        f.write("// Última atualização: " + datetime.now().strftime("%d/%m/%Y %H:%M") + "\n")
        f.write("const DATA = ")
        json.dump(out, f, ensure_ascii=False)
        f.write(";\n")

    print(f"OK! {len(out)} ordens de serviço exportadas para '{ARQUIVO_SAIDA}'.")
    print("Agora é só commitar e dar push no GitHub.")


if __name__ == "__main__":
    main()
