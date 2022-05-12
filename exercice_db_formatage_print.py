# -*- coding: utf-8 -*-

import argparse
import csv
import sqlite3

conn = sqlite3.connect("/data/departements.db")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE departements (department_id INT ,department_name TEXT,manager_id INT,location_id INT)""")

################################## GET DATA AND FORMAT #######################################
# parse = argparse.ArgumentParser(description="Chargement de mon parseur !")
# parse.add_argument("-f", "--file",
#                    dest="filename",
#                    default="data/departements.csv")
# args = parse.parse_args()
# file = open(args.filename, "r")
# fields = []
# myData = []
# with open(args.filename) as myfile:
#     print(myfile)
#     data = csv.reader(myfile)
#     fields = next(data)
#     for row in data:
#         myData.append(tuple(row))
# print(myData)


################################## INSERTION IN DB #######################################
# for e in myData:
#     cursor.execute("INSERT INTO departements VALUES (?, ?, ?, ?)",
#                    (e))
# conn.commit()

cursor.execute("""SELECT * FROM departements""")
for row in cursor:
    print(row)

cursor.close()
conn.close()


