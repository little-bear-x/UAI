# main.py
import subprocess

process = subprocess.Popen("streamlit run Homepage.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output)
