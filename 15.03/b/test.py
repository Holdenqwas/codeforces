import subprocess

with open('testcase.txt', 'r') as file:
    data = file.read().strip()

process = subprocess.Popen(
    ['python', 'main.py'],
    stdin=subprocess.PIPE,
    text=True
)
process.communicate(input=data)
