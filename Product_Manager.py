import mysql.connector

class ProductManager:
    def __init__(self):
        self.connect=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Achulachu@123",
            database="shop_db"
        )
        self.cursor=self.connect.cursor()
        print("database connected successfully")

    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query=("insert product(name,category,price,quantity,manufacturer)values(%s,%s,%s,%s,%s)")
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Products added...!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select*from product"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            return records
        except Exception as e:
            print(e)

    def get_object(self,id):
        try:
            self.cursor=self.connection.cursor()
            query="select * from product where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print (e)

    def retrieve(self,id):
        try:
            self.cursor=self.connection.cursor()
            query="select*from product where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record is not None:
                print(record)
            else:
                print("product nor found ...!")
        except Exception as e:
            print(e)

    def put(self,id):
        pass

    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select*from product where id=%s"
            value=(id,)
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            if record is not None:
                query="delete from product where id=%s"
                self.cursor.execute(query,value)
                self.connection.commit()
                print("Product deleted...!")
            else:
                print("Product not found...!")
        except Exception as e:
            print(e)


