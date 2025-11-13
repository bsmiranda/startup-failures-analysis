"""
Módulo de carregamento e concatenação de datasets de falhas de startups.

Objetivo:
---------
Este script carrega todos os arquivos CSV localizados na pasta `data/` e os concatena
em um único DataFrame para posterior análise.

Autor: Bruno Miranda
Projeto: Startup Failures Analysis
Data: 2025-11
"""

# Importando as bibliotecas necessárias
import os
import pandas as pd


def load_startup_data(data_path="../data/raw"):
    """
    Carrega todos os arquivos CSV da pasta especificada e os combina em um único DataFrame.

    Parâmetros
    ----------
    data_path : str
        Caminho para a pasta onde estão os arquivos CSV (padrão: "../data")

    Retorno
    -------
    pandas.DataFrame
        DataFrame concatenado com os dados de todas as indústrias.
    """

    # Lista para armazenar temporariamente os DataFrames individuais
    dataframes = []

    # Loop sobre os arquivos na pasta de dados
    for file in os.listdir(data_path):
        # Verifica se o arquivo termina com .csv
        if file.endswith(".csv"):
            file_path = os.path.join(data_path, file)

            print(f"📂 Carregando arquivo: {file}")

            # Lê o CSV usando pandas
            df = pd.read_csv(file_path)

            # Adiciona uma coluna indicando de qual arquivo veio (útil para análises setoriais)
            df["Source_File"] = file

            # Adiciona o DataFrame à lista
            dataframes.append(df)

    # Concatena todos os DataFrames da lista em um único
    full_df = pd.concat(dataframes, ignore_index=True)

    # Limpeza básica: remover espaços extras nos nomes das colunas
    full_df.columns = full_df.columns.str.strip()

    print(f"\n Total de registros combinados: {len(full_df)}")
    print(f" Total de colunas: {len(full_df.columns)}")

    return full_df


# Execução direta do script (útil para testes)
if __name__ == "__main__":
    df = load_startup_data("data/raw")
    print("\nVisualização inicial:")
    print(df.head())

