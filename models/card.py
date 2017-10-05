'''A card has details on a task to be carried out'''
import datetime
import functions


class Card:
    def __init__(self, name, description, due_date=None):
        self.name = name
        self.description = description
        # You don't always have to require your instance variables upfront
        # require what makes and delegate the rest to setters
        self.members = []
        self.activities = []
        self.comments = []
        self.due_date = due_date
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return functions.get_class_representation(self)

    def add_member(self, user):
        '''Add a user as a member of the card'''
        self.members.append(user)

    def add_activity(self, activity):
        '''Records activities for the card'''
        self.activities.append(activity)

    def add_comment(self, comment):
        '''Add a comment to the card'''
        self.comments.append(comment)
