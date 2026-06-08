from etl import pipeline_calcular_kpi_vendas

pasta_argumento: str = "data"
formato_saida: list = ["csv"] 
pipeline_calcular_kpi_vendas("data", ["csv"])