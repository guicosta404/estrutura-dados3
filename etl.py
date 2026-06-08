import pandas as pd
import os # consegue fazer as coisas que faz no terminal
import glob
from ultils import log_decorator
# Função extract que lê e consolida um json
@log_decorator
def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index = True)
    return df_total

# Função de transformação
@log_decorator
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

#Função que da load em csv ou parquet
@log_decorator
def carregar_dados(df: pd.DataFrame, formato_saida:list):
    for formato in formato_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet")
            
@log_decorator
def pipeline_calcular_kpi_vendas(pasta: str, saida: list):
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    carregar_dados(data_frame_calculado, saida)            

