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
