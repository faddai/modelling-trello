import functions


class Board:
    def __init__(self, name, lists=[], members=[]):
        self.name = name
        self.lists = lists
        self.members = members

    def __repr__(self):
        return functions.get_class_representation(self)

    def add_list(self, board_list):
        '''Add an instance of a list to the board'''
        self.lists.append(board_list)

    def add_member(self, user):
        '''Add an instance of a user to the board so that 
        user can have access to the board
        '''
        self.members.append(user)
