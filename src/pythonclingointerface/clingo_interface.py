import subprocess

# class ClingoInterface:
#
#     def __init__(self, text):
#         self.text = text
#
#     def execute(self):
#         return self.text

    # def addFact(self,varName,var):
    #     return


# output for testing purpose only
# obj = ClingoInterface("hello world")
# print(obj.execute())

#Clingo
# subprocess.call(['Exes/Executable.exe','hello','to you'])

var=subprocess.call('clingo')
print(type(var))

