"""
Módulo de carregamento e concatenação de datasets de falhas de startups.

Autor: Bruno Miranda
Projeto: Startup Failures Analysis
Data: 2025-11
"""

import os
import pandas as pd

def load_startup_data(data_path="data/raw"):
    """
    Carrega todos os CSVs de uma pasta e concatena em um DataFrame.

    Parâmetros
    ----------
    data_path : str
        Caminho para a pasta com os CSVs

    Retorno
    -------
    pandas.DataFrame
        DataFrame único com todos os dados carregados
    """
    dataframes = []
    
    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            file_path = os.path.join(data_path, file)
            print(f"Carregando: {file_path}")
            df = pd.read_csv(file_path)
            df["Source_File"] = file
            dataframes.append(df)
    
    full_df = pd.concat(dataframes, ignore_index=True)
    full_df.columns = full_df.columns.str.strip()  # Limpeza básica
    print(f"\nTotal de registros combinados: {len(full_df)}")
    print(f"Total de colunas: {len(full_df.columns)}")
    
    return full_df

# Teste rápido
if __name__ == "__main__":
    df = load_startup_data()
    print(df.head())
