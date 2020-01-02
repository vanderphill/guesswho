from tkinter import *
from PIL import Image, ImageTk
x=15
y=15
root = Tk()
root.title("Guess Who!")
root.bg="yellow"
topFrame=Frame(root)
title=Label(topFrame,text="Guess Who!",font='Helvetica 22 bold',width="38",fg="brown",bg="yellow").pack()
topFrame.grid(row=0,column=0,columnspan=3)


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


Aleximage = Aleximage1
Alfredimage = Alfredimage1
Anitaimage = Anitaimage1
Anneimage = Anneimage1
Bernardimage = Bernardimage1
Billimage = Billimage1
Charlesimage = Charlesimage1
Claireimage = Claireimage1
Davidimage = Davidimage1
Ericimage = Ericimage1
Fransimage = Fransimage1
Georgeimage = Georgeimage1
Hermanimage = Hermanimage1
Joeimage = Joeimage1
Mariaimage = Mariaimage1
Maximage = Maximage1
Paulimage = Paulimage1
Peterimage = Peterimage1
Philipimage = Philipimage1
Richardimage = Richardimage1
Robertimage = Robertimage1
Samimage = Samimage1
Susanimage = Susanimage1
Tomimage = Tomimage1







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
    return(guess)


def click(name):
    global urchar
    global choice
    global yourcharcter
    if urchar == start: #CHARECTER SELECTION
        urchar = name
        choice.destroy()
        yourcharcter.destroy()
        choice = Label(choiceFrame, bg="yellow", padx=15, pady=15, image=urchar)
        yourcharcter = Label(choiceFrame, text="Your Person", font='Helvetica 15 bold', bg="yellow", fg="brown")
        choice.pack()
        yourcharcter.pack()
    else:
        guess(name)
Alex = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Aleximage,command= lambda: click(Aleximage))
Alfred = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Alfredimage,command=lambda: click(Alfredimage))
Anita = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Anitaimage,command=lambda: click(Anitaimage))
Anne = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Anneimage,command=lambda: click(Anneimage))
Bernard = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Bernardimage,command=lambda: click(Bernardimage))
Bill = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Billimage,command=lambda: click(Billimage))
Charles = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Charlesimage,command=lambda: click(Charlesimage))
Claire = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Claireimage,command=lambda: click(Claireimage))
David = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Davidimage,command=lambda: click(Davidimage))
Eric = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Ericimage,command=lambda: click(Ericimage))
Frans = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Fransimage,command=lambda: click(Fransimage))
George = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Georgeimage,command=lambda: click(Georgeimage))
Herman = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Hermanimage,command=lambda: click(Hermanimage))
Joe = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Joeimage,command=lambda: click(Joeimage))
Maria = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Mariaimage,command=lambda: click(Mariaimage))
Max = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Maximage,command=lambda: click(Maximage))
Paul = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Paulimage,command=lambda: click(Paulimage))
Peter = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Peterimage,command=lambda: click(Peterimage))
Philip = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Philipimage,command=lambda: click(Philipimage))
Richard = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Richardimage,command=lambda: click(Richardimage))
Robert = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Robertimage,command=lambda: click(Robertimage))
Sam = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Samimage,command=lambda: click(Samimage))
Susan = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Susanimage,command=lambda: click(Susanimage))
Tom = Button(mainFrame,bg="yellow",borderwidth=0,padx=x,pady=y,image=Tomimage,command=lambda: click(Tomimage))
Alex.grid(row=0,column=0)
Alfred.grid(row=0,column=1)
Anita.grid(row=0,column=2)
Anne.grid(row=0,column=3)
Bernard.grid(row=0,column=4)
Bill.grid(row=0,column=5)
Charles.grid(row=0,column=6)
Claire.grid(row=0,column=7)
David.grid(row=1,column=0)
Eric.grid(row=1,column=1)
Frans.grid(row=1,column=2)
George.grid(row=1,column=3)
Herman.grid(row=1,column=4)
Joe.grid(row=1,column=5)
Maria.grid(row=1,column=6)
Max.grid(row=1,column=7)
Paul.grid(row=2,column=0)
Peter.grid(row=2,column=1)
Philip.grid(row=2,column=2)
Richard.grid(row=2,column=3)
Robert.grid(row=2,column=4)
Sam.grid(row=2,column=5)
Susan.grid(row=2,column=6)
Tom.grid(row=2,column=7)
def hat()
    global hat
    hat.destroy()
    hat = Button(questionFrame, bg="tan", fg="brown", text="Do they have a hat?",state = DISABLED)
def glasses()
    global glasses
    glasses.destroy()
    glasses = Button(questionFrame, bg="tan", fg="brown", text="Do they have glasses?",state = DISABLED)
def sex()
    global man
    global woman
    man.destroy()
    woman.destroy()
    man = Button(questionFrame, bg="tan", fg="brown", text="Are they a man?    ",state = DISABLED)
    woman = Button(questionFrame, bg="tan", fg="brown", text="Are they a woman?  ",state = DISABLED)
def bald()
    global bald
    bald.destroy()
    bald = Button(questionFrame, bg="tan", fg="brown", text="Are they bald?",state = DISABLED)
def beard()
    global beard
    beard.destroy()
    beard = Button(questionFrame, bg="tan", fg="brown", text="Do they have a beard?",state = DISABLED)
def cheeks()
    global rosiecheeks
    rosiecheeks.destroy()
    rosiecheeks=Button(questionFrame, bg="tan",fg="brown",text="Do they have rosie cheeks?",state = DISABLED)
def mustache()
    global mustache
    mustache.destroy()
    mustache=Button(questionFrame2,bg="tan",fg="brown", text="Do they have a mustache?",state = DISABLED)
def longhair()
    global longhair
    longhair.destroy()
    longhair=Button(questionFrame2,bg="tan",fg="brown", text="Do they have long hair?",state = DISABLED)
def hair(color)
    global blonde
    global black
    global red
    global brown
    global white
    if color == "blonde":
        blonde.destroy()
        blonde = Button(questionFrame2, bg="tan", fg="brown", text="Do they have blonde hair? ",state = DISABLED)

    if color == "black":
        black.destroy()
        black = Button(questionFrame2, bg="tan", fg="brown", text="Do they have black hair?",state = DISABLED )
    if color == "red":
        red.destroy()
        red = Button(questionFrame2, bg="tan", fg="brown", text="Do they have red hair? ",state = DISABLED)
    if color == "brown":
        brown.destroy()
        brown = Button(questionFrame2, bg="tan", fg="brown", text="Do they have brown hair? ",state = DISABLED)
    if color == "white":
        white.destroy()
        white = Button(questionFrame2, bg="tan", fg="brown", text="Do they have white hair?",state = DISABLED)

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
