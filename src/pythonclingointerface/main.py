from pythonclingointerface import clingo_interface


def main():
    # test = clingo_interface.ClingoInterface()
    # path = test.jnotebookParenthesis()
    # test.run(path)

    test = clingo_interface.ClingoInterface()
    path = test.jupyterParenthesis()
    test.run(path)
    test.printSolutions()

    # path = os.path.abspath("")
    #
    # print("absolute: " + path)
    # print("old: " + os.path.join(os.path.abspath(".\\PycharmProjects")))
    #
    # print(findDirectory("PythonClingo_Interface"))

    # ClingoInterface("text").run("clingoCodeExample")


main()
