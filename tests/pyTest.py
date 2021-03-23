from src.pythonclingointerface.clingo_interface import ClingoInterface

test = ClingoInterface()
test.checkParenthesis(py=False, txt=False, ipynb=True)
test.printSolutions()
