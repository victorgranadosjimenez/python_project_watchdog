import pyodbc
import json
from io import open


class connect_to_database():
    def __init__(self, ProductID, ProductSize, ProductColour, ProductGender, ProductType, ProductPrice):
        self.ProductID = ProductID
        self.ProductSize = ProductSize
        self.ProductColour = ProductColour
        self.ProductGender = ProductGender
        self.ProductType = ProductType
        self.ProductPrice = ProductPrice
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

        with open("file.json", "r") as myfile:
            data = myfile.read()
            json_object = json.loads(data)

        print(json_object)

        for item in json_object:
            self.ProductID = item.get("ProductID", None)
            self.ProductSize = item.get("ProductSize", None)
            self.ProductColour = item.get("ProductColour", None)
            self.ProductGender = item.get("ProductGender", None)
            self.ProductType = item.get("ProductType", None)
            self.ProductPrice = item.get("ProductPrice", None)


    def modify_clothes_table(self):
        sql_insert = "INSERT INTO Clothes( ProductID, ProductSize, ProductColour, ProductGender, ProductType, ProductPrice) \
        VALUES ({},{},{},{},{},{})".format(self.ProductID, self.ProductSize, self.ProductColour, self.ProductGender, self.ProductType, self.ProductPrice)

        self.cursor.execute(sql_insert)
        self.cursor.commit()


