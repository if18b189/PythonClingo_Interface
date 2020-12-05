# first test ... resources: https://www.jetbrains.com/pycharm/guide/tutorials/visual_pytest/hello_test/
#                           https://www.thecodebuzz.com/tdd-unit-testing-naming-conventions-and-standards/
from pythonclingointerface import ClingoInterface


def test_execute():
    test = ClingoInterface("test")
    assert test.execute() == "test"

test=ClingoInterface()
print(test.solutions)
for i in test.solutions:
    print(i.text)
    print(i.solutions)
