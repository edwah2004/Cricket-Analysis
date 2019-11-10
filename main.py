import time, csv

while True:
    print ("\n\n*********************************************")
    bowlerName = input ("Enter the name of the bowler: ")
    batterName = input ("Enter the name of the batter: ")
    hit = ("n")
    howOut = ("Not Out")

    ballInput = True

    while ballInput == True:
        ballLengthInput = input ("\nWhat was the length of the ball?\n1.Short\n2.Back of a Length\n3.Good Length\n4.Full\n5.Yorker\n")
        if ballLengthInput == ("1"):
            print ("Short Selected")
            ballLineInput = input ("\nWhat was the line of the ball?\n1.Wide Off Side\n2.Far Outside Off\n3.Outside Off\n4.Off Stump\n5.Middle Stump\n6.Leg Stump\n7.Outside Leg\n8.Far Outside Leg\n9.Wide Leg Side\n")

            if ballLineInput == ("1"):
                print ("Wide Off Side Selected")
                ballLength = ("Short")
                ballLine = ("Wide Off Side")
                ballInput = False

            elif ballLineInput == ("2"):
                print ("Far Outside Off Selected")
                ballLength = ("Short")
                ballLine = ("Far Outside Off")
                ballInput = False

            elif ballLineInput == ("3"):
                print ("Outside Off Selected")
                ballLength = ("Short")
                ballLine = ("Outside Off")
                ballInput = False

            elif ballLineInput == ("4"):
                print ("Off Stump Selected")
                ballLength = ("Short")
                ballLine = ("Off Stump")
                ballInput = False

            elif ballLineInput == ("5"):
                print ("Middle Stump Selected")
                ballLength = ("Short")
                ballLine = ("Middle Stump")
                ballInput = False

            elif ballLineInput == ("6"):
                print ("Leg Stump Selected")
                ballLength = ("Short")
                ballLine = ("Leg Stump")
                ballInput = False

            elif ballLineInput == ("7"):
                print ("Outside Leg Selected")
                ballLength = ("Short")
                ballLine = ("Outside Leg")
                ballInput = False

            elif ballLineInput == ("8"):
                print ("Far Outside Leg Selected")
                ballLength = ("Short")
                ballLine = ("Far Outside Leg")
                ballInput = False

            elif ballLineInput == ("9"):
                print ("Wide Leg Side Selected")
                ballLength = ("Short")
                ballLine = ("Wide Leg Side")
                ballInput = False

            else:
                print ("That was not a valid option.")


        elif ballLengthInput == ("2"):
            print ("Back of a Length Selected")
            ballLineInput = input ("\nWhat was the line of the ball?\n1.Wide Off Side\n2.Far Outside Off\n3.Outside Off\n4.Off Stump\n5.Middle Stump\n6.Leg Stump\n7.Outside Leg\n8.Far Outside Leg\n9.Wide Leg Side\n")

            if ballLineInput == ("1"):
                print ("Wide Off Side Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Wide Off Side")
                ballInput = False

            elif ballLineInput == ("2"):
                print ("Far Outside Off Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Far Outside Off")
                ballInput = False

            elif ballLineInput == ("3"):
                print ("Outside Off Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Outside Off")
                ballInput = False

            elif ballLineInput == ("4"):
                print ("Off Stump Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Off Stump")
                ballInput = False

            elif ballLineInput == ("5"):
                print ("Middle Stump Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Middle Stump")
                ballInput = False

            elif ballLineInput == ("6"):
                print ("Leg Stump Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Leg Stump")
                ballInput = False

            elif ballLineInput == ("7"):
                print ("Outside Leg Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Outside Leg")
                ballInput = False

            elif ballLineInput == ("8"):
                print ("Far Outside Leg Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Far Outside Leg")
                ballInput = False

            elif ballLineInput == ("9"):
                print ("Wide Leg Side Selected")
                ballLength = ("Back of a Length")
                ballLine = ("Wide Leg Side")
                ballInput = False
            else:
                print ("That was not a valid option.")


        elif ballLengthInput == ("3"):
            print ("Good Length Selected")
            ballLineInput = input ("\nWhat was the line of the ball?\n1.Wide Off Side\n2.Far Outside Off\n3.Outside Off\n4.Off Stump\n5.Middle Stump\n6.Leg Stump\n7.Outside Leg\n8.Far Outside Leg\n9.Wide Leg Side\n")

            if ballLineInput == ("1"):
                print ("Wide Off Side Selected")
                ballLength = ("Good Length")
                ballLine = ("Wide Off Side")
                ballInput = False

            elif ballLineInput == ("2"):
                print ("Far Outside Off Selected")
                ballLength = ("Good Length")
                ballLine = ("Far Outside Off")
                ballInput = False

            elif ballLineInput == ("3"):
                print ("Outside Off Selected")
                ballLength = ("Good Length")
                ballLine = ("Outside Off")
                ballInput = False

            elif ballLineInput == ("4"):
                print ("Off Stump Selected")
                ballLength = ("Good Length")
                ballLine = ("Off Stump")
                ballInput = False

            elif ballLineInput == ("5"):
                print ("Middle Stump Selected")
                ballLength = ("Good Length")
                ballLine = ("Middle Stump")
                ballInput = False

            elif ballLineInput == ("6"):
                print ("Leg Stump Selected")
                ballLength = ("Good Length")
                ballLine = ("Leg Stump")
                ballInput = False

            elif ballLineInput == ("7"):
                print ("Outside Leg Selected")
                ballLength = ("Good Length")
                ballLine = ("Outside Leg")
                ballInput = False

            elif ballLineInput == ("8"):
                print ("Far Outside Leg Selected")
                ballLength = ("Good Length")
                ballLine = ("Far Outside Leg")
                ballInput = False

            elif ballLineInput == ("9"):
                print ("Wide Leg Side Selected")
                ballLength = ("Good Length")
                ballLine = ("Wide Leg Side")
                ballInput = False

            else:
                print ("That was not a valid option.")


        elif ballLengthInput == ("4"):
            print ("Full Selected")
            ballLineInput = input ("\nWhat was the line of the ball?\n1.Wide Off Side\n2.Far Outside Off\n3.Outside Off\n4.Off Stump\n5.Middle Stump\n6.Leg Stump\n7.Outside Leg\n8.Far Outside Leg\n9.Wide Leg Side\n")

            if ballLineInput == ("1"):
                print ("Wide Off Side Selected")
                ballLength = ("Full")
                ballLine = ("Wide Off Side")
                ballInput = False

            elif ballLineInput == ("2"):
                print ("Far Outside Off Selected")
                ballLength = ("Full")
                ballLine = ("Far Outside Off")
                ballInput = False

            elif ballLineInput == ("3"):
                print ("Outside Off Selected")
                ballLength = ("Full")
                ballLine = ("Outside Off")
                ballInput = False

            elif ballLineInput == ("4"):
                print ("Off Stump Selected")
                ballLength = ("Full")
                ballLine = ("Off Stump")
                ballInput = False

            elif ballLineInput == ("5"):
                print ("Middle Stump Selected")
                ballLength = ("Full")
                ballLine = ("Middle Stump")
                ballInput = False

            elif ballLineInput == ("6"):
                print ("Leg Stump Selected")
                ballLength = ("Full")
                ballLine = ("Leg Stump")
                ballInput = False

            elif ballLineInput == ("7"):
                print ("Outside Leg Selected")
                ballLength = ("Full")
                ballLine = ("Outside Leg")
                ballInput = False

            elif ballLineInput == ("8"):
                print ("Far Outside Leg Selected")
                ballLength = ("Full")
                ballLine = ("Far Outside Leg")
                ballInput = False

            elif ballLineInput == ("9"):
                print ("Wide Leg Side Selected")
                ballLength = ("Full")
                ballLine = ("Wide Leg Side")
                ballInput = False
            else:
                print ("That was not a valid option.")


        elif ballLengthInput == ("5"):
            print ("Yorker Selected")
            ballLineInput = input ("\nWhat was the line of the ball?\n1.Wide Off Side\n2.Far Outside Off\n3.Outside Off\n4.Off Stump\n5.Middle Stump\n6.Leg Stump\n7.Outside Leg\n8.Far Outside Leg\n9.Wide Leg Side\n")

            if ballLineInput == ("1"):
                print ("Wide Off Side Selected")
                ballLength = ("Yorker")
                ballLine = ("Wide Off Side")
                ballInput = False

            elif ballLineInput == ("2"):
                print ("Far Outside Off Selected")
                ballLength = ("Yorker")
                ballLine = ("Far Outside Off")
                ballInput = False

            elif ballLineInput == ("3"):
                print ("Outside Off Selected")
                ballLength = ("Yorker")
                ballLine = ("Outside Off")
                ballInput = False

            elif ballLineInput == ("4"):
                print ("Off Stump Selected")
                ballLength = ("Yorker")
                ballLine = ("Off Stump")
                ballInput = False

            elif ballLineInput == ("5"):
                print ("Middle Stump Selected")
                ballLength = ("Yorker")
                ballLine = ("Middle Stump")
                ballInput = False

            elif ballLineInput == ("6"):
                print ("Leg Stump Selected")
                ballLength = ("Yorker")
                ballLine = ("Leg Stump")
                ballInput = False

            elif ballLineInput == ("7"):
                print ("Outside Leg Selected")
                ballLength = ("Yorker")
                ballLine = ("Outside Leg")
                ballInput = False

            elif ballLineInput == ("8"):
                print ("Far Outside Leg Selected")
                ballLength = ("Yorker")
                ballLine = ("Far Outside Leg")
                ballInput = False

            elif ballLineInput == ("9"):
                print ("Wide Leg Side Selected")
                ballLength = ("Yorker")
                ballLine = ("Wide Leg Side")
                ballInput = False
            else:
                print ("That was not a valid option.")

        else:
            print ("That was not a valid option.")

    runs = input ("\nHow Many Runs Did the Batter Hit? (type OUT for a wicket) ")

    if runs == ("0"):
        hit = input("\nDid the Batter Hit the Ball? (y/n) ")
    elif runs == ("1"):
        hit = ("y")
    elif runs == ("2"):
        hit = ("y")
    elif runs == ("3"):
        hit = ("y")
    elif runs == ("4"):
        hit = ("y")
    elif runs == ("5"):
        hit = ("y")
    elif runs == ("6"):
        hit = ("y")
    elif runs == ("OUT"):
        hit = input("\nDid the Batter Hit the Ball (y/n) ")
        howOut = input("\nHow Did the Batter Get Out? ")

    if hit == ("y"):
        areaInput = input ("\nWhere Did the Batter Hit the Ball? \n1.Leg Side Behind Square\n2.Leg Side In Front of Square\n3.Straight\n4.Off Side In Front of Square\n5.Off Side Behind Square\n")

    fieldedInput = input("\nWas the ball Fielded? (y/n) ")
    if fieldedInput == ("y"):
        fielderName = input ("What was the Name of the Fielder? ")
        fielderHand = input ("Which Hand(s) did the Fielder Use? ")
        fielderHightInput = input ("What Type of Fielding Took Place?\n1.Ground\n2.Flat Catch\n3.Medium Height Catch\n4.High Catch\n")
        if fielderHightInput == ("1"):
            fielderHight = ("Ground")
        elif fielderHightInput == ("2"):
            fielderHight = ("Flat Catch")
        elif fielderHightInput == ("3"):
            fielderHight = ("Medium Catch")
        elif fielderHightInput == ("4"):
            fielderHight = ("High Catch")

        wasFumbled = input ("\nDid the Fielder Fumble the Ball? (y/n) ")
        if wasFumbled == ("y"):
            wasFumbled = ("Fumbled")
        else:
            wasFumbled = ("Clean")

        fieldnames = ["bowlerName","batterName","ballLine","ballLength","Runs","hit","howOut","Fielded","fielderName","fielderHand","fielderHight","wasFumbled"]

        with open("analysis.csv","a") as analysisFile:
            writer = csv.DictWriter(analysisFile, fieldnames = fieldnames)
            writer.writerow({"bowlerName":bowlerName,"batterName":batterName,"ballLine":ballLine,"ballLength":ballLength,"Runs":runs,"hit":hit,"howOut":howOut,"Fielded":fieldedInput,"fielderName":fielderName,"fielderHand":fielderHand,"fielderHight":fielderHight,"wasFumbled":wasFumbled})
            analysisFile.close()
