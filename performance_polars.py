import polars as pl
import timeit

tic=timeit.default_timer()
df_csv = pl.read_csv("D:\Documentos\Polars\data\discogs.csv")
print(df_csv.head())
toc=timeit.default_timer()
print("Polars:", toc - tic)



