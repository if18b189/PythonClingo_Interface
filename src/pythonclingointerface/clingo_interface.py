import subprocess
import os
import tempfile
import sys
import glob


class ClingoInterface:

    def __init__(self, text):
        self.text = text

        ClingoInterface.check_jnotebook_parenthesis(self)

    def execute(self):
        return self.text

    def run(self, file_or_code):
        # os.chdir(os.path.join(os.path.abspath("../../tests/")))  # finding the right directory
        # print(os.getcwd())  # printing the current working directory

        with tempfile.TemporaryFile() as tempf:  # reading into a temporary file prevents issues with bigger input values
            proc = subprocess.Popen('clingo ' + file_or_code, shell=True, stdout=tempf)
            proc.wait()
            tempf.seek(0)

            x = tempf.read().splitlines()  # splitlines '\n' -> list

            for i in x:
                print(i.decode("utf-8"))  # decoding  b'1234' -> 1234

    """
        scanning all directories recursively for jupyter notebook files
        extracting the code between 2 markers/parenthesis (perenthesis_start & parenthesis_end)
        running the clingo code with run()
    """

    def check_jnotebook_parenthesis(self):
        parenthesis = False
        parenthesis_start = "<CLINGO"
        parenthesis_end = "CLINGO>"
        parenthesis_content = ""

        os.chdir(os.path.join(os.path.abspath("../../")))  # finding the right directory
        files = glob.glob(os.getcwd() + '/**/*.ipynb', recursive=True)  # searching all .ipynb recursively

        for file in files:
            fs = open(file, 'r') # file provides the filename, r stands for read
            con = fs.read().splitlines()  # splitlines '\n' -> list

            for line in con:

                if parenthesis_end in line:  # checks for the end parenthesis
                    parenthesis = False

                if parenthesis:  # adds clingo code to to parenthesis_content
                    parenthesis_content += line[5:-2].replace("\\n", "\n").replace('\\"', '"')

                if parenthesis_start in line:  # checks for start parenthesis
                    parenthesis = True

            # creating a temporary file for each notebook which contains clingo code
            fd, path = tempfile.mkstemp()
            with open(path, "w") as f:
                postString = parenthesis_content.split("\n", 1)[1]
                f.write(postString)

            # running the clingo code in the temporary files
            ClingoInterface.run(self, path)
