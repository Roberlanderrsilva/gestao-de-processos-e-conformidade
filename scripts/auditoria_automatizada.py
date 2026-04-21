name: Auditoria

on: [push]

jobs:
  verificacao:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Configurando Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalando Pandas
        run: pip install pandas

      - name: Rodando o Script
        run: python scripts/auditoria_automatizada.py
