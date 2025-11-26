from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
import threading
import tkinter as tk
from tkinter import messagebox

import PrisonerBackend
import GuardBackend


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



# Prisoners Endjointjai --------

@app.route("/prisoners", methods=["GET"])
def get_prisoners():
    try:
        result = PrisonerBackend.get_all_prisoners()
        return jsonify(result), result.get("status", 500)
    except Exception as e:
        return jsonify({"status": 500, "error": str(e)}), 500


@app.route("/prisoners/add", methods=["POST"])
def add_prisoner():
    data = request.json
    result = PrisonerBackend.add_prisoner(data)
    return jsonify(result), result.get("status", 500)

@app.route("/prisoners/<int:pid>/move", methods=["PUT"])
def move_prisoner(pid):
    data = request.get_json(silent=True) or{}
    new_cell = data.get("new_cell")

    result = PrisonerBackend.move_prisoner(pid, new_cell)
    return jsonify(result), result.get("Status",500)


# Guardok Endpointjai -------


@app.route("/guards", methods = ["GET"])
def get_all_guards():
    try:
        result = GuardBackend.get_all_guards()
        return jsonify(result), result.get("status" , 500)
    except Exception as e:
        return jsonify({"status":500,"error":str(e)}),500

@app.route("/guards/<int:guard_id>/schedule", methods = ["GET"])
def get_guard_schedule(guard_id):
    result = GuardBackend.get_guard_schedule(guard_id)
    if "error" in result:
        return jsonify(result), 500
    return jsonify(result),200



@app.route("/blocks)",methods = ["GET"])
def get_all_blocks():
    try:
        result = PrisonerBackend.get_all_blocks()
        return jsonify(result), result.get("status", 500)
    except Exception as e:
        return jsonify({"status": 500, "error": str(e)}), 500



@app.route("/cells/blocks/<int:block_id>", methods=["GET"])
def get_cells_by_block(block_id):
    try:
        cells = PrisonerBackend.get_cells_by_block(block_id)
        return jsonify(cells), 200
    except Exception as e:
        return jsonify({"status": 500, "error": str(e)}), 500
    
@app.route("/cells/<int:cell_number>/prisoners", methods=["GET"])
def get_prisoners_in_cell(cell_number):
    try:
        prisoners = PrisonerBackend.get_prisoners_in_cell(cell_number)
        return jsonify(prisoners), 200
    except Exception as e:
        return jsonify({"status": 500, "error": str(e)}), 500




if __name__ == "__main__":
    print("A backend a http:127.0.0.1:5000-ren fut")
    app.run(debug=True)

