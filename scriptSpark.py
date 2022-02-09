# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:06:57 2022

@author: Utilisateur
"""

#import mysql.connector
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="PythonSparkStreamingKafka")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 10)
DKS = KafkaUtils.createDirectStream(ssc, ["CovidCountry"], {"metadata.broker.list": "192.168.33.13:9092"})

lines = DKS.map(lambda x: x[1])
splitLine = lines.map(lambda s: s.split(','))

splitLine.pprint()

#Starting Spark context
ssc.start()
ssc.awaitTermination()