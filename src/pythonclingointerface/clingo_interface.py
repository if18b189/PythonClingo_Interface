import subprocess
import os
import tempfile
import sys
import glob

"""Solution Format"""
class ClingoSolutions:
    def __init__(self, clingoCode):
        if(type(clingoCode==bytes)):
            self.text=clingoCode
        if(type(clingoCode==str)):
            self.text=clingoCode
        self.solutions=[]
        lines=self.text.splitlines()
        go=False
        for line in lines:
            if (go):
                self.solutions.append([])
                """Parts of the solution can be accessed too. """
                for part in line.decode("utf-8").split(" "):
                    self.solutions[len(self.solutions) - 1].append(part)
                go = False
            """If it is an awnser, the next line will be saved as a Solution. """
            if ("Answer" in line.decode("utf-8")):
                go = True
        self.text=self.text.decode("utf-8")

class ClingoProblem:
    def __init__(self):
        self.name:str
        pass

    def run(self):
        pass


"""Looking for Code"""
class ClingoInterface:
    def __init__(self):
        self.solutions=[]
        # ClingoInterface.check_jnotebook_parenthesis(self)

    def run(self, file_or_code):
        with tempfile.TemporaryFile() as tempf:  # reading into a temporary file prevents issues with bigger input values
            proc = subprocess.Popen('clingo ' + file_or_code, shell=True, stdout=tempf)
            proc.wait()
            tempf.seek(0)
            self.solutions.append(ClingoSolutions(tempf.read()))

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
            print("Clingo Code found in: ", file)
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



