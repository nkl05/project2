from select_friend import select_friend
from add_status import add_status
from addfriend import add_friend

def start_chat(name,age,rating,status):
    from globals import current_status_messages
    error_message = None

    if not (age > 12 and age < 50):
        error_message = "Invalid age. provide correct details"
        print error_message
    else:
        welcome_message = "Authentication complete. Welcome"
        print welcome_message

        show_menu = True
        while show_menu:
            menu_choices = "what choice do you want ? \n " \
                            "1. Add a status update \n " \
                            "2. Add a friend \n " \
                            "3. Send a secret message \n " \
                            "4. Read a secret message \n " \
                            "5. Read chat from a user \n " \
                            "6. Close Application \n "
            result = int(input(menu_choices))

            #validating user input
            if (result == 1):
                current_status_messages = add_status(current_status_messages)
            elif (result == 2):
                number_of_friend = add_friend()
                print "You have %d friends" % (number_of_friend)
            elif (result == 3):
                select_friend()
            elif (result == 6):
                show_menu = False
            else:
                print "Wrong choice please try again...!!"