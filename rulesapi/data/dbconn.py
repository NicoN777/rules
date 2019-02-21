import sqlite3


class DatabaseConnection:
    def __init__(self, name=None, host='localhost', port=None, **kwargs):
        self.name = name
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.name, check_same_thread=False)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
