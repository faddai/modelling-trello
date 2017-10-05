# Trello Clone

This is how I would model my objects if I were building a clone of Trello.

## Classes

* User
    - firstname
    - lastname
    - email
    - password
    + hash_password
    + login
    + signup

* Board
    - name
    - members
    - lists
    + add_member
    + add_list

* List
    - name
    - cards
    + add_card
    + move_card

* Card
    - title
    - members
    - comments
    - description
    - due_date
    - activities
    + archive

* Activity
    - performed_by
    - timestamp
    - description