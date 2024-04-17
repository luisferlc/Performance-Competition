import pandas as pd
import timeit

tic=timeit.default_timer()
df_csv = pd.read_csv("D:\Documentos\Polars\data\discogs.csv")
print(df_csv.head())
toc=timeit.default_timer()
print("Pandas:", toc - tic)

