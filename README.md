# 🕵️ Verificador de Tags `<title>` em URLs

Este script Python realiza a verificação da presença da tag `<title>` em uma lista de URLs fornecidas por um arquivo de texto. Os resultados são salvos em dois arquivos de saída: um `.txt` e um `.csv`.

---

## 📌 Funcionalidades

- Acessa cada URL presente no arquivo `urls.txt`;
- Verifica se a tag `<title>` está presente e não está vazia;
- Salva os resultados em:
  - `resultado_titles.txt` (formato simples para leitura);
  - `resultado_titles.csv` (formato ideal para planilhas).

---

## 🚀 Como usar

### 1. Pré-requisitos

Certifique-se de ter o Python 3.x instalado, com as bibliotecas abaixo:

```bash
pip install requests beautifulsoup4
