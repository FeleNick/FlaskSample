import logging
import luigi

# get the logger object for the luigi.task namespace
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

