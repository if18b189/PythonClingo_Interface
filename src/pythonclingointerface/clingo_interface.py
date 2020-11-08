import subprocess
import os
import tempfile
import sys


class ClingoInterface:

    def __init__(self, text):
        self.text = text

    def execute(self):
        return self.text

    def run(self):

        os.chdir(os.path.join(os.path.abspath("../../tests/"))) # finding the right directory
        print(os.getcwd())  # printing the current working directory

        with tempfile.TemporaryFile() as tempf: # reading into a temporary file prevents issues with bigger input values
            proc = subprocess.Popen('clingo clingoCodeExample', shell=True, stdout=tempf)
            proc.wait()
            tempf.seek(0)

            x = tempf.read().splitlines()   # splitlines '\n' -> list

            for i in x:
                print(i.decode("utf-8"))    # decoding  b'1234' -> 1234


