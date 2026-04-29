import threading

class DatabaseConnection:
    """Singleton Pattern - ensures only one database connection"""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    print("🔌 New Database Connection created")
        return cls._instance

    def query(self, sql: str):
        return f"Executing: {sql}"