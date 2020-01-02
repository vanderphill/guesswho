from person import person

M1 = person("Alex", False, "black", False, True, False, True, False, False, False)
M2 = person("Alfred", False, "red", False, True, False, True, False, False, True)
M3 = person("Anita", False, "blonde", False, False, False, False, False, True, True)
M4 = person("Anne", False, "black", False, False, False, False, False, False, False)
M5 = person("Bernard", True, "brown", False, True, False, False, False, False, False)
M6 = person("Bill", False, "red", False, True, True, False, True, True, False)
M7 = person("Charles", False, "blonde", False, True, False, True, False, False, False)
M8 = person("Claire", True, "red", True, False, False, False, False, False, False)
M9 = person("David", False, "blonde", False, True, False, False, True, False, False)
M10 = person("Eric", True, "blonde", False, True, False, False, False, False, False)
M11 = person("Frans", False, "red", False, True, False, False, False, False, False)
M12 = person("George", True, "white", False, True, False, False, False, False, False)
M13 = person("Herman", False, "red", False, True, True, False, False, False, False)
M14 = person("Joe", False, "blonde", True, True, False, False, False, False, False)
M15 = person("Maria", True, "brown", False, False, False, False, False, False, True)
M16 = person("Max", False, "black", False, True, False, True, False, False, False)
M17 = person("Paul", False, "white", True, True, False, False, False, False, False)
M18 = person("Peter", False, "white", False, True, False, False, False, False, False)
M19 = person("Philip", False, "black", False, True, False, False, True, True, False)
M20 = person("Richard", False, "brown", False, True, True, True, True, False, False)
M21 = person("Robert", False, "brown", False, True, False, False, False, True, False)
M22 = person("Sam", False, "white", True, True, True, False, False, False, False)
M23 = person("Susan", False, "white", False, False, False, False, False, True, True)
M24 = person("Tom", False, "Black", True, True, True, False, False, False, False)



import random
choice = random.randint(1, 24)
if choice == 1:
    choice1 = M1
if choice == 2:
    choice1 = M2
if choice == 3:
    choice1 = M3
if choice == 4:
    choice1 = M4
if choice == 5:
    choice1 = M5
if choice == 6:
    choice1 = M6
if choice == 7:
    choice1 = M7
if choice == 8:
    choice1 = M8
if choice == 9:
    choice1 = M9
if choice == 10:
    choice1 = M10
if choice == 11:
    choice1 = M11
if choice == 12:
    choice1 = M12
if choice == 13:
    choice1 = M13
if choice == 14:
    choice1 = M14
if choice == 15:
    choice1 = M15
if choice == 16:
    choice1 = M16
if choice == 17:
    choice1 = M17
if choice == 18:
    choice1 = M18
if choice == 19:
    choice1 = M19
if choice == 20:
    choice1 = M20
if choice == 21:
    choice1 = M21
if choice == 22:
    choice1 = M22
if choice == 23:
    choice1 = M23
if choice == 24:
    choice1 = M24

print(choice1.name)

def func():
    i = 0
    while i < 1:
        question = input("ask me a question about my person")
        print(question)

        if (("male" in question) and ((choice1.male) == False)):
            print("my person is a female")
            i += 1
        elif (("male" in question) and ((choice1.male) == True)):
            print("my person is a male")
            i += 1
        elif (("hat" in question) and (choice1.hat == True)):
            print("yes, my person has a hat")
            i += 1
        elif (("hat" in question) and (choice1.hat == False)):
            print("No, my person does not have a hat")
            i += 1
        elif (("blonde" in question) and (choice1.hair_color == "blonde")):
            print("yes, my person has blonde hair")
            i += 1
        elif (("blonde" in question) and (choice1.hair_color != "blonde")):
            print("No, my person does not have blonde hair")
            i += 1
        elif (("black" in question) and (choice1.hair_color == "black")):
            print("yes, my person has black hair")
            i += 1
        elif (("black" in question) and (choice1.hair_color != "black")):
            print("No, my person does not have black hair")
            i += 1
        elif (("red" in question) and (choice1.hair_color == "red")):
            print("yes, my person has red hair")
            i += 1
        elif (("red" in question) and (choice1.hair_color != "red")):
            print("No, my person does not have red hair")
            i += 1
        elif (("brown" in question) and (choice1.hair_color == "brown")):
            print("yes, my person has brown hair")
            i += 1
        elif (("blonde" in question) and (choice1.hair_color != "brown")):
            print("No, my person does not have brown hair")
            i += 1
        elif (("white" in question) and (choice1.hair_color == "white")):
            print("yes, my person has white hair")
            i += 1
        elif (("white" in question) and (choice1.hair_color != "white")):
            print("No, my person does not have white hair")
            i += 1
        elif (("glasses" in question) and (choice1.glasses == True)):
            print("yes, my person has glasses")
            i += 1
        elif (("glasses" in question) and (choice1.glasses == False)):
            print("No, my person does not have glasses")
            i += 1

        elif (("bald" in question) and (choice1.bald == True)):
            print("yes, my person is bald")
            i += 1
        elif (("bald" in question) and (choice1.bald == False)):
            print("No, my person is not bald")
            i += 1
        elif (("mustache" in question) and (choice1.mustache == True)):
            print("yes, my person has a mustache ")
            i += 1
        elif (("mustache" in question) and (choice1.mustache == False)):
            print("No, my person doesn't have a mustache ")
            i += 1
        elif (("long" in question) and (choice1.long_hair == True)):
            print("yes, my person has a long hair ")
            i += 1
        elif (("long" in question) and (choice1.long_hair == False)):
            print("No, my person doesn't have long hair ")
            i += 1
        elif (("beard" in question) and (choice1.beard == True)):
            print("yes, my person has a beard")
            i += 1
        elif (("beard" in question) and (choice1.beard == False)):
            print("No, my person does not have a beard")
            i += 1
        elif (("cheeks" in question) and (choice1.rosie_cheeks == True)):
            print("yes my person has rosie cheeks")
            i += 1
        elif (("cheeks" in question) and (choice1.rosie_cheeks == False)):
            print("No, my person doesn't have rosie cheeks")
            i += 1
        elif ((choice1.name) in question):
            print("you guessed my person " + choice1.name + "\n YOU WIN!!")
            print(str(i) + " guesses")
            i += 12


again = True
while again == True:

    Cwin = False
    while Cwin == False:
        pick = input("Pick a person from the sheet and don't tell me who it is, OK?")
        if pick in (("alexalfredanitaannebernardbillcharlesclairedavidericfransgeorgehermanjoemariamaxpaulpeterphiliprichardrobertsamsusantom")):
            print("I TOLD YOU NOT TO TELL ME!!! \n YOU LOSE!!!")
            again = False
            Cwin = False
            break

        print("I have also picked a person, I'll go first. ")



        sex = input("Is your person a male? ")
        if sex == "no":
            func()
            hatf = input("Is she wearing a hat? ")
            if hatf == "yes":
                func()
                glassesf = input("is she wearing glasses? ")
                if glassesf == "yes":
                    func()
                    print("your person is Claire")
                    Cwin = True
                if glassesf == "no":
                    func()
                    print("your person is Maria")
                    Cwin = True
            if hatf == "no":
                func()
                whitef = input("does she have white hair? ")
                if whitef == "yes":
                    func()
                    print("Your person is Susan")
                    game_done = True
                if whitef == "no":
                    func()
                    blackf = input("does she have black hair? ")
                    if blackf == "yes":
                        func()
                        print("Your person is Anne")
                    if blackf == "no":
                        func()
                        print("Your person is Anita")
                        Cwin = True
        if sex == "yes":
            func()
            hatm = input("Is he wearing a hat? ")
            if hatm == "yes":
                func()
                blondem1 = input("is he blonde? ")
                if blondem1 == "yes":
                    func()
                    print("your person is Eric")
                if blondem1 == "no":
                    func()
                    whitem1 = input("Does he have white hair? ")
                    if whitem1 == "yes":
                        func()
                        print("your person is George")
                        Cwin = True
                    if whitem1 == "no":
                        func()
                        print("your person is Bernard")
                        Cwin = True
            if hatm == "no":
                func()
                glassesm1 = input("Is he wearing glasses? ")
                if glassesm1 == "yes":
                    func()
                    bald1 = input("is he bald? ")
                    if bald1 == "yes":
                        func()
                        black1 = input("does he have black hair? ")
                        if black1 == "yes":
                            func()
                            print("your person is Tom")
                            Cwin = True
                        if black1 == "no":
                            func()
                            print("your person is Sam")
                            Cwin = True
                    if bald1 == "no":
                        func()
                        blondem1 = input("does he have blonde hair? ")
                        if blondem1 == "yes":
                            func()
                            print("your person is Joe")
                            Cwin = True
                        if blondem1 == "no":
                            func()
                            print("your person is Paul")
                            Cwin = True
                if glassesm1 == "no":
                    func()
                    mustache1 = input("does he have a mustache? ")
                    if mustache1 == "yes":
                        func()
                        symetric1 = input("does he have symetrical eye brows? ")
                        if symetric1 == "yes":
                            func()
                            blackm2 = input("does he have black hair? ")
                            if blackm2 == "yes":
                                func()
                                print("your person is Max")
                                Cwin = True
                            if blackm2 == "no":
                                func()
                                beard2 = input("does he have a beard? ")
                                if beard2 == "yes":
                                    func()
                                    print("your person is Richard")
                                    Cwin = True
                                if beard2 == "no":
                                    func()
                                    print("your person is Charles")
                                    Cwin = True
                        if symetric1 == "no":
                            func()
                            blackm3 = input("does he have black hair? ")
                            if blackm3 == "yes":
                                func()
                                print("your person is Alex")
                                Cwin = True
                            if blackm3 == "no":
                                func()
                                print("your person is Alfred")
                                Cwin = True
                            if blackm3 == "what?":
                                what3 = input("WHAT COUNTRY ARE YOU FROM!")
                                if what3 == "what?":
                                    what1 = input("What ain't no country I ever heard of; do they speak english in what?")
                                    if what1 == "what?":
                                        what2 = input("ENGLISH MOTHER F*##ER! DO YOU SPEAK IT!?")
                                        if what2 == "yes":
                                            yeah1 = input("then you understand what I am saying to you?")
                                            if yeah1 == "yes":
                                                print("DOES HE LOOK LIKE A BITCH!!")




                    if mustache1 == "no":
                        func()
                        redh = input("Does he have Red hair? ")
                        if redh == "yes":
                            func()
                            bald2 = input("Is he bald? ")
                            if bald2 == "yes":
                                func()
                                rosie = input("does he have rosie cheeks? ")
                                if rosie == "yes":
                                    func()
                                    print("your person is Bill")
                                    Cwin = True
                                if rosie == "no":
                                    func()
                                    print("your person is Herman")
                                    Cwin = True
                            if bald2 == "no":
                                func()
                                print("your person is Frans")
                                Cwin = True
                        elif redh == "no":
                            func()
                            beard3 = input("does he have a beard? ")
                            if beard3 == "yes":
                                func()
                                blondem2 = input("does he have blonde hair?")
                                if blondem2 == "yes":
                                    func()
                                    print("your person is David")
                                    Cwin = True
                                if blondem2 == "no":
                                    func()
                                    print("your person is Philip")
                            if beard3 == "no":
                                func()
                                brown1 = input("does he have brown hair? ")
                                if brown1 == "yes":
                                    func()
                                    print("your person is Robert")
                                    Cwin = True
                                if brown1 == "no":
                                    func()
                                    print("your person is peter")
                                    Cwin = True
        if Cwin == True:
            print("I have guessed your person")
        again1 = input("would you like to play again?")
        if again == "no":
            Cwin = False
            again = False

