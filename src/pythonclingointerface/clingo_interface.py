import subprocess
import os
import tempfile
import glob


class ClingoSolution:
    def __init__(self, p_text):
        self.solutions = []
        self.text = p_text
        self.go = False
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
    def __init__(self, tmpFile=None, autoexecute=True, clingoString=None, name="Problem Name"):
        self.solution: ClingoSolution
        self.name = name
        self.path = tmpFile
        self.problemCode = clingoString

        if (autoexecute):
            self.executeClingoCode()
            if (clingoString and tmpFile == None):
                fd, tmpFile = tempfile.mkstemp(suffix='.txt', prefix='clingoInterfaceTemp_', dir=os.getcwd(), text=True)
                with os.fdopen(fd, "w") as tmp:
                    tmp.write(clingoString)
                self.executeClingoCode()
                os.remove(tmpFile)

    def executeClingoCode(self):
        if self.path is not None:
            with tempfile.TemporaryFile() as tempf:
                proc = subprocess.Popen('clingo ' + self.path, shell=True, stdout=tempf)
                proc.wait()
                tempf.seek(0)
                self.solution = ClingoSolution(tempf.read())
        else:
            print("ClingoInterface:Run(): there is no file to run")


class ClingoInterface:
    def __init__(self):
        self.problems = []

    def printSolutions(self):
        print(self.problems)
        for i in self.problems:
            print(i.name)
            print(i.solution.solutions)

    def run(self, pathList_or_code):
        if type(pathList_or_code) is list:
            for path in pathList_or_code:
                self.executeClingoCode(path)
        else:
            self.executeClingoCode(pathList_or_code)

    def findDirectory(self, foldername):
        sep = os.sep
        dirs = os.path.abspath("").split("\\")
        newdir = ""
        for d in dirs:
            newdir += d + sep
            if d == foldername:
                return newdir

    def checkParenthesis(self, directoryName="PythonClingo_Interface", py=True, txt=True, ipynb=True):
        parenthesis = False
        parenthesis_start = "<CLINGO"
        parenthesis_end = "CLINGO>"
        parenthesis_content = ""
        print('ClingoInterface: jupyterParenthesis: scanning all subfolders of "' + directoryName + '"(folder) recursively for .ipynb')
        files = []
        print(self.findDirectory(directoryName))
        try:
            if (py):
                files.extend(glob.glob(self.findDirectory(directoryName) + '**/*.py', recursive=True))
            if (txt):
                files.extend(glob.glob(self.findDirectory(directoryName) + '**/*.txt', recursive=True))
            if (ipynb):
                files.extend(glob.glob(self.findDirectory(directoryName) + '**/*.ipynb', recursive=True))

            print("Found .ipynb Files: " + str(files))
        except:
            print(
                "ClingoInterface:jnotebookParenthesis: could not find any .ipynb in the given directory, try to set directory manually")
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
                fd, temporaryFilePath = tempfile.mkstemp(suffix='.txt', prefix='clingoInterfaceTemp_', dir=os.getcwd(),
                                                         text=True)
                with os.fdopen(fd, "w") as tmp:
                    print(parenthesis_content)
                    clingoCodeContent = parenthesis_content.split("\n", 1)
                    if len(clingoCodeContent) > 1:
                        clingoCodeContent = clingoCodeContent[1]
                    else:
                        return
                    tmp.write(clingoCodeContent)
                self.problems.append(ClingoProblem(temporaryFilePath))
                os.remove(temporaryFilePath)
