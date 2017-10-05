'''Trello application
Putting our hard work to good use
'''
import models.user
import models.board
import models.card
import models.boardlist

firstname = input('Please enter your first name: ')
lastname = input('Please enter your last name: ')
email = input('Please enter your email: ')
password = input('Please enter your password: ')

user = models.user.User(firstname, 
                        lastname, 
                        email, 
                        bytes(password, 'utf-8'))

print(user)