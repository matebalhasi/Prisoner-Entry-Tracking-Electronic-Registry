import pymysql

from flask import Flask, request, jsonify

import os
from dotenv import laod_dotenv, dotenv_values

def connection():
    try:
            connection = pymysql.connect(
                 host=os.getenv("HOST"),
                 user = os.getenv("USER"),
                 password = os.getenv("PASSWORD"),
                 database = os.getenv("DATABASE")
            )
            cursor = connection.cursor()
            return jsonify({"message":"Kapcsolat sikeres!"}),200
    except:
        return jsonify({"message": "Adatbázis hiba"}), 503