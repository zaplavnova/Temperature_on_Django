#!/usr/bin/env python3

import os
import requests
from datetime import datetime
import psycopg2

conn = psycopg2.connect(dbname='temperature', user='postgres',  password='enot115735', host='localhost', port="5432")
cursor = conn.cursor()

url = "http://cloudseism.ru/sensors/"

js = requests.get(url).json()[0]
js["ts"] = datetime.now()

sql = "INSERT INTO TEMPERATURE (temp1, temp2, temp3, ts) VALUES (%s, %s, %s, %s)"
record = (js['temp1'], js['temp2'], js['temp3'], js['ts'])
cursor.execute(sql, record)
conn.commit()
conn.close()
