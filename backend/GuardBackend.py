import mysql.connector
from datetime import timedelta
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER","root")
PASSWORD = os.getenv("PASSWORD","")
DATABASE = os.getenv("DATABASE","prisondb")


def get_connection():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

def get_all_guards():
    try:
        conn = get_connection()

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prison_guard")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"status": 200, "data": data}
    except Error as e:
        return {"status": 500, "error": str(e)}


def get_guard_schedule(guard_id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        
        sql = "SELECT * FROM guard_shifts WHERE Guard_ID = %s"
        cursor.execute(sql, (guard_id,))
        data = cursor.fetchall()

        # Minden timedelta mezőt stringgé alakítunk, hogy JSON serializálható legyen
        for row in data:
            for key, value in row.items():
                if isinstance(value, timedelta):  # itt kell a második argumentum is
                    row[key] = str(value)  # pl. "08:00:00"

        cursor.close()
        conn.close()

        return {"status": 200, "data": data}

    except Error as e:
        return {"status": 500, "error": str(e)}

