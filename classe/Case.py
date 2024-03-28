class Case:
    def __init__(self, attribute=None):
        self.attribute = attribute

    def __str__(self):
        if self.attribute is None:
            return " -"
        else:
            return str(self.attribute)[0].upper()