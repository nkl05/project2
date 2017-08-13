from Spydetails import spy_name, spy_salutation, spy_age, spy_rating,spy_is_online

print "Lets get started"
print "Do you want to continue as " + spy_salutation+" " +spy_name
existing_user = raw_input("enter y/n")
if(existing_user.upper() == "Y"):
    #procced with default user
    spy_name = spy_salutation + " " + spy_name
    print "Welcome Back " +spy_salutation +" " +spy_name
    print "%s is your spy rating" % (spy_rating)
    print "Your age is : %s" % (spy_age)

else:
    #new input
    spy_name = raw_input("Welcome to spy chat, you must enter your name here: ")
    #check is spy has something or not
    if len(spy_name)>0:
        spy_salutation = raw_input("should I call you Mr. or Mrs. :")
        spy_age = raw_input("What is your age")
        spy_age = int(spy_age)

        spy_rating = raw_input("What is your spy rating")
        spy_rating = float(spy_rating)

        spy_is_online = True
        print "Your authentication is verified %s %s\n Your seem to be a very young spy with an age of %s \n with an excellent rating of" % (spy_salutation,spy_name,spy_age)