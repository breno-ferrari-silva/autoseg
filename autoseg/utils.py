import zipfile
import os
import shutil
import pandas as pd

from typing import Optional

def descompactar_zip(path_zip: str, path_ext: str) -> None:
    """
    Descompacta um arquivo ZIP para um diretório especificado.

    Args:
        path_zip (str): Caminho para o arquivo ZIP a ser descompactado.
        path_ext (str): Caminho para o diretório onde os arquivos serão extraídos.

    Returns:
        None
    """
    with zipfile.ZipFile(path_zip, 'r') as zip_ref:
        zip_ref.extractall(path_ext)
        print(f"Arquivo '{path_zip}' descompactado com sucesso em '{path_ext}'.")


def limpar_pasta(path: str) -> None:
    """
    Remove todos os arquivos e subpastas de um diretório, deixando-o vazio.

    Args:
        path (str): Caminho para a pasta que será esvaziada.

    Returns:
        None: Não retorna nenhum valor.
    """
    shutil.rmtree(path)
    os.makedirs(path)