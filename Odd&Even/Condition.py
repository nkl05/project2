spy_name = raw_input("enter the name: ")
if len(spy_name)>0:
    #start writing from here now. See how this is under the if statement?
    print "Welcome " + spy_name + " glad to have you with us"
    spy_salutation = raw_input("what should I call you Mr. or Mrs. or your wish: ")
    spy_name = spy_salutation + " " + spy_name
    print "Alright " + spy_name + " what are you good at..??"
