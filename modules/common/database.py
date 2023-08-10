import sqlite3


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(
            r"C:\\Users\\Користувач\\KhymynQAauto" + r"\\become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite3_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite3_select_Query)
        record = self.cursor.fetchall()

        print(f"Connected successfully. SQlite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
                VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = f"SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_checking_table_relationships(self, table):
        query = f"SELECT * FROM '{table}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def check_data_types(self, table):
        query = f"SELECT name FROM '{table}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_address_by_id(self, id):
        query = f"SELECT address, city FROM customers WHERE id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def insert_new_customer(self, id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
                VALUES ({id}, '{name}', '{address}', '{city}', {postalCode}, '{country}')"
        self.cursor.execute(query)
        self.connection.commit()
        
    def delete_customer_by_id(self, id):
        query = f"DELETE FROM customers WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()
