from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error
import threading
import tkinter as tk
from tkinter import messagebox
from Prisoner_Backend import get_all_prisoners, add_prisoner, move_prisoner


app = Flask(__name__)

#adatbazis csatlakozasi teszt
def test_connection():
    try:
        conn = mysql.connector.connect(
            host ="127.0.0.1",
            port = 3306,
            user="root",
            password="",
            database="prisondb"
        )
        if conn.is_connected():
            conn.close()
           
            return True
        else:
            return False
    except Error:
        return False
    
@app.route("/check-db")
def check_db():
    success = test_connection()
    if success:
        return jsonify({"status":200, "message":"Csatlazotott az adatbazisra"}),200
    else:
        return jsonify({"status":503, "message":"Az adatbazis nem elerheto"}),503

if __name__ == "__main__":
    print("A backend a http:127.0.0.1:5000-ren fut")
    app.run(debug=True)


@app.route("/prisoners", methods=["GET"])
def route_get_all_prisoners():
    return jsonify(get_all_prisoners()),200

@app.route("/prisoners/add", methods=["POST"])
def route_add_prisoners():
    data = requests.json
    if not data or "name" not in data or "cell" not in data:
        return jsonify({"error": "Hibas informacio"}), 400
    result = add_prisoner(data)
    status = 201 if "id" in result else 500
    return jsonify(result), status

@app.route("/prisoners/<int:pid>/move", methods=["PUT"])
def route_move_prisoner(pid):
    data = request.json
    new_cell = data.get("new_cell")
    if new_cell is None:
        return jsonify({"error": "Missing new_cell"}), 400
    result = move_prisoner(pid, new_cell)
    status = 200 if "error" not in result else 500
    return jsonify(result), status