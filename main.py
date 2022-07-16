import os

from flask import Flask, request
from classes import InputData
from exceptions import IncorrectCommand
from utils import execute_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data/")


@app.route("/perform_query", methods=["GET", "POST"])
def perform_query():

    if request.method == "GET":
        file_name = request.args.get('file_name', None)
        cmd1 = request.args.get('cmd1', None)
        value1 = request.args.get('value1', None)
        cmd2 = request.args.get('cmd2', None)
        value2 = request.args.get('value2', None)
    else:
        file_name = request.form.get('file_name', None)
        cmd1 = request.form.get('cmd1', None)
        value1 = request.form.get('value1', None)
        cmd2 = request.form.get('cmd2', None)
        value2 = request.form.get('value2', None)

    file_name = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_name):
        return app.response_class('File not found', content_type="text/plain", status=400)

    query = InputData(file_name, cmd1, value1, cmd2, value2)

    try:
        result = '\n'.join(execute_query(query))
    except IncorrectCommand:
        return app.response_class('Incorrect command', content_type="text/plain", status=400)
    except (TypeError, ValueError):
        return app.response_class('Incorrect value', content_type="text/plain", status=400)

    return app.response_class(result, content_type="text/plain", status=200)


if __name__ == "__main__":
    app.run(debug=True)
