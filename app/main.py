from flask import Flask, request, jsonify
import luigi
from luigi import Task, Parameter
import logging
import os
import multiprocessing
import threading

logging_config_path = os.path.join(os.path.dirname(__file__), 'logging.cfg')
logging.config.fileConfig(logging_config_path)

app = Flask(__name__)

logger = logging.getLogger('luigi.task')

class MyTask(luigi.Task):
    name = luigi.Parameter()

    def run(self):
        logger.info(f'Starting task for name {self.name}')
        with self.output().open('w') as f:
            f.write(f'Hello, {self.name}!')
        logger.info(f'Task completed for name {self.name}')

    def output(self):
        return luigi.LocalTarget(f'output/{self.name}.txt')

@app.route("/")
def hello():
    return jsonify(message="Hello, World!")

@app.route('/run-task')
def run_task():
    name = request.args.get('name')
    #threading.Thread(target=luigi.build, args=([MyTask(name=name)],), kwargs={'local_scheduler': True}).start()
    luigi.build([MyTask(name=name)], local_scheduler=True)
    with MyTask(name=name).output().open() as f:
        output = f.read()
    return output

if __name__ == "__main__":
    #multiprocessing.set_start_method('spawn')
    app.run(threaded=False)
