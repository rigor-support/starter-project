import importlib
import subprocess
import sys
import os

runner_name = sys.argv[1]

job = importlib.import_module(runner_name)

result = job.loader()

number_of_runners = len(result.get('runner_inputs', []))

if result.get('jobs', None):
    number_of_runners = len(result['jobs'])

running_processes = []
for task_index in range(number_of_runners):

    env = os.environ.copy()
    env['TASK_INDEX'] = f'{task_index}'
    task_process = subprocess.Popen(
        [
            'python',
            '-c',
            f"import importlib; job = importlib.import_module('{runner_name}'); job.runner({result.get('runner_inputs')})"
        ], env=env)
    running_processes.append(task_process)
