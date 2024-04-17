from pyspark.sql import SparkSession
import timeit

spark = SparkSession.builder.appName("pyspark_performance").getOrCreate()
tic=timeit.default_timer()
df_csv = spark.read.csv("D:\Documentos\Polars\data\discogs.csv")
print(df_csv.show(2))
toc=timeit.default_timer()
print("PySpark:", toc - tic)

