#spy_salutation = 'Mr.'
#spy_name = 'Abhilash'
#spy_age = 32
#spy_rating = 4.8
#spy_is_online = True

#Spy ={
 #   'name' : '',
  #  'salutation' : '',
   # 'age' : 0,
    #'spy_rating' : 0.0,
    #'spy_is_online': True
#}

from datetime import datetime

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.spy_is_online = True
        self.chats = []
        self.current_status_messages = None


# one default spy details
spy = Spy('Abhilash', 'Mr.', 22, 4.7)

friend_one = Spy('Chetan', 'Mr', 21,4.5)
friend_two = Spy('Chetan', 'Mr', 21,4.5)
friend_three = Spy('Chetan', 'Mr', 21,4.5)
friends = [friend_one, friend_two, friend_three]


class Chat:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me