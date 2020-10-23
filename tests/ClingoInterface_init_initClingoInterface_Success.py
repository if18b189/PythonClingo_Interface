# first test ... resources: https://www.jetbrains.com/pycharm/guide/tutorials/visual_pytest/hello_test/
#                           https://www.thecodebuzz.com/tdd-unit-testing-naming-conventions-and-standards/
from pythonclingointerface import ClingoInterface


def test_execute():
    assert ClingoInterface("hello")
