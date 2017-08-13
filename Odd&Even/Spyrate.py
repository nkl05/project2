spy_name = raw_input("Enter the Spy Name: ")
spy_is_online = True

if len(spy_name)>0:
    spy_salutation = raw_input("Add your salutation like Mr. or Mrs.: ")
    spy_name = spy_salutation + " " + spy_name
    spy_age = raw_input("Enter spy's age: ")
    spy_rate = raw_input("Give rating to spy by your opinion: ")

    if (spy_age.isdigit() or spy_salutation.isalpha()):
        print spy_name
        print spy_age
        print spy_rate
    else:
        print "User has entered wrong input datatype"

else:
    print "Name is empty"