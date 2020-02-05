import json
import pyodbc
from io import open

class connect_to_database():
    def __init__(self):
        server = "localhost,1433"
        database_name = "Northwind"
        user_name = "sa"
        password = "Passw0rd2018"
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};'
                                                'SERVER=' + server + ';'
                                                'DATABASE=' + database_name + ';'
                                                'UID=' + user_name + ';'
                                                'PWD=' + password)
        self.cursor = self.docker_Northwind.cursor()

    def modify_clothes_table(self):
        with open("file.json", "r") as myfile:
            data = myfile.read()
            json_object = json.loads(data)

        self.ProductID = json_object["ProductID"]
        self.ProductSize = json_object["ProductSize"]
        self.ProductColour = json_object["ProductColour"]
        self.ProductGender = json_object["ProductGender"]
        self.ProductType = json_object["ProductType"]
        self.ProductPrice = json_object["ProductPrice"]

        sql_insert = "INSERT INTO Clothes( ProductID, ProductSize, ProductColour, ProductGender, ProductType, ProductPrice) \
        VALUES ({},{},{},{},{},{})".format(self.ProductID, self.ProductSize, self.ProductColour, self.ProductGender, self.ProductType, self.ProductPrice)

        self.cursor.execute(sql_insert)
        self.cursor.commit()
