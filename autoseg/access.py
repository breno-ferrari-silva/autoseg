import pyodbc
import pandas as pd

from typing import List, Optional

def calcular_media(valores: List[float], peso: Optional[List[float]] = None) -> float:
    """
    Calcula a média ponderada ou aritmética de uma lista de valores.

    Args:
        valores (List[float]): Lista de números para calcular a média.
        peso (Optional[List[float]], optional): Lista de pesos correspondentes aos valores.
            Se não fornecido, a média será aritmética. Defaults to None.

    Returns:
        float: A média calculada (ponderada ou aritmética).

    Raises:
        ValueError: Se a lista de pesos tiver um tamanho diferente da lista de valores.
    """

#def conectar_access():
