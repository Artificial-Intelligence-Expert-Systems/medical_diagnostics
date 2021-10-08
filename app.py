from flask import Flask, jsonify
from db import database

app = Flask(__name__)


@app.route('/api/questionnaire/create', methods=['GET'])
@database.decorated_connect
def create_questionnaire(cursor):
    cursor.execute()
    return jsonify()


if __name__ == '__main__':
    app.run()
