from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("createDataframe").getOrCreate()
# Empty DataFrame with no data
empty_df = spark.createDataFrame([], "id INT, name STRING")
empty_df.show()

# Convert rdd to dataframe using toDF() metho
rdd = spark.sparkContext.parallelize([(1, 'Alice'), (2, 'Bob')])
columns = ["id", "name"]
df_from_rdd = rdd.toDF(columns)
df_from_rdd.show()