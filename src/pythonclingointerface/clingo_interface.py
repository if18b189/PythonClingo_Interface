import subprocess
import os




class ClingoInterface:

    def __init__(self, text):
        self.text = text

    def execute(self):
        return self.text

    def run(self):
        subprocess.call('clingo ../../tests/clingoCodeExample')

