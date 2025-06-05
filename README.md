# ETLGPT

Projeto de ETL para CRM Marketing utilizando ChatGPT.

## Requisitos
- Python 3.9+
- `pandas`, `requests` e `openai`

## Instalando dependências
```bash
pip install pandas requests openai
```

## Definindo a chave da API da OpenAI
Obtenha sua chave na plataforma da OpenAI e defina-a em uma variável de ambiente chamada `OPENAI_API_KEY` antes de executar o notebook.

Linux/macOS:
```bash
export OPENAI_API_KEY="sua-chave"
```
Windows (cmd):
```cmd
set OPENAI_API_KEY="sua-chave"
```

## Executando o notebook
1. Inicie o Jupyter e abra `ETLpython.ipynb`:
```bash
jupyter notebook
```
2. Execute as células do notebook na ordem desejada. O arquivo `Extract.csv.txt` deve estar no mesmo diretório.

Também é possível executar o notebook de forma não interativa:
```bash
jupyter nbconvert --to notebook --execute ETLpython.ipynb
```
