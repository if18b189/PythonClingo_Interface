import subprocess
import os
import tempfile
import glob

class ClingoSolution:
    def __init__(self,p_text):
        self.solutions=[]
        self.text=p_text
        self.go=False
        lines = self.text.splitlines()
        for line in lines:
            if self.go:
                self.solutions.append([])
                for part in line.decode("utf-8").split(" "):
                    self.solutions[len(self.solutions) - 1].append(part)
                self.go = False
            if "Answer" in line.decode("utf-8"):
                self.go = True
        self.text = self.text.decode("utf-8")

class ClingoProblem:
    def __init__(self,tmpFile=None):
        self.solution:ClingoSolution
        self.path=tmpFile
        self.executeClingoCode()

    def executeClingoCode(self):
        if self.path is not None:
            with tempfile.TemporaryFile() as tempf:
                proc = subprocess.Popen('clingo ' + self.path, shell=True, stdout=tempf)
                proc.wait()
                tempf.seek(0)
                self.solution=ClingoSolution(tempf.read())
        else:
            print("ClingoInterface:Run(): there is no file to run")

class ClingoInterface:
    def __init__(self):
        self.problems = []
        self.checkParenthesis()

    def findDirectory(self, foldername):
        sep = os.sep
        dirs = os.path.abspath("").split("\\")
        newdir = ""
        for d in dirs:
            newdir += d + sep
            if d == foldername:
                return newdir

    def checkParenthesis(self, directoryName="PythonClingo_Interface"):
        parenthesis = False
        parenthesis_start = "<CLINGO"
        parenthesis_end = "CLINGO>"
        parenthesis_content = ""
        print('ClingoInterface: jupyterParenthesis: scanning all subfolders of "' + directoryName + '"(folder) recursively for .ipynb')

        try:
            files = glob.glob(self.findDirectory(directoryName) + '**/*.ipynb',
                              recursive=True)  # searching all .ipynb recursively
            print("Found .ipynb Files: " + str(files))
        except:
            print("ClingoInterface:jnotebookParenthesis: could not find any .ipynb in the given directory, try to set directory manually")
            raise

        for file in files:
            print("Reading File: ", file)
            fs = open(file, 'r')
            if parenthesis_start in fs.read():
                print("Found Clingo Parenthesis in File: ", file)
                fs = open(file, 'r')
                con = fs.read().splitlines()  # splitlines '\n' -> list
                for line in con:
                    if parenthesis_end in line:  # checks for the end parenthesis
                        parenthesis = False
                    if parenthesis:  # adds clingo code to to parenthesis_content
                        parenthesis_content += line[5:-2].replace("\\n", "\n").replace('\\"', '"')
                    if parenthesis_start in line:  # checks for start parenthesis
                        parenthesis = True
                fd, temporaryFilePath = tempfile.mkstemp(suffix='.txt', prefix='clingoInterfaceTemp_', dir=os.getcwd(), text=True)
                with os.fdopen(fd, "w") as tmp:
                    clingoCodeContent = parenthesis_content.split("\n", 1)[1]
                    tmp.write(clingoCodeContent)
                self.problems.append(ClingoProblem(temporaryFilePath))