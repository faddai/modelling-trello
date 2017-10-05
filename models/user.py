'''Model a User object
'''
import hashlib
import csv
import functions


DATASTORE = 'users.csv'

class User:
    '''A user on trello'''
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = self.hash_password(password)
        self.is_logged_in = False

    def __repr__(self):
        return functions.get_class_representation(self)

    def hash_password(self, password):
        '''Hash a given password'''
        return hashlib.sha256(password).hexdigest()

    def login(self, email, password):
        self.is_logged_in = True

    def save(self):
        with open(DATASTORE, 'a+') as file:
            store = csv.DictWriter(file, ['firstname', 'lastname', 'email', 'password', 'is_logged_in'])
            
            if file.readline() == '':
                store.writeheader()
            
            store.writerow(self.__dict__)
