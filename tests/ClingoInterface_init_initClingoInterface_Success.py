from src.pythonclingointerface.clingo_interface import ClingoInterface




test=ClingoInterface()
print(test.problems[0].solution.solutions)
# for i in test.solutions:
#     print(i.text)
#     print(i.solutions)

