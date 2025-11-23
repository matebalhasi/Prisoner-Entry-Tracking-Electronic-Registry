import pymysql
import Connection

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/connection', methods=[GET])
def connection():
        return Connection.connection()