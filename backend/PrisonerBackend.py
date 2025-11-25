import mysql.connector

def get_all_prisoners():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="prisondb"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prisoner")
        data = cursor.fetchall()
        conn.close()
        return {"status": 200, "data": data}
    except mysql.connector.Error as e:
        return {"status": 500, "error": str(e)}

def add_prisoner(data: dict):
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="prisondb"
        )
        cursor = conn.cursor()
        sql = """
        INSERT INTO prisoner (F_Name, L_Name, Birth_Date, Danger_Level, Cell_Number)
        VALUES (%s, %s, %s, %s, %s)
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
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="prisondb"
        )
        cursor = conn.cursor()
        sql = "UPDATE prisoner SET Cell_Number=%s WHERE ID=%s"
        cursor.execute(sql, (new_cell, pid))
        conn.commit()
        conn.close()
        return {"status": 200, "message": "Fogvatartott áthelyezve"}
    except mysql.connector.Error as e:
        return {"status": 500, "error": str(e)}
