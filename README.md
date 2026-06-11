# Rotas DESUL Sul

Painel de sugestão de rotas para as equipes comerciais do DESUL Sul (Cosampa),
com mapa, priorização por vencimento, geração de rota e navegação (Google
Maps / Waze).

## Arquivos

- **index.html** — o aplicativo (mapa, lista, rota, navegação). Não precisa mexer.
- **dados.js** — os dados da carteira (gerado a partir do Excel). É o único
  arquivo que muda toda vez que você atualiza a carteira.
- **gerar_dados.py** — script que converte o Excel exportado em `dados.js`.

## 1. Subir no GitHub Pages (primeira vez)

1. Crie um repositório novo no GitHub (ex.: `rotas-desul-sul`), público.
2. Faça upload destes 3 arquivos (`index.html`, `dados.js`, `gerar_dados.py`)
   pra raiz do repositório (pelo site mesmo: **Add file → Upload files**).
3. Vá em **Settings → Pages**.
4. Em "Source", selecione a branch `main` e a pasta `/ (root)`. Salve.
5. Espere ~1 minuto e acesse:
   `https://SEU-USUARIO.github.io/rotas-desul-sul/`

Pronto — esse link é o que você manda pras equipes (pode até virar atalho na
tela inicial do celular).

## 2. Atualizar a carteira (toda vez que exportar do Excel)

Você só precisa repetir esse passo a passo. O `index.html` nunca muda.

1. Exporte a carteira do Excel como sempre, com o nome
   `CARTEIRA_EM_CAMPO.xlsx`.
2. Coloque esse arquivo na mesma pasta do `gerar_dados.py` no seu computador.
3. Rode (uma vez só, se ainda não tiver instalado):
   ```
   pip install openpyxl --break-system-packages
   ```
4. Rode o script:
   ```
   python gerar_dados.py
   ```
   Isso vai gerar/atualizar o arquivo `dados.js`.
5. Suba o `dados.js` atualizado pro GitHub:
   - Pelo site: vá no repositório → clique em `dados.js` → ícone de lápis
     (editar) → cole o conteúdo novo OU use **Add file → Upload files**
     marcando "substituir" o arquivo existente → **Commit changes**.
   - Ou, se preferir linha de comando (git já configurado):
     ```
     git add dados.js
     git commit -m "Atualiza carteira"
     git push
     ```

Em ~1 minuto o GitHub Pages atualiza sozinho e as equipes já veem os dados
novos ao recarregar a página.

## Observações

- O arquivo `CARTEIRA_EM_CAMPO.xlsx` (com nomes/endereços de clientes) **não
  precisa ir pro GitHub** — só o `dados.js` (já no formato do app). Tem um
  `.gitignore` evitando subir `.xlsx` por engano.
- A coluna usada como "Equipe" é a mesma que aparece na carteira
  (`CPE-LB-13B`, `JZN-MM-13B`, etc). Se o código de alguma equipe mudar, o
  app já se ajusta sozinho na próxima geração de `dados.js`.
- A rota e a localização (GPS) só funcionam direito quando acessado por
  **HTTPS** — o GitHub Pages já serve assim por padrão.
