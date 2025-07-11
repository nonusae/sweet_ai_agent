import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not os.path.commonpath([full_path, abs_working_dir]) == abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'
        if not full_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        # Run python file
        result = subprocess.run(['python3', full_path], timeout=30, capture_output=True)

        # if output is empty, return error
        if result.stdout.decode('utf-8') == '':
            return f'No output produced.'

        exit_code = result.returncode
        if exit_code != 0:
            return f'Process exited with code {exit_code}'


        return f'STDOUT: {result.stdout.decode("utf-8")}\nSTDERR: {result.stderr.decode("utf-8")}'
    except Exception as e:
        return f'Error: executing Python file: {e}'

