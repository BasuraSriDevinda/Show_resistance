import os
import sqlite3
if os.path.exists("mydatabase.db"):
    print("Database exists. Connecting...")

else:
    print("Database does not exist. Creating new one...")


connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()



connection.close()