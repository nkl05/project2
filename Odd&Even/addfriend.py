from globals import friends

def add_friend():
    new_friend_name = {
        'name':'',
        'salutation':'',
        'age':0,
        'rating':0.0,
        'is online': False

    }
    new_friend_name['name'] = raw_input("Please add your friend's")
    new_friend_name['salutation'] =raw_input("Is he/she ")

    new_friend_name['name']= new_friend_name['salutation'] + " " + new_friend_name['name']

    new_friend_name['age'] = int(raw_input("Age .? "))
    new_friend_name['rating'] = float(raw_input("rating is..?? "))

    if len(new_friend_name['name'])> 0 and new_friend_name['age']> 12 and new_friend_name['age']<55:
        new_friend_name['is online'] = True
        friends.append(new_friend_name)
        print "Friend is added..!!"
    else:
        print "user has not inserted any value"
    return len(friends)
