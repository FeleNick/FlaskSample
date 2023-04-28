from flask import request
from flask import jsonify
import luigi
from app import app
from app.tasks import MyTask

@app.route("/")
def hello():
    return jsonify(message="Hello, World!")

@app.route('/run-task')
def run_task():
    name = request.args.get('name')
    luigi.build([MyTask(name=name)], local_scheduler=True)
    with MyTask(name=name).output().open() as f:
        output = f.read()
    return output