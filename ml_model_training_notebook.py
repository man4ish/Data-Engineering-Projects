from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ML with Databricks').getOrCreate()

# Load training data
df = spark.read.csv('train_data.csv', header=True, inferSchema=True)

# Feature engineering
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
df = assembler.transform(df)

# Model training
lr = LogisticRegression(featuresCol='features', labelCol='label')
model = lr.fit(df)

# Model evaluation
predictions = model.transform(df)
predictions.show()

