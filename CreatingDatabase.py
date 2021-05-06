import pandas as pd
import sqlite3

# Reading data from excel

annual_data = pd.read_excel("Annual.xlsx")
monthly_data = pd.read_excel("Monthly.xlsx")

# Creating a database and tables

conn = sqlite3.connect("GoldDatabase.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS annualdata ({})".format(" ,".join(annual_data.columns)))
cur.execute("CREATE TABLE IF NOT EXISTS monthlydata ({})".format(" ,".join(monthly_data.columns)))

# Inserting annual and monthly gold price data into tables

for row in annual_data.iterrows():
  sql = 'INSERT INTO annualdata ({}) VALUES({})'.format(' ,'.join(annual_data.columns), ','.join(['?'] * len(annual_data.columns)))
  cur.execute(sql, tuple(row[1]))
  conn.commit()
for row in monthly_data.iterrows():
  sql = 'INSERT INTO monthlydata ({}) VALUES({})'.format(' ,'.join(monthly_data.columns), ','.join(['?'] * len(monthly_data.columns)))
  cur.execute(sql, tuple(row[1]))
  conn.commit()
