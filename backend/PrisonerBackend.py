import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER", "root")
PASSWORD = os.getenv("PASSWORD", "")
DATABASE = os.getenv("DATABASE", "prisondb")


def get_connection():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )


def get_all_prisoners():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prisoner")
        data = cursor.fetchall()
        conn.close()
        return {"status": 200, "data": data}
    except mysql.connector.Error as e:
        return {"status": 500, "error": str(e)}

def add_prisoner(data: dict):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO prisoner (F_Name, L_Name, Birth_Date, Danger_Level, Cell_Number, Prison_ID)
        VALUES (%s, %s, %s, %s, %s,1)
        """
        cursor.execute(sql, (
            data["F_Name"],
            data["L_Name"],
            data["Birth_Date"],
            data["Danger_Level"],
            int(data["Cell_Number"])
        ))
        conn.commit()
        conn.close()
        return {"status": 200, "message": "Fogvatartott hozzáadva"}
    except mysql.connector.Error as e:
        return {"status": 500, "error": str(e)}


def move_prisoner(pid: int, new_cell: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE prisoner SET Cell_Number=%s WHERE ID=%s"
        cursor.execute(sql, (new_cell, pid))
        conn.commit()
        conn.close()
        return {"status": 200, "message": "Fogvatartott áthelyezve"}
    except mysql.connector.Error as e:
        return {"status": 500, "error": str(e)}

def get_all_blocks():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT Block_ID, Block_Name, Status FROM block")
        data = cursor.fetchall()
        conn.close()
        return {"status": 200, "data": data}
    except mysql.connector.Error as e:
        return {"status": 500, "error": str(e)}

def get_cells_by_block(block_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT Cell_Number, Block_ID FROM cell WHERE Block_ID=%s"
        cursor.execute(sql, (block_id,))
        cells = cursor.fetchall()

        conn.close()

        return cells if cells else []
    except mysql.connector.Error as e:
        return {"status": 500,"error": str(e)}
    
def get_prisoners_in_cell(cell_number:int):

    try:
        conn = get_connection()
        cursor= conn.cursor(dictionary=True)

        cell_number = int(cell_number)
        sql = "SELECT ID, F_Name, L_Name, Birth_Date, Danger_Level, Cell_Number, Prison_ID FROM Prisoner WHERE Cell_Number=%s"
        cursor.execute(sql, (cell_number,))
        prisoners = cursor.fetchall()

        conn.close()

        return prisoners if prisoners else []
    except mysql.connector.Error as e:
        return {"status": 500, "error": str(e)}
