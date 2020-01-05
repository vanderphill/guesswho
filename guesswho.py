from tkinter import *
from PIL import Image, ImageTk
from person import person
from tkinter import messagebox
import random
root = Tk()
root.title("Guess Who!")
root.bg = "yellow"
topFrame = Frame(root)
title = Label(topFrame, text="Guess Who!", font='Helvetica 22 bold', width="38", fg="brown", bg="yellow").pack()
topFrame.grid(row=0, column=0, columnspan=3)

x = 15
y = 15

start = ImageTk.PhotoImage(Image.open("Start.png"))
mainFrame = Frame(root, bg="yellow", width="50", padx=42, pady=3)
questionFrame = Frame(root, bg="yellow", padx=1, pady=31)
questionFrame2 = Frame(root, bg="yellow", padx=1, pady=31)
choiceFrame = Frame(root, bg="yellow", pady=3)
urchar = start
choice = Label(choiceFrame, bg="yellow", padx=15, pady=15, image=urchar)
yourcharcter = Label(choiceFrame, text="Your Person", font='Helvetica 15 bold', bg="yellow", fg="brown")
choice.pack()
yourcharcter.pack()
mainFrame.grid(row=1, column=0, columnspan=3)
questionFrame.grid(row=2, column=0)
choiceFrame.grid(row=2, column=1)
questionFrame2.grid(row=2, column=2)

Aleximage1 = ImageTk.PhotoImage(Image.open("Alex.png"))
Alfredimage1 = ImageTk.PhotoImage(Image.open("Alfred.png"))
Anitaimage1 = ImageTk.PhotoImage(Image.open("Anita.png"))
Anneimage1 = ImageTk.PhotoImage(Image.open("Anne.png"))
Bernardimage1 = ImageTk.PhotoImage(Image.open("Bernard.png"))
Billimage1 = ImageTk.PhotoImage(Image.open("Bill.png"))
Charlesimage1 = ImageTk.PhotoImage(Image.open("Charles.png"))
Claireimage1 = ImageTk.PhotoImage(Image.open("Claire.png"))
Davidimage1 = ImageTk.PhotoImage(Image.open("David.png"))
Ericimage1 = ImageTk.PhotoImage(Image.open("Eric.png"))
Fransimage1 = ImageTk.PhotoImage(Image.open("Frans.png"))
Georgeimage1 = ImageTk.PhotoImage(Image.open("George.png"))
Hermanimage1 = ImageTk.PhotoImage(Image.open("Herman.png"))
Joeimage1 = ImageTk.PhotoImage(Image.open("Joe.png"))
Mariaimage1 = ImageTk.PhotoImage(Image.open("Maria.png"))
Maximage1 = ImageTk.PhotoImage(Image.open("Max.png"))
Paulimage1 = ImageTk.PhotoImage(Image.open("Paul.png"))
Peterimage1 = ImageTk.PhotoImage(Image.open("Peter.png"))
Philipimage1 = ImageTk.PhotoImage(Image.open("Philip.png"))
Richardimage1 = ImageTk.PhotoImage(Image.open("Richard.png"))
Robertimage1 = ImageTk.PhotoImage(Image.open("Robert.png"))
Samimage1 = ImageTk.PhotoImage(Image.open("Sam.png"))
Susanimage1 = ImageTk.PhotoImage(Image.open("Susan.png"))
Tomimage1 = ImageTk.PhotoImage(Image.open("Tom.png"))

AleximageX = ImageTk.PhotoImage(Image.open("AlexX.png"))
AlfredimageX = ImageTk.PhotoImage(Image.open("AlfredX.png"))
AnitaimageX = ImageTk.PhotoImage(Image.open("AnitaX.png"))
AnneimageX = ImageTk.PhotoImage(Image.open("AnneX.png"))
BernardimageX = ImageTk.PhotoImage(Image.open("BernardX.png"))
BillimageX = ImageTk.PhotoImage(Image.open("BillX.png"))
CharlesimageX = ImageTk.PhotoImage(Image.open("CharlesX.png"))
ClaireimageX = ImageTk.PhotoImage(Image.open("ClaireX.png"))
DavidimageX = ImageTk.PhotoImage(Image.open("DavidX.png"))
EricimageX = ImageTk.PhotoImage(Image.open("EricX.png"))
FransimageX = ImageTk.PhotoImage(Image.open("FransX.png"))
GeorgeimageX = ImageTk.PhotoImage(Image.open("GeorgeX.png"))
HermanimageX = ImageTk.PhotoImage(Image.open("HermanX.png"))
JoeimageX = ImageTk.PhotoImage(Image.open("JoeX.png"))
MariaimageX = ImageTk.PhotoImage(Image.open("MariaX.png"))
MaximageX = ImageTk.PhotoImage(Image.open("MaxX.png"))
PaulimageX = ImageTk.PhotoImage(Image.open("PaulX.png"))
PeterimageX = ImageTk.PhotoImage(Image.open("PeterX.png"))
PhilipimageX = ImageTk.PhotoImage(Image.open("PhilipX.png"))
RichardimageX = ImageTk.PhotoImage(Image.open("RichardX.png"))
RobertimageX = ImageTk.PhotoImage(Image.open("RobertX.png"))
SamimageX = ImageTk.PhotoImage(Image.open("SamX.png"))
SusanimageX = ImageTk.PhotoImage(Image.open("SusanX.png"))
TomimageX = ImageTk.PhotoImage(Image.open("TomX.png"))

Alex = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Aleximage1, command=lambda: click("Alex"))
Alfred = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Alfredimage1,
                command=lambda: click("Alfred"))
Anita = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Anitaimage1, command=lambda: click("Anita"))
Anne = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Anneimage1, command=lambda: click("Anne"))
Bernard = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Bernardimage1,
                 command=lambda: click("Bernard"))
Bill = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Billimage1, command=lambda: click("Bill"))
Charles = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Charlesimage1,
                 command=lambda: click("Charles"))
Claire = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Claireimage1,
                command=lambda: click("Claire"))
David = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Davidimage1, command=lambda: click("David"))
Eric = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Ericimage1, command=lambda: click("Eric"))
Frans = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Fransimage1, command=lambda: click("Frans"))
George = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Georgeimage1,
                command=lambda: click("George"))
Herman = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Hermanimage1,
                command=lambda: click("Herman"))
Joe = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Joeimage1, command=lambda: click("Joe"))
Maria = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Mariaimage1, command=lambda: click("Maria"))
Max = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Maximage1, command=lambda: click("Max"))
Paul = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Paulimage1, command=lambda: click("Paul"))
Peter = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Peterimage1, command=lambda: click("Peter"))
Philip = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Philipimage1,
                command=lambda: click("Philip"))
Richard = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Richardimage1,
                 command=lambda: click("Richard"))
Robert = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Robertimage1,
                command=lambda: click("Robert"))
Sam = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Samimage1, command=lambda: click("Sam"))
Susan = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Susanimage1, command=lambda: click("Susan"))
Tom = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=Tomimage1, command=lambda: click("Tom"))

M1 = person("Alex", Alex, Aleximage1, AleximageX, False, "black", False, True, False, True, False, False, False, 0, 0)
M2 = person("Alfred", Alfred, Alfredimage1, AlfredimageX, False, "red", False, True, False, True, False, False, True, 0,
            1)
M3 = person("Anita", Anita, Anitaimage1, AnitaimageX, False, "blonde", False, False, False, False, False, True, True, 0,
            2)
M4 = person("Anne", Anne, Anneimage1, AnneimageX, False, "black", False, False, False, False, False, False, False, 0, 3)
M5 = person("Bernard", Bernard, Bernardimage1, BernardimageX, True, "brown", False, True, False, False, False, False,
            False, 0, 4)
M6 = person("Bill", Bill, Billimage1, BillimageX, False, "red", False, True, True, False, True, True, False, 0, 5)
M7 = person("Charles", Charles, Charlesimage1, CharlesimageX, False, "blonde", False, True, False, True, False, False,
            False, 0, 6)
M8 = person("Claire", Claire, Claireimage1, ClaireimageX, True, "red", True, False, False, False, False, False, False,
            0, 7)
M9 = person("David", David, Davidimage1, DavidimageX, False, "blonde", False, True, False, False, True, False, False, 1,
            0)
M10 = person("Eric", Eric, Ericimage1, EricimageX, True, "blonde", False, True, False, False, False, False, False, 1, 1)
M11 = person("Frans", Frans, Fransimage1, FransimageX, False, "red", False, True, False, False, False, False, False, 1,
             2)
M12 = person("George", George, Georgeimage1, GeorgeimageX, True, "white", False, True, False, False, False, False,
             False, 1, 3)
M13 = person("Herman", Herman, Hermanimage1, HermanimageX, False, "red", False, True, True, False, False, False, False,
             1, 4)
M14 = person("Joe", Joe, Joeimage1, JoeimageX, False, "blonde", True, True, False, False, False, False, False, 1, 5)
M15 = person("Maria", Maria, Mariaimage1, MariaimageX, True, "brown", False, False, False, False, False, False, True, 1,
             6)
M16 = person("Max", Max, Maximage1, MaximageX, False, "black", False, True, False, True, False, False, False, 1, 7)
M17 = person("Paul", Paul, Paulimage1, PaulimageX, False, "white", True, True, False, False, False, False, False, 2, 0)
M18 = person("Peter", Peter, Peterimage1, PeterimageX, False, "white", False, True, False, False, False, False, False,
             2, 1)
M19 = person("Philip", Philip, Philipimage1, PhilipimageX, False, "black", False, True, False, False, True, True, False,
             2, 2)
M20 = person("Richard", Richard, Richardimage1, RichardimageX, False, "brown", False, True, True, True, True, False,
             False, 2, 3)
M21 = person("Robert", Robert, Robertimage1, RobertimageX, False, "brown", False, True, False, False, False, True,
             False, 2, 4)
M22 = person("Sam", Sam, Samimage1, SamimageX, False, "white", True, True, True, False, False, False, False, 2, 5)
M23 = person("Susan", Susan, Susanimage1, SusanimageX, False, "white", False, False, False, False, False, True, True, 2,
             6)
M24 = person("Tom", Tom, Tomimage1, TomimageX, False, "Black", True, True, True, False, False, False, False, 2, 7)

people = [M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24]
people2 = ['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Claire', 'David', 'Eric', 'Frans',
           'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan',
           'Tom']


choice1 = people[random.randint(0, 23)]  # computer picks person at random
print(choice1.name)

Alex.grid(row=M1.row, column=M1.column)
Alfred.grid(row=M2.row, column=M2.column)
Anita.grid(row=M3.row, column=M3.column)
Anne.grid(row=M4.row, column=M4.column)
Bernard.grid(row=M5.row, column=M5.column)
Bill.grid(row=M6.row, column=M6.column)
Charles.grid(row=M7.row, column=M7.column)
Claire.grid(row=M8.row, column=M8.column)
David.grid(row=M9.row, column=M9.column)
Eric.grid(row=M10.row, column=M10.column)
Frans.grid(row=M11.row, column=M11.column)
George.grid(row=M12.row, column=M12.column)
Herman.grid(row=M13.row, column=M13.column)
Joe.grid(row=M14.row, column=M14.column)
Maria.grid(row=M15.row, column=M15.column)
Max.grid(row=M16.row, column=M16.column)
Paul.grid(row=M17.row, column=M17.column)
Peter.grid(row=M18.row, column=M18.column)
Philip.grid(row=M19.row, column=M19.column)
Richard.grid(row=M20.row, column=M20.column)
Robert.grid(row=M21.row, column=M21.column)
Sam.grid(row=M22.row, column=M22.column)
Susan.grid(row=M23.row, column=M23.column)
Tom.grid(row=M24.row, column=M24.column)
questions = ["do they have a hat?",  "Are they wearing glasses?","Are they a woman?",
             "Are they bald?","Do they have a mustache?", "Do they have a beard?",
             "Do they have rosie-cheeks?", "Do they have long hair?", "Do they have red hair?",
             "Do they have blonde hair?", "Do they have brown hair?", "Do they have black hair?",
             "Do they have white hair?"]
questions2 = ["do they have a hat?", "Are they wearing glasses?","Are they a woman?",
             "Are they bald?","Do they have a mustache?", "Do they have a beard?",
             "Do they have rosie-cheeks?", "Do they have long hair?", "Do they have red hair?",
             "Do they have blonde hair?", "Do they have brown hair?", "Do they have black hair?",
             "Do they have white hair?"]
people3 = [M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24]
people4 = [M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24]

def machineguess():
    global questions
    global people3
    global people4
    for peeps in people4:
        print(peeps.name)
    quest =  random.randint(0,(len(questions)-1))
    blah = questions[quest]
    responce = messagebox.askyesno("Question", questions[quest])
    track = questions2.index(questions[quest])
    print(questions2[track])
    if responce == 1:
        if track == 0:
            for item in people3:
                if item.hat == False:
                    people4.remove(item)
        if track == 1:
            for item in people3:
                if item.glasses == False:
                    people4.remove(item)
        if track == 2:
            for item in people3:
                if item.male == True:
                    people4.remove(item)
        if track == 3:
            for item in people3:
                if item.bald == False:
                    people4.remove(item)
        if track == 4:
            for item in people3:
                if item.mustache == False:
                    people4.remove(item)
        if track == 5:
            for item in people3:
                if item.beard == False:
                    people4.remove(item)
        if track == 6:
            for item in people3:
                if item.rosie_cheeks == False:
                    people4.remove(item)
        if track == 7:
            for item in people3:
                if item.long_hair == False:
                    people4.remove(item)
        if track == 8:
            for item in people3:
                if item.hair_color != "red":
                    people4.remove(item)
                    if "Do they have blonde hair?" in questions:
                        questions.remove("Do they have blonde hair?")
                    if "Do they have brown hair?" in questions:
                        questions.remove("Do they have brown hair?")
                    if "Do they have black hair?" in questions:
                        questions.remove("Do they have black hair?")
                    if "Do they have white hair?" in questions:
                        questions.remove("Do they have white hair?")
        if track == 9:
            for item in people3:
                if item.hair_color != "blonde":
                    people4.remove(item)
                    if "Do they have white hair?" in questions:
                        questions.remove("Do they have white hair?")
                    if "Do they have brown hair?" in questions:
                        questions.remove("Do they have brown hair?")
                    if "Do they have black hair?" in questions:
                        questions.remove("Do they have black hair?")
                    if "Do they have red hair?" in questions:
                        questions.remove("Do they have red hair?")

        if track == 10:
            for item in people3:
                if item.hair_color != "brown":
                    people4.remove(item)
                    if "Do they have blonde hair?" in questions:
                        questions.remove("Do they have blonde hair?")
                    if "Do they have brown hair?" in questions:
                        questions.remove("Do they have white hair?")
                    if "Do they have white hair?" in questions:
                        questions.remove("Do they have black hair?")
                    if "Do they have red hair?" in questions:
                        questions.remove("Do they have red hair?")

        if track == 11:
            for item in people3:
                if item.hair_color != "black":
                    people4.remove(item)
                    if "Do they have blonde hair?" in questions:
                        questions.remove("Do they have blonde hair?")
                    if "Do they have brown hair?" in questions:
                        questions.remove("Do they have brown hair?")
                    if "Do they have white hair?" in questions:
                        questions.remove("Do they have white hair?")
                    if "Do they have red hair?" in questions:
                        questions.remove("Do they have red hair?")

        if track == 12:
            for item in people3:
                if item.hair_color != "white":
                    people4.remove(item)
                    if "Do they have blonde hair?" in questions:
                        questions.remove("Do they have blonde hair?")
                    if "Do they have brown hair?" in questions:
                        questions.remove("Do they have brown hair?")
                    if "Do they have black hair?" in questions:
                        questions.remove("Do they have black hair?")
                    if "Do they have red hair?" in questions:
                        questions.remove("Do they have red hair?")

    if responce == 0:
        if track == 0:
            for item in people3:
                if item.hat == True:
                    people4.remove(item)
        if track == 1:
            for item in people3:
                if item.glasses == True:
                    people4.remove(item)
        if track == 2:
            for item in people3:
                if item.male == False:
                    people4.remove(item)
        if track == 3:
            for item in people3:
                if item.bald == True:
                    people4.remove(item)
        if track == 4:
            for item in people3:
                if item.mustache == True:
                    people4.remove(item)
        if track == 5:
            for item in people3:
                if item.beard == True:
                    people4.remove(item)
        if track == 6:
            for item in people3:
                if item.rosie_cheeks == True:
                    people4.remove(item)
        if track == 7:
            for item in people3:
                if item.long_hair == True:
                    people4.remove(item)
        if track == 8:
            for item in people3:
                if item.hair_color == "red":
                    people4.remove(item)

        if track == 9:
            for item in people3:
                if item.hair_color == "blonde":
                    people4.remove(item)

        if track == 10:
            for item in people3:
                if item.hair_color == "brown":
                    people4.remove(item)

        if track ==11:
            for item in people3:
                if item.hair_color == "black":
                    people4.remove(item)

        if track == 12:
            for item in people3:
                if item.hair_color == "white":
                    people4.remove(item)

    print("removed")
    for item in people3:
        if item not in people4:
            print(item.name)

    people3 = people4

    print(blah)
    if responce == 1:
        print("yes")
    else:
        print("no")
    for peeps in people4:
        print(peeps.name)
    print("============================")
    questions.remove(blah)
    print(questions)
def click(name):
    global urchar
    global choice
    global yourcharcter
    if urchar == start:  # player CHARECTER SELECTION
        urchar = (people[people2.index(name)].image)
        choice.destroy()
        yourcharcter.destroy()
        choice = Label(choiceFrame, bg="yellow", padx=15, pady=15, image=urchar)
        yourcharcter = Label(choiceFrame, text="Your Person", font='Helvetica 15 bold', bg="yellow", fg="brown")
        choice.pack()
        yourcharcter.pack()
    else:
        if name == choice1.name:
            print("winner")
            for person in people:
                if person.name != name:
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    person.variable.grid(row=person.row, column=person.column)
            # winner() #add winner animation later
        else:
            (people[people2.index(name)].variable).destroy()
            people[people2.index(name)].variable = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y,
                                                          image=people[people2.index(name)].imageX, state=DISABLED)
            (people[people2.index(name)].variable).grid(row=(people[people2.index(name)].row),
                                                        column=(people[people2.index(name)].column))
            machineguess()

def hat():
    global hat
    hat.destroy()
    hat = Button(questionFrame, bg="tan", fg="brown", text="Do they have a hat?", state=DISABLED)
    hat.grid(row=2, column=0)
    if choice1.hat == True:
        for person in people:
            if person.hat == False:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    elif choice1.hat == False:
        for person in people:
            if person.hat == True:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    machineguess()

def glasses():
    global glasses
    glasses.destroy()
    glasses = Button(questionFrame, bg="tan", fg="brown", text="Do they have glasses?", state=DISABLED)
    glasses.grid(row=0, column=1)
    if choice1.glasses == True:
        for person in people:
            if person.glasses == False:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    elif choice1.glasses == False:
        for person in people:
            if person.glasses == True:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    machineguess()

def sex():
    global man
    global woman
    man.destroy()
    woman.destroy()
    man = Button(questionFrame, bg="tan", fg="brown", text="Are they a man?    ", state=DISABLED)
    woman = Button(questionFrame, bg="tan", fg="brown", text="Are they a woman?  ", state=DISABLED)
    man.grid(row=0, column=0)
    woman.grid(row=1, column=0)
    if choice1.male == True:
        for person in people:
            if person.male == False:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    elif choice1.male == False:
        for person in people:
            if person.male == True:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    machineguess()

def bald():
    global bald
    bald.destroy()
    bald = Button(questionFrame, bg="tan", fg="brown", text="Are they bald?", state=DISABLED)
    bald.grid(row=2, column=1)
    if choice1.bald == True:
        for person in people:
            if person.bald == False:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    elif choice1.bald == False:
        for person in people:
            if person.bald == True:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    machineguess()

def beard():
    global beard
    beard.destroy()
    beard = Button(questionFrame, bg="tan", fg="brown", text="Do they have a beard?", state=DISABLED)
    beard.grid(row=3, column=1)
    if choice1.beard == True:
        for person in people:
            if person.beard == False:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    elif choice1.beard == False:
        for person in people:
            if person.beard == True:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    machineguess()

def cheeks():
    global rosiecheeks
    rosiecheeks.destroy()
    rosiecheeks = Button(questionFrame, bg="tan", fg="brown", text="Do they have rosie cheeks?", state=DISABLED)
    rosiecheeks.grid(row=1, column=1)
    if choice1.rosie_cheeks == True:
        for person in people:
            if person.rosie_cheeks == False:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    elif choice1.rosie_cheeks == False:
        for person in people:
            if person.rosie_cheeks == True:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    machineguess()

def mustache():
    global mustache
    mustache.destroy()
    mustache = Button(questionFrame2, bg="tan", fg="brown", text="Do they have a mustache?", state=DISABLED)
    mustache.grid(row=0, column=0)
    if choice1.mustache == True:
        for person in people:
            if person.mustache == False:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    elif choice1.mustache == False:
        for person in people:
            if person.mustache == True:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    machineguess()

def longhair():
    global longhair
    longhair.destroy()
    longhair = Button(questionFrame2, bg="tan", fg="brown", text="Do they have long hair?", state=DISABLED)
    longhair.grid(row=1, column=0)
    if choice1.long_hair == True:
        for person in people:
            if person.long_hair == False:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    elif choice1.long_hair == False:
        for person in people:
            if person.long_hair == True:
                (person.variable).destroy()
                person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                         state=DISABLED)
                (person.variable).grid(row=person.row, column=person.column)
    machineguess()

def hair(color):
    global blonde
    global black
    global red
    global brown
    global white
    if color == "blonde":
        blonde.destroy()
        blonde = Button(questionFrame2, bg="tan", fg="brown", text="Do they have blonde hair? ", state=DISABLED)
        blonde.grid(row=2, column=0)
        if choice1.hair_color == "blonde":
            for person in people:
                if person.hair_color != "blonde":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
        elif choice1.hair_color != "blonde":
            for person in people:
                if person.hair_color == "blonde":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)

    if color == "black":
        black.destroy()
        black = Button(questionFrame2, bg="tan", fg="brown", text="Do they have black hair?", state=DISABLED)
        black.grid(row=3, column=0)
        if choice1.hair_color == "black":
            for person in people:
                if person.hair_color != "black":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
        elif choice1.hair_color != "black":
            for person in people:
                if person.hair_color == "black":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
    if color == "red":
        red.destroy()
        red = Button(questionFrame2, bg="tan", fg="brown", text="Do they have red hair? ", state=DISABLED)
        red.grid(row=0, column=1)
        if choice1.hair_color == "red":
            for person in people:
                if person.hair_color != "red":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
        elif choice1.hair_color != "red":
            for person in people:
                if person.hair_color == "red":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
    if color == "brown":
        brown.destroy()
        brown = Button(questionFrame2, bg="tan", fg="brown", text="Do they have brown hair? ", state=DISABLED)
        brown.grid(row=1, column=1)
        if choice1.hair_color == "brown":
            for person in people:
                if person.hair_color != "brown":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
        elif choice1.hair_color != "brown":
            for person in people:
                if person.hair_color == "brown":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
    if color == "white":
        white.destroy()
        white = Button(questionFrame2, bg="tan", fg="brown", text="Do they have white hair?", state=DISABLED)
        white.grid(row=2, column=1)
        if choice1.hair_color == "white":
            for person in people:
                if person.hair_color != "white":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
        elif choice1.hair_color != "white":
            for person in people:
                if person.hair_color == "white":
                    (person.variable).destroy()
                    person.variable = Button(mainFrame, bg="yellow", borderwidth=0, padx=x, pady=y, image=person.imageX,
                                             state=DISABLED)
                    (person.variable).grid(row=person.row, column=person.column)
    machineguess()

hat = Button(questionFrame, bg="tan", fg="brown", text="Do they have a hat?", command=hat)
glasses = Button(questionFrame, bg="tan", fg="brown", text="Do they have glasses?", command=glasses)
man = Button(questionFrame, bg="tan", fg="brown", text="Are they a man?    ", command=sex)
woman = Button(questionFrame, bg="tan", fg="brown", text="Are they a woman?  ", command=sex)
bald = Button(questionFrame, bg="tan", fg="brown", text="Are they bald?", command=bald)
beard = Button(questionFrame, bg="tan", fg="brown", text="Do they have a beard?", command=beard)
rosiecheeks = Button(questionFrame, bg="tan", fg="brown", text="Do they have rosie cheeks?", command=cheeks)

mustache = Button(questionFrame2, bg="tan", fg="brown", text="Do they have a mustache?", command=mustache)
longhair = Button(questionFrame2, bg="tan", fg="brown", text="Do they have long hair?", command=longhair)
blonde = Button(questionFrame2, bg="tan", fg="brown", text="Do they have blonde hair? ", command=lambda: hair("blonde"))
black = Button(questionFrame2, bg="tan", fg="brown", text="Do they have black hair?", command=lambda: hair("black"))
red = Button(questionFrame2, bg="tan", fg="brown", text="Do they have red hair? ", command=lambda: hair("red"))
brown = Button(questionFrame2, bg="tan", fg="brown", text="Do they have brown hair? ", command=lambda: hair("brown"))
white = Button(questionFrame2, bg="tan", fg="brown", text="Do they have white hair?", command=lambda: hair("white"))

man.grid(row=0, column=0)
woman.grid(row=1, column=0)
hat.grid(row=2, column=0)
glasses.grid(row=0, column=1)
rosiecheeks.grid(row=1, column=1)
bald.grid(row=2, column=1)
beard.grid(row=3, column=1)

mustache.grid(row=0, column=0)
longhair.grid(row=1, column=0)
blonde.grid(row=2, column=0)
black.grid(row=3, column=0)
red.grid(row=0, column=1)
brown.grid(row=1, column=1)
white.grid(row=2, column=1)

root.mainloop()
