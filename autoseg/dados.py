import os
import shutil
import pandas as pd
from pathlib import Path

from autoseg import utils

def processar_arquivo_bruto_autoseg() -> None:
    """
    Processa o arquivo bruto da Autoseg, criando uma coluna de referência baseada
    nos valores da coluna 'ENVIO' e exporta o resultado para um arquivo CSV processado.

    O arquivo bruto é lido do diretório 'interim/autoseg', e o arquivo processado é salvo
    no diretório 'processed/autoseg'. A referência é gerada substituindo as letras 'A' por '1'
    e 'B' por '2' na coluna 'ENVIO'.

    Args:
        None

    Returns:
        None
    """
    # Diretório provisório
    path_interim = Path('..') / 'data' / 'interim' / 'autoseg'

    # Leitura do arquivo
    df = pd.read_csv(
        path_interim / 'arq_casco3_comp.csv',
        sep=';',
        encoding='ansi'
    )

    # Criando uma variável de referência
    ref = df['ENVIO'].str.replace('A', '1')
    ref = ref.str.replace('B', '2')

    # Inserindo a referência no dataframe
    df.insert(0, 'REF', ref)

    # Exportando arquivo
    path_save = Path('..') / 'data' / 'processed' / 'autoseg'
    nome_save = f"{df['REF'].unique()[0]}.csv"
    df.to_csv(path_save / nome_save, index=False)

    print(f"Arquivo arq_casco3_comp da referência '{nome_save}' salvo com sucesso em '{path_save / nome_save}'.")
    
