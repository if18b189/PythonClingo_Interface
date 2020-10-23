class ClingoInterface:

    def __init__(self, text):
        self.text = text

    def execute(self):
        return self.text


# output for testing purpose only
obj = ClingoInterface("hello world")
print(obj.execute())
