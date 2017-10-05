import functions


class BoardList:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return functions.get_class_representation(self)
    