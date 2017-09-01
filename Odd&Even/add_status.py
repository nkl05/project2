from globals import STATUS_MESSAGES

updated_status_message = None

def add_status(current_status_message):
    if current_status_message != None:
        print "your current status message is " + current_status_message + "\n"
    else:
        print "you don't have any status message currently \n"
    default = raw_input("Do you want to select from older messages y/n")
    if default.upper() == "N":
        new_status_message = raw_input("what status message do you want")

        if len(new_status_message)>0:
            update_status_message = new_status_message
            STATUS_MESSAGES.append(update_status_message)
            print 'your updated status message is : %s' % (update_status_message)
        else:
            print 'you did not provided any status..'
    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print str(item_position) + ". " + message
            item_position = item_position + 1
        #asking users choice.
        message_selection = int(input("\n Choose from the "))

        #validating user input
        if len(STATUS_MESSAGES) >=message_selection:
            update_status_message = STATUS_MESSAGES(message_selection)
            print "Your updated status message is : %s" % ()
        else:
            print "Invalid choice"
    else:
        print "The option you chose is not valid.."

    return update_status_message