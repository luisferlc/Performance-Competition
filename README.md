# Performance-Competition
Comparing the speed to read a simple 9GB CSV when using the new promising data managemnt library named Polars, vs Pandas vs Spark

I wanted to try this new Polars library which is created with the purpose of faster performance when working with dataframes. They say is going to replace Pandas and thats very interesting for enterprises who wants to deal better with costs of processing data and speed.

I have always used Pandas as my main tool to work with data but, these little experiment is giving me motivation to learn more about Polars and also, keep learning about Spark, because as you may see in the results, Spark was the fastest by far.

The task was simple, just read a 9GB CSV file with the different tools and compare the times for loading the data. My poor 12GB of RAM doesnt allow me to read something bigger but, I think its a good start to test Polars.

## Pandas
<img src="https://github.com/luisferlc/Performance-Competition/blob/main/pandas.png">

## Polars
<img src="https://github.com/luisferlc/Performance-Competition/blob/main/polars.png">

## Spark
<img src="https://github.com/luisferlc/Performance-Competition/blob/main/spark.png">

# Conclusions
- Spark was the fastest with less than 5 seconds followed by
- Polars with 54.2 seconds and the last was
- Pandas with 109 seconds.

Pros and Cons of each tool:
#### Spark:
- Built in parallelization between CPU Cores.
- Harder to setup, not as many functions like pandas or polars but,
- its seems that the way of paralelization of spark still better than polars.
#### Polars:
- Built in parallelization between CPU Cores.
- I have seen more functions options than spark, not as many as pandas, but,
- still faster than pandas.
- Also,  in the documentation of polars it is said that it can process data larger than your memory, this is very PROMISING.
#### Pandas:
- A lot of functions to use but,
- it doesnt have the built-in parallelization that Spark and Polars have, making it much harder when daling with big data.

I'm very excited to learn more about Polars and the benefits that this can bring to reduce costs.

More about Polars:
https://pola.rs/
