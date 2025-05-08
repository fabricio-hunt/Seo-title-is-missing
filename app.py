import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv

def verificar_titles(input_file, output_txt, output_csv):
    """
    Verifica a presença de tags <title> em uma lista de URLs.

    Lê URLs de um arquivo de entrada, acessa cada URL, verifica se
    a tag <title> existe e não está vazia. Salva os resultados
    em arquivos .txt e .csv.

    Args:
        input_file (Path): Caminho para o arquivo .txt contendo as URLs.
        output_txt (Path): Caminho para o arquivo .txt de saída dos resultados.
        output_csv (Path): Caminho para o arquivo .csv de saída dos resultados.
    """
    with open(input_file, 'r', encoding='utf-8') as file: # Adicionar encoding na leitura também
        urls = [line.strip() for line in file.readlines() if line.strip()]

    resultados_txt = []
    resultados_csv = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Levanta exceção para erros HTTP (4xx, 5xx)
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')

            if not title_tag or not title_tag.text.strip():
                status = "title is missing"
            else:
                status = "OK"

        except requests.exceptions.HTTPError as e: # Erro HTTP específico
            status = f"erro HTTP ({e.response.status_code}) ao acessar"
        except requests.RequestException as e: # Outros erros de request (timeout, conexão)
            status = f"erro ao acessar ({e.__class__.__name__})"
        except Exception as e: # Pega qualquer outra exceção inesperada
            status = f"erro inesperado ({e.__class__.__name__})"


        resultados_txt.append(f"{url} -> {status}")
        resultados_csv.append([url, status])

    # Salvar resultado em .txt
    with open(output_txt, 'w', encoding='utf-8') as out_file:
        out_file.write('\n'.join(resultados_txt))

    # Salvar resultado em .csv
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["URL", "Status"])
        writer.writerows(resultados_csv)

    print(f"✅ Verificação concluída.\n- TXT salvo em: {output_txt}\n- CSV salvo em: {output_csv}")


base_dir = Path(__file__).parent

verificar_titles(
    base_dir / "urls.txt",
    base_dir / "resultado_titles.txt",
    base_dir / "resultado_titles.csv"
)