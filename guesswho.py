from tkinter import *
from PIL import Image, ImageTk
from person import person

root = Tk()
root.title("Guess Who!")
root.bg="yellow"
topFrame=Frame(root)
title=Label(topFrame,text="Guess Who!",font='Helvetica 22 bold',width="38",fg="brown",bg="yellow").pack()
topFrame.grid(row=0,column=0,columnspan=3)

x=15
y=15

start=ImageTk.PhotoImage(Image.open("Start.png"))
mainFrame=Frame(root,bg="yellow",width="50",padx=42,pady=3)
questionFrame=Frame(root,bg="yellow",padx=1,pady=31)
questionFrame2=Frame(root,bg="yellow",padx=1,pady=31)
choiceFrame=Frame(root,bg="yellow",pady=3)
urchar= start
choice=Label(choiceFrame,bg="yellow",padx=15,pady=15,image=urchar)
yourcharcter = Label(choiceFrame,text ="Your Person",font='Helvetica 15 bold',bg="yellow",fg="brown")
choice.pack()
yourcharcter.pack()
mainFrame.grid(row=1,column=0,columnspan=3)
questionFrame.grid(row=2,column=0)
choiceFrame.grid(row=2,column=1)
questionFrame2.grid(row=2,column=2)


Aleximage1=ImageTk.PhotoImage(Image.open("Alex.png"))
Alfredimage1=ImageTk.PhotoImage(Image.open("Alfred.png"))
Anitaimage1=ImageTk.PhotoImage(Image.open("Anita.png"))
Anneimage1=ImageTk.PhotoImage(Image.open("Anne.png"))
Bernardimage1=ImageTk.PhotoImage(Image.open("Bernard.png"))
Billimage1=ImageTk.PhotoImage(Image.open("Bill.png"))
Charlesimage1=ImageTk.PhotoImage(Image.open("Charles.png"))
Claireimage1=ImageTk.PhotoImage(Image.open("Claire.png"))
Davidimage1=ImageTk.PhotoImage(Image.open("David.png"))
Ericimage1=ImageTk.PhotoImage(Image.open("Eric.png"))
Fransimage1=ImageTk.PhotoImage(Image.open("Frans.png"))
Georgeimage1=ImageTk.PhotoImage(Image.open("George.png"))
Hermanimage1=ImageTk.PhotoImage(Image.open("Herman.png"))
Joeimage1=ImageTk.PhotoImage(Image.open("Joe.png"))
Mariaimage1=ImageTk.PhotoImage(Image.open("Maria.png"))
Maximage1=ImageTk.PhotoImage(Image.open("Max.png"))
Paulimage1=ImageTk.PhotoImage(Image.open("Paul.png"))
Peterimage1=ImageTk.PhotoImage(Image.open("Peter.png"))
Philipimage1=ImageTk.PhotoImage(Image.open("Philip.png"))
Richardimage1=ImageTk.PhotoImage(Image.open("Richard.png"))
Robertimage1=ImageTk.PhotoImage(Image.open("Robert.png"))
Samimage1=ImageTk.PhotoImage(Image.open("Sam.png"))
Susanimage1=ImageTk.PhotoImage(Image.open("Susan.png"))
Tomimage1=ImageTk.PhotoImage(Image.open("Tom.png"))

AleximageX=ImageTk.PhotoImage(Image.open("AlexX.png"))
AlfredimageX=ImageTk.PhotoImage(Image.open("AlfredX.png"))
AnitaimageX=ImageTk.PhotoImage(Image.open("AnitaX.png"))
AnneimageX=ImageTk.PhotoImage(Image.open("AnneX.png"))
BernardimageX=ImageTk.PhotoImage(Image.open("BernardX.png"))
BillimageX=ImageTk.PhotoImage(Image.open("BillX.png"))
CharlesimageX=ImageTk.PhotoImage(Image.open("CharlesX.png"))
ClaireimageX=ImageTk.PhotoImage(Image.open("ClaireX.png"))
DavidimageX=ImageTk.PhotoImage(Image.open("DavidX.png"))
EricimageX=ImageTk.PhotoImage(Image.open("EricX.png"))
FransimageX=ImageTk.PhotoImage(Image.open("FransX.png"))
GeorgeimageX=ImageTk.PhotoImage(Image.open("GeorgeX.png"))
HermanimageX=ImageTk.PhotoImage(Image.open("HermanX.png"))
JoeimageX=ImageTk.PhotoImage(Image.open("JoeX.png"))
MariaimageX=ImageTk.PhotoImage(Image.open("MariaX.png"))
MaximageX=ImageTk.PhotoImage(Image.open("MaxX.png"))
PaulimageX=ImageTk.PhotoImage(Image.open("PaulX.png"))
PeterimageX=ImageTk.PhotoImage(Image.open("PeterX.png"))
PhilipimageX=ImageTk.PhotoImage(Image.open("PhilipX.png"))
RichardimageX=ImageTk.PhotoImage(Image.open("RichardX.png"))
RobertimageX=ImageTk.PhotoImage(Image.open("RobertX.png"))
SamimageX=ImageTk.PhotoImage(Image.open("SamX.png"))
SusanimageX=ImageTk.PhotoImage(Image.open("SusanX.png"))
TomimageX=ImageTk.PhotoImage(Image.open("TomX.png"))



Alex = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Aleximage1,command= lambda: click("Alex"))
Alfred = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Alfredimage1,command=lambda: click("Alfred"))
Anita = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Anitaimage1,command=lambda: click("Anita"))
Anne = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Anneimage1,command=lambda: click("Anne"))
Bernard = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Bernardimage1,command=lambda: click("Bernard"))
Bill = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Billimage1,command=lambda: click("Bill"))
Charles = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Charlesimage1,command=lambda: click("Charles"))
Claire = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Claireimage1,command=lambda: click("Claire"))
David = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Davidimage1,command=lambda: click("David"))
Eric = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Ericimage1,command=lambda: click("Eric"))
Frans = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Fransimage1,command=lambda: click("Frans"))
George = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Georgeimage1,command=lambda: click("George"))
Herman = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Hermanimage1,command=lambda: click("Herman"))
Joe = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Joeimage1,command=lambda: click("Joe"))
Maria = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Mariaimage1,command=lambda: click("Maria"))
Max = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Maximage1,command=lambda: click("Max"))
Paul = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Paulimage1,command=lambda: click("Paul"))
Peter = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Peterimage1,command=lambda: click("Peter"))
Philip = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Philipimage1,command=lambda: click("Philip"))
Richard = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Richardimage1,command=lambda: click("Richard"))
Robert = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Robertimage1,command=lambda: click("Robert"))
Sam = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Samimage1,command=lambda: click("Sam"))
Susan = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Susanimage1,command=lambda: click("Susan"))
Tom = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Tomimage1,command=lambda: click("Tom"))


M1 = person("Alex", Alex, Aleximage1, AleximageX, False, "black", False, True, False, True, False, False, False,0,0)
M2 = person("Alfred", Alfred, Alfredimage1,AlfredimageX, False, "red", False, True, False, True, False, False, True,0,1)
M3 = person("Anita", Anita, Anitaimage1,AnitaimageX, False, "blonde", False, False, False, False, False, True, True,0,2)
M4 = person("Anne",Anne,Anneimage1,AnneimageX, False, "black", False, False, False, False, False, False, False,0,3)
M5 = person("Bernard",Bernard, Bernardimage1,BernardimageX, True, "brown", False, True, False, False, False, False, False,0,4)
M6 = person("Bill", Bill, Billimage1, BernardimageX, False, "red", False, True, True, False, True, True, False,0,5)
M7 = person("Charles",Charles, Charlesimage1, CharlesimageX, False, "blonde", False, True, False, True, False, False, False,0,6)
M8 = person("Claire", Claire, Claireimage1, ClaireimageX,True, "red", True, False, False, False, False, False, False,0,7)
M9 = person("David",David, Davidimage1, DavidimageX, False, "blonde", False, True, False, False, True, False, False,1,0)
M10 = person("Eric",Eric, Ericimage1, EricimageX, True, "blonde", False, True, False, False, False, False, False,1,1)
M11 = person("Frans",Frans, Fransimage1, FransimageX, False, "red", False, True, False, False, False, False, False,1,2)
M12 = person("George",George, Georgeimage1, GeorgeimageX, True, "white", False, True, False, False, False, False, False,1,3)
M13 = person("Herman",Herman,Hermanimage1,HermanimageX, False, "red", False, True, True, False, False, False, False,1,4)
M14 = person("Joe", Joe, Joeimage1, JoeimageX, False, "blonde", True, True, False, False, False, False, False,1,5)
M15 = person("Maria",Maria, Mariaimage1, MariaimageX, True, "brown", False, False, False, False, False, False, True,1,6)
M16 = person("Max",Max, Maximage1, MaximageX, False, "black", False, True, False, True, False, False, False,1,7)
M17 = person("Paul", Paul, Paulimage1, PaulimageX, False, "white", True, True, False, False, False, False, False,2,0)
M18 = person("Peter", Peter, Peterimage1, PeterimageX, False, "white", False, True, False, False, False, False, False,2,1)
M19 = person("Philip", Philip, Philipimage1, PhilipimageX, False, "black", False, True, False, False, True, True, False,2,2)
M20 = person("Richard", Richard, Richardimage1, RichardimageX, False, "brown", False, True, True, True, True, False, False,2,3)
M21 = person("Robert",Robert, Robertimage1, RobertimageX, False, "brown", False, True, False, False, False, True, False,2,4)
M22 = person("Sam",Sam, Samimage1,SamimageX, False, "white", True, True, True, False, False, False, False,2,5)
M23 = person("Susan",Susan,Susanimage1,SusanimageX, False, "white", False, False, False, False, False, True, True,2,6)
M24 = person("Tom",Tom,Tomimage1,TomimageX, False, "Black", True, True, True, False, False, False, False,2,7)


people=[M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12,M13,M14,M15,M16,M17,M18,M19,M20,M21,M22,M23,M24]
people2=['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Claire', 'David', 'Eric', 'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan', 'Tom']
import random
choice1 = people[random.randint(0, 23)] #computer picks person at random
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


def guess(name):
    global Aleximage
    global Alfredimage
    global Anitaimage
    global Anneimage
    global Bernardimage
    global Billimage
    global Charlesimage
    global Claireimage
    global Davidimage
    global Ericimage
    global Fransimage
    global Georgeimage
    global Hermanimage
    global Joeimage
    global Mariaimage
    global Maximage
    global Paulimage
    global Peterimage
    global Philipimage
    global Richardimage
    global Robertimage
    global Samimage
    global Susanimage
    global Tomimage
    global Alex
    global Alfred
    global Anita
    global Anne
    global Bernard
    global Bill
    global Charles
    global Claire
    global David
    global Eric
    global Frans
    global George
    global Herman
    global Joe
    global Maria
    global Max
    global Paul
    global Peter
    global Philip
    global Richard
    global Robert
    global Sam
    global Susan
    global Tom

    guess = "none"
    if name == Aleximage:
        guess = "Alex"
        Aleximage = AleximageX
        Alex.destroy()
        Alex = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Aleximage,
                      command=lambda: click(Aleximage), state=DISABLED)
    if name == Alfredimage:
        guess = "Alfred"
        Alfredimage = AlfredimageX
        Alfred.destroy()
        Alfred = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Alfredimage,
                        command=lambda: click(Alfredimage), state=DISABLED)
    if name == Anitaimage:
        guess = "Anita"
        Anitaimage = AnitaimageX
        Anita.destroy()
        Anita = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Anitaimage,
                       command=lambda: click(Anitaimage), state=DISABLED)
    if name == Anneimage:
        guess = "Anne"
        Anneimage = AnneimageX
        Anne.destroy()
        Anne = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Anneimage,
                      command=lambda: click(Anneimage), state=DISABLED)

    if name == Bernardimage:
        guess = "Bernard"
        Bernardimage = BernardimageX
        Bernard.destroy()
        Bernard = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Bernardimage,
                     command=lambda: click(Bernardimage), state=DISABLED)
    if name == Billimage:
        guess = "Bill"
        Billimage = BillimageX
        Bill.destroy()
        Bill = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Billimage,
                      command=lambda: click(Billimage), state=DISABLED)
    if name == Charlesimage:
        guess = "Charles"
        Charlesimage = CharlesimageX
        Charles.destroy()
        Charles = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Charlesimage,
                         command=lambda: click(Charlesimage), state=DISABLED)

    if name == Claireimage:
        guess = "Claire"
        Claireimage = ClaireimageX
        Claire.destroy()
        Claire = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Claireimage,
                        command=lambda: click(Claireimage), state=DISABLED)

    if name == Davidimage:
        guess = "David"
        Davidimage = DavidimageX
        David.destroy()
        David = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Davidimage,
                       command=lambda: click(Davidimage), state=DISABLED)

    if name == Ericimage:
        guess = "Eric"
        Ericimage = EricimageX
        Eric.destroy()
        Eric = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Ericimage,
                      command=lambda: click(Ericimage), state=DISABLED)

    if name == Fransimage:
        guess = "Frans"
        Fransimage = FransimageX
        Frans.destroy()
        Frans = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Fransimage,
                       command=lambda: click(Fransimage), state=DISABLED)

    if name == Georgeimage:
        guess = "George"
        Georgeimage = GeorgeimageX
        George.destroy()
        George = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Georgeimage,
                        command=lambda: click(Georgeimage), state=DISABLED)

    if name == Hermanimage:
        guess = "Herman"
        Hermanimage = HermanimageX
        Herman.destroy()
        Herman = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Hermanimage,
                        command=lambda: click(Hermanimage), state=DISABLED)

    if name == Joeimage:
        guess = "Joe"
        Joeimage = JoeimageX
        Joe.destroy()
        Joe = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Joeimage,
                     command=lambda: click(Joeimage), state=DISABLED)

    if name == Mariaimage:
        guess = "Maria"
        Mariaimage = MariaimageX
        Maria.destroy()
        Maria = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Mariaimage,
                       command=lambda: click(Mariaimage), state=DISABLED)

    if name == Maximage:
        guess = "Max"
        Maximage = MaximageX
        Max.destroy()
        Max = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Maximage,
                     command=lambda: click(Maximage), state=DISABLED)

    if name == Paulimage:
        guess = "Paul"
        Paulimage = PaulimageX
        Paul.destroy()
        Paul = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Paulimage,
                      command=lambda: click(Paulimage), state=DISABLED)

    if name == Peterimage:
        guess = "Peter"
        Peterimage = PeterimageX
        Peter.destroy()
        Peter = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Peterimage,
                       command=lambda: click(Peterimage), state=DISABLED)

    if name == Philipimage:
        guess = "Philip"
        Philipimage =PhilipimageX
        Philip.destroy()
        Philip = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Philipimage,
                        command=lambda: click(Philipimage), state=DISABLED)

    if name == Richardimage:
        guess = "Richard"
        Richardimage = RichardimageX
        Richard.destroy()
        Richard = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Richardimage,
                         command=lambda: click(Richardimage), state=DISABLED)

    if name == Robertimage:
        guess = "Robert"
        Robertimage = RobertimageX
        Robert.destroy()
        Robert = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Robertimage,
                        command=lambda: click(Robertimage), state=DISABLED)

    if name == Samimage:
        guess = "Sam"
        Samimage = SamimageX
        Sam.destroy()
        Sam = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Samimage,
                     command=lambda: click(Samimage), state=DISABLED)

    if name == Susanimage:
        guess = "Susan"
        Susanimage = SusanimageX
        Susan.destroy()
        Susan = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Susanimage,
                       command=lambda: click(Susanimage), state=DISABLED)

    if name == Tomimage:
        guess = "Tom"
        Tomimage = TomimageX
        Tom.destroy()
        Tom = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=Tomimage,
                     command=lambda: click(Tomimage), state=DISABLED)



    Alex.grid(row=0, column=0)
    Alfred.grid(row=0, column=1)
    Anita.grid(row=0, column=2)
    Anne.grid(row=0, column=3)
    Bernard.grid(row=0, column=4)
    Bill.grid(row=0, column=5)
    Charles.grid(row=0, column=6)
    Claire.grid(row=0, column=7)
    David.grid(row=1, column=0)
    Eric.grid(row=1, column=1)
    Frans.grid(row=1, column=2)
    George.grid(row=1, column=3)
    Herman.grid(row=1, column=4)
    Joe.grid(row=1, column=5)
    Maria.grid(row=1, column=6)
    Max.grid(row=1, column=7)
    Paul.grid(row=2, column=0)
    Peter.grid(row=2, column=1)
    Philip.grid(row=2, column=2)
    Richard.grid(row=2, column=3)
    Robert.grid(row=2, column=4)
    Sam.grid(row=2, column=5)
    Susan.grid(row=2, column=6)
    Tom.grid(row=2, column=7)
    if guess == choice1.name:
        print("winner")
        reset()
    return(guess)


def click(name):
    global urchar
    global choice
    global yourcharcter
    if urchar == start: #CHARECTER SELECTION
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
            #winner() #add winner animation later
        else:
            (people[people2.index(name)].variable).destroy()
            people[people2.index(name)].variable = Button(mainFrame, bg="gray", borderwidth=0, padx=x, pady=y, image=people[people2.index(name)].imageX, state=DISABLED)
            (people[people2.index(name)].variable).grid(row=(people[people2.index(name)].row),column=(people[people2.index(name)].column))



def hat():
    global hat
    hat.destroy()
    hat = Button(questionFrame, bg="tan", fg="brown", text="Do they have a hat?",state = DISABLED)
    hat.grid(row=2, column=0)
    if choice1.hat == True:
        for person in people:
            if person. hat == False:
                (person.variable).destroy()
                person.variable=Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=person.imageX,state=DISABLED)
                (person.variable).grid(row=person.row,column=person.column)
def glasses():
    global glasses
    glasses.destroy()
    glasses = Button(questionFrame, bg="tan", fg="brown", text="Do they have glasses?",state = DISABLED)
    glasses.grid(row=0, column=1)
def sex():
    global man
    global woman
    man.destroy()
    woman.destroy()
    man = Button(questionFrame, bg="tan", fg="brown", text="Are they a man?    ",state = DISABLED)
    woman = Button(questionFrame, bg="tan", fg="brown", text="Are they a woman?  ",state = DISABLED)
    man.grid(row=0, column=0)
    woman.grid(row=1, column=0)
def bald():
    global bald
    bald.destroy()
    bald = Button(questionFrame, bg="tan", fg="brown", text="Are they bald?",state = DISABLED)
    bald.grid(row=2, column=1)
def beard():
    global beard
    beard.destroy()
    beard = Button(questionFrame, bg="tan", fg="brown", text="Do they have a beard?",state = DISABLED)
    beard.grid(row=3, column=1)
def cheeks():
    global rosiecheeks
    rosiecheeks.destroy()
    rosiecheeks=Button(questionFrame, bg="tan",fg="brown",text="Do they have rosie cheeks?",state = DISABLED)
    rosiecheeks.grid(row=1, column=1)
def mustache():
    global mustache
    mustache.destroy()
    mustache=Button(questionFrame2,bg="tan",fg="brown", text="Do they have a mustache?",state = DISABLED)
    mustache.grid(row=0, column=0)
def longhair():
    global longhair
    longhair.destroy()
    longhair=Button(questionFrame2,bg="tan",fg="brown", text="Do they have long hair?",state = DISABLED)
    longhair.grid(row=1, column=0)
def hair(color):
    global blonde
    global black
    global red
    global brown
    global white
    if color == "blonde":
        blonde.destroy()
        blonde = Button(questionFrame2, bg="tan", fg="brown", text="Do they have blonde hair? ",state = DISABLED)
        blonde.grid(row=2, column=0)
    if color == "black":
        black.destroy()
        black = Button(questionFrame2, bg="tan", fg="brown", text="Do they have black hair?",state = DISABLED )
        black.grid(row=3, column=0)
    if color == "red":
        red.destroy()
        red = Button(questionFrame2, bg="tan", fg="brown", text="Do they have red hair? ",state = DISABLED)
        red.grid(row=0, column=1)
    if color == "brown":
        brown.destroy()
        brown = Button(questionFrame2, bg="tan", fg="brown", text="Do they have brown hair? ",state = DISABLED)
        brown.grid(row=1, column=1)
    if color == "white":
        white.destroy()
        white = Button(questionFrame2, bg="tan", fg="brown", text="Do they have white hair?",state = DISABLED)
        white.grid(row=2, column=1)
hat=Button(questionFrame,bg="tan",fg="brown", text="Do they have a hat?",command=hat)
glasses=Button(questionFrame,bg="tan",fg="brown", text="Do they have glasses?",command=glasses)
man=Button(questionFrame,bg="tan",fg="brown",   text="Are they a man?    ",command=sex)
woman=Button(questionFrame,bg="tan",fg="brown", text="Are they a woman?  ",command=sex)
bald=Button(questionFrame,bg="tan",fg="brown", text="Are they bald?",command=bald)
beard=Button(questionFrame,bg="tan",fg="brown", text="Do they have a beard?",command=beard)
rosiecheeks=Button(questionFrame, bg="tan",fg="brown",text="Do they have rosie cheeks?",command=cheeks)

mustache=Button(questionFrame2,bg="tan",fg="brown", text="Do they have a mustache?",command=mustache)
longhair=Button(questionFrame2,bg="tan",fg="brown", text="Do they have long hair?",command=longhair)
blonde=Button(questionFrame2,bg="tan",fg="brown", text="Do they have blonde hair? ",command=lambda:hair("blonde"))
black=Button(questionFrame2,bg="tan",fg="brown", text="Do they have black hair?",command=lambda:hair("black"))
red =Button(questionFrame2,bg="tan",fg="brown", text="Do they have red hair? ",command=lambda:hair("red"))
brown=Button(questionFrame2,bg="tan",fg="brown", text="Do they have brown hair? ",command=lambda:hair("brown"))
white=Button(questionFrame2,bg="tan",fg="brown", text="Do they have white hair?",command=lambda:hair("white"))

man.grid(row=0,column=0)
woman.grid(row=1,column=0)
hat.grid(row=2,column=0)
glasses.grid(row=0,column=1)
rosiecheeks.grid(row=1,column=1)
bald.grid(row=2,column=1)
beard.grid(row=3,column=1)

mustache.grid(row=0,column=0)
longhair.grid(row=1,column=0)
blonde.grid(row=2,column=0)
black.grid(row=3,column=0)
red.grid(row=0,column=1)
brown.grid(row=1,column=1)
white.grid(row=2,column=1)


root.mainloop()
