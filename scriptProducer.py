# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:51:44 2022

@author: Utilisateur
"""


#Envoie un fichier json ligne ligne par ligne dans le bus Kafka
import json
from kafka import KafkaProducer
import time
#On se connecte à la machine Kafka
producer = KafkaProducer(bootstrap_servers='192.168.33.13:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#On récupère chaque ligne du fichier json dans une liste 
with open('covid19_by_country.csv', 'r') as f:
    lines= f.readlines()


for i in lines:
    message=i.strip()
    print(message)
    producer.send('CovidCountry', message)
    time.sleep(10)