from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("The Agrestal West")
root.geometry("10000x10000")

f1 = Frame(root)
f1.pack()
#Variables
gold = 5000


#The Rambo Scene
click = 0
amount = 1

#pics place
pic8 = PhotoImage(file = "Mumflr opening morax's cage.png")
pic6 =PhotoImage(file = "Mumflr 2.png")
pic7 =PhotoImage(file = "Part1ofthetown.png")
pic1 = PhotoImage(file = "Mumflr Fumperdink full body pic.png")
pic2 = PhotoImage(file = "THe horsery.png")
pic9 = PhotoImage(file = "Cursed Mumflr Fumperdink.png")
pic10 = PhotoImage(file = "The Horsery Owner.png")
pic11 = PhotoImage(file = "Mumflr Holding a snake Oiling book.png")
pic12 = PhotoImage(file= "Mumflr Killing his first snake.png")
pic13 = PhotoImage(file = "First fight against the snake.png")
pic14 = PhotoImage(file = "DEad snake.png")
pic15 = PhotoImage(file = "Dude Hide Behind the rock.png")
pic16 = PhotoImage(file = "Dude now snipe those snakes and get the horse.png")
pic17 = PhotoImage(file = "Mumflr Mounting his gun.png")
pic18 = PhotoImage(file = "MAP.png")
pic19 = PhotoImage(file = "SPAM clicking the snakes.png")
pic20 = PhotoImage(file = "Nani There were all 3 of the horses over there.png")
pic21 = PhotoImage(file = "The horses follow you when you have the oats1.png")
pic22 = PhotoImage(file = "The horses follow you when you have the oats.png")
pic23 = PhotoImage(file = "The returning of the horses.png")
pic24 = PhotoImage(file = "Mumflr Entering the SAloon.png")
pic25 = PhotoImage(file = "The Bartender.png")
pic26 = PhotoImage(file = "Map 2.0.png")
pic27 = PhotoImage(file = "The Grand Junction.png")
pic28 = PhotoImage(file = "Kamisoto AYato.png")
pic29 = PhotoImage(file = "IS it the end.png")
pic30 = PhotoImage(file = "I WILL HAVE ORDER.png")
pic31 = PhotoImage(file = "THe ENd.png")
pic32 = PhotoImage(file = "The end finally.png")


#Definitions of stuff
def go_to_ur_bro():
	l4 = Label(f1,text="Timflr I'm moving out.", font=("Arial", 13))
	l4.grid(row=10, column=2)
	l5 = Label(f1, text="                               So long brother Mumflr, I'll miss you.", font=("Arial", 13))
	l5.grid(row=11, column=2)



def go_to_ur_mum():
	l6 = Label(f1, text="Mom I'm moving out.", font=("Arial", 13))
	l6.grid(row=13, column=2)
	l7 = Label(f1, text="                                                                              Good. I mean I'm gonna 100% miss you, so sad boo hoo. Now leave!", font=("Arial", 13))
	l7.grid(row=14, column=2)
	l8 = Label(f1, text="                     (What kind of a mother do I have?)", font=("Arial", 13))
	l8.grid(row=15, column=2)



def go_to_ur_dad():
	l9 = Label(f1, text="Pops I'm leaving.",font=("Arial", 13))
	l9.grid(row=16, column=2)
	l10 = Label(f1, text="                                                                        Finally one less liability. Wait, I mean I am gonna miss you.", font=("Arial", 13))
	l10.grid(row=17, column=2)
	l11=Label(f1, text="                       (What kind of a family do I live with?)",font=("Arial", 13))
	l11.grid(row=18, column=2)





def go_to_ur_raven():
	global l15, l14, l13,l12, pic8
	l15=Label(f1, image=pic8)
	l15.grid(row= 19, column = 1)
	l12=Label(f1, text="                                                    Morax my man it's time, you are now free from your cage",font=("Arial",13))
	l12.grid(row=19, column=2)
	l13=Label(f1, text="                                                    *You open Morax's cage and he flies off into the distance*",font=("Arial",13))
	l13.grid(row=20, column=2)
	l14=Label(f1, text="                              Now it's time for me to go and live my life",font=("Arial",13))
	l14.grid(row=21, column=2)




def next_scene():
	f1.destroy()
	f2.pack()
def scene_3():
	f2.destroy()
	f3.pack()
def scene_4():
	f3.destroy()
	f4.pack()
def horsery():
	f4.destroy()
	f5.pack()
#def saloon():
	pass
#def sheriff():
	pass
def hay():
	l31=Label(f5,text = "You found 2 needles")
	l31.grid(row = 11,column = 1)
def talk_to_the_owner():
	f5.destroy()
	f6.pack()
def task1():
	f6.destroy()
	f7.pack()
def map():
	f7.destroy()
	f8.pack()
def BSR():
	f8.destroy()
	f9.pack()
def Enter_the_Ravine():
	f9.destroy()
	f10.pack()

def Read_1st_book():
	l48 = Label(f9, text = "You learn how to counter snakes, and how you can make use of them and you get a free gun with 100 bullets")
	l48.grid(row = 6, column = 5)
	btn15 = Button(f9, text = "Continue", command = Enter_the_Ravine)
	btn15.grid(row = 7, column =5)
def Fire1():
	f10.destroy()
	f11.pack()
def Fire_again():
	f11.destroy()
	f12.pack()
def Look_for_horse1():
	f12.destroy()
	f13.pack()
def Behind_the_rock():
	f13.destroy()
	f14.pack()
def Rambo():
	f14.destroy()
	f15.pack()

def scene_16():
	f15.destroy()
	f16.pack()

def clicked():
	global click
	global amount
	click += amount
	if click == 25:
		f16.destroy()
		f17.pack()
def REad_the_book():
	l67 = Label(f17, text = "I failed Gary, and now I dropped my book, guns and ammo and now I'm surrounded by snakes")
	l67.grid(row =5, column = 5)
def Bait_the_horses():
	f17.destroy()
	f18.pack()	
def MAP1():
	f18.destroy()
	f19.pack()
def Slumpersville():
	f19.destroy()
	f20.pack()
def Return_the_horses():
	f20.destroy()
	f21.pack()
def The_End_of_chapter_1():
	f21.destroy()
	f22.pack()
def Exit_the_Horsery():
	f22.destroy()
	f23.pack()
def Welcome_to_the_Saloon():
	f23.destroy()
	f24.pack()
def Talk_to_the_bartender():
	f24.destroy()
	f25.pack()
def TRAIN():
	f25.destroy()
	f26.pack()
def THE_station():
	f26.destroy()
	f27.pack()
def SAVEOURBOWLS():
	f27.destroy()
	f28.pack()
def Enter_THE_TRain():
	f28.destroy()
	f29.pack()
def Somehow():
	f29.destroy()
	f30.pack()
def I_WILL_HAVE_ORDER():
	f30.destroy()
	f31.pack()
def THE_END():
	f31.destroy()
	f32.pack()
def THE_END_SRSLY():
	f32.destroy()
	f33.pack()

#Gameplay
l1 = Label(f1, text="You've turned 18 two weeks ago, it's time you move out",font=('Arial', 13))
l1.grid(row=3, column=2)
l2=Label(f1, text="You think about all the good memories you had ",font=('Arial',13))
l2.grid(row=4, column=2)
l3=Label(f1, text= "You can't just leave yet, you have to say goodbye to your family",font=('Arial',13))
l3.grid(row=5, column=2)




btn1=Button(f1, text="Go to your younger brother", command=go_to_ur_bro)
btn1.grid(row=6, column=2)


btn2=Button(f1, text="Go to your mom",command=go_to_ur_mum)
btn2.grid(row=7, column=2)

btn3=Button(f1, text="Go to your dad",command=go_to_ur_dad)
btn3.grid(row=8, column=2)

btn4=Button(f1, text="Go to your pet raven",command=go_to_ur_raven)
btn4.grid(row=9, column=2)

btn5=Button(f1, text="Live your life",command=next_scene)
btn5.grid(row=22,column=2)




#scene 2



f2=Frame(root)

pic5=PhotoImage(file = "Mumflr on the horse carriage.png")

l20 = Label(f2,image=pic5)
l20.grid(row = 3,column=2)
l13=Label(f2, text="*You set up the horse cart and wander around the land ",font=("Arial",13))
l13.grid(row=4,column=2)
l16=Label(f2, text = "*Night falls and you hear the sound of horses and men speaking spanish*",font=("Arial",13))
l16.grid(row = 5, column=2)
l17=Label(f2, text = "(Oh no! It must be the wild ones!)",font=("Arial",13))
l17.grid(row = 6, column=2)
l18=Label(f2, text = "(I should make a run for it)",font=("Arial", 13))
l18.grid(row = 7, column=2)
l21 = Label(f2, text = "(You lash the horse's reins but, a hard metal object strikes your head and you go unconsious)",font=("Arial",13))
l21.grid(row = 8, column=2)
btn5=Button(f2, text="Continue",command=scene_3)
btn5.grid(row=9,column=2)


# scene 3
f3=Frame(root)
l26 = Label(f3, image = pic6)
l26.grid(row = 3,column=2)
l22 = Label(f3,text = "You wake up with a sharp pain in your head",font= ("Arial",13))
l22.grid(row = 4,column=2)
l23 = Label(f3,text = "You check your pockets and find that you'd been completely plundered",font= ("Arial",13))
l23.grid(row = 5,column=2)
l24 = Label(f3,text = "You look around and see that you are in an unknown town called 'Slumpersville'",font= ("Arial",13))
l24.grid(row = 6,column=2)
l25 = Label(f3,text = "You should search the town to get a sense of what's going on ",font= ("Arial",13))
l25.grid(row = 7,column=2)
btn6=Button(f3,text = "Explore the town", command = scene_4)
btn6.grid(row = 8, column = 2)


#scene 4
f4=Frame(root)
l27= Label(f4, image = pic7)
l27. grid(row=1, column = 1)
l28 = Label(f4, image = pic1)
l28.grid(row = 13, column = 1)
#label=Label(f4, text = "Testing",font = ("Arial",28))
#label.grid(row = 3, column = 2)
btn6=Button(f4,text = "Check out the horsery",command = horsery)
btn6.grid(row=10,column=1)
#btn7=Button(f4,text = "Check out the Saloon", command = saloon)
#btn7.grid(row = 12,column = 1)
#btn8=Button(f4,text = "Check out the Sheriff's department")
#btn8.grid(row = 11, column = 1)

#scene 5 aka enter the horsery
f5 = Frame(root)
l30 = Label(f5, image = pic2)
l30.grid(row = 2, column = 1)
btn9=Button(f5,text = "Check the haystacks",command = hay)
btn9.grid(row=9, column = 1)
btn10 = Button(f5,text = "Talk to the owner",command = talk_to_the_owner)
btn10.grid(row=10, column = 1)

#scene 6 # talk with the owner
f6 = Frame(root)
l32 = Label(f6,image = pic9)
l32.grid(row = 3, column = 1)
l34 = Label(f6,image = pic10)
l34.grid(row = 3, column = 5)
l33 = Label(f6, text = "        						  How's business?",font=("Arial",13))
l33.grid(row = 4, column = 1)
l35 = Label(f6, text = "        Not too good, 3 of my horses escaped and there isn't anything I can do to get them back.",font=("Arial",13))
l35.grid(row = 5,column=2)
l36 = Label(f6, text = "                               Maybe I can help.",font=("Arial",13))
l36.grid(row = 6,column=1)
l37 = Label(f6, text = "As if, these horses wandered off to the most dangerous spot in the West.",font=("Arial",13))
l37.grid(row = 7,column = 2)
l38 = Label(f6, text = "                      I'm willing to take up a challenge and plus I survived the wild ones.",font = ("Arial",13))
l38.grid(row = 8, column = 1)
l39 = Label(f6 , text = "If you really did then why don't you go to 'The Black Snake Ravine', one of my horses wander there",font = ("Arial",13))
l39.grid(row = 9, column = 2)
l40 = Label(f6, text = "Fine go and mark it on a map and I'll get you your horse back",font = ("Arial",13))
l40.grid(row = 10, column =1)
btn11 = Button(f6, text = "Exit the horsery and go do your task",command=task1)
btn11.grid(row =11, column=2)

#scene 7 
f7 = Frame(root)

l41 = Label(f7, image = pic7)
l41.grid(row = 2,column = 2)
l42 = Label(f7, image =pic1)
l42.grid(row = 5,column = 2)
btn12 = Button(f7,image = pic18,command = map)
btn12.grid(row = 7,column=8)

#map design
f8 = Frame(root)	
btn13 = Button(f8, text = "'The Black Snake Ravine'",command = BSR)
btn13.grid(row = 5, column = 5)

#The Black Snake ravine
f9=Frame(root)
l44 = Label(f9, image = pic11)
l44.grid(row = 3,column =5)
l43=Label(f9,text = "You find a book on the ground, it reads 'Snake Oiling'",font = ("Arial",13))
l43.grid(row = 4,column=5)
b14 = Button(f9, text = "Read it", command = Read_1st_book)
b14.grid(row = 5, column =5)
b17 = Button (f9, text = "Continue")
#Scene 10
f10=Frame(root)
l49 = Label(f10, image = pic13)
l49.grid(row = 1, column =5)
l50 = Label(f10, text = "While walking down ,you see a snake! Use the gun and shoot it", font = ("Arial",13))
l50.grid(row = 2, column = 5)
b17=Button(f10, text = "SHOOT!", command = Fire1)
b17.grid(row =3, column =5)
#scene 11
f11=Frame(root)
l52 = Label(f11,image = pic12)
l52.grid(row = 3, column =5)
b18 = Button(f11, text = "Fire again you didn't kill it", command = Fire_again)
b18.grid(row =4,column=5)

# scene 12
f12 = Frame(root)
l61 = Label(f12, image = pic14)
l61.grid(row = 2, column = 5)
l60=Label(f12, text ="You Killed it, now go find the horse",font = ("Arial",13))
l60.grid(row =3, column = 5)
b19 = Button(f12, text = "Continue walking", command = Look_for_horse1)
b19.grid(row = 4, column =5)

#scene 13
f13 = Frame(root)
l62 = Label(f13, image = pic15)
l62.grid(row =2, column =5)
l63 = Label(f13, text = "You've found a horse, but there are tons of snakes to the right")
l63.grid(row = 3, column =5)
b21 = Button(f13, text = "DUDE GET BEHIND THAT ROCK NOW!!!", command = Behind_the_rock)
b21.grid(row = 4, column =5)

#scene 14
f14 = Frame(root)
l64 = Label(f14, image = pic16)
l64.grid(row = 2, column = 5)
b22 = Button(f14, text = "Mount your gun on the rock and become Rambo", command = Rambo)
b22.grid(row = 3, column =5)

# scene 15
f15 = Frame(root)
l65 = Label(f15, image= pic17)
l65.grid(row = 2, column = 5)
b23=Button(f15, text = "Get ready to fire(Spam click the next button)", command = scene_16)
b23.grid(row = 3, column =5)

#scene 16
f16 = Frame(root)
l64 = Label(f16, image = pic19)
l64.grid(row = 2, column =5)
b24 = Button(f16, text = "FIRE!", command = clicked)
b24.grid(row = 3, column = 5)

#scene 17
f17 = Frame(root)
l65 = Label(f17,image = pic20)
l65.grid(row = 2,column =5)
l58 = Label(f17, text = "")
l66 = Label(f17,text = "After killing the snakes, you go behind the rocks and find all 3 horses! But there is a skeleton having a note and a bag of oats with him")
l66.grid(row = 3, column = 5)
b25 = Button(f17, text = "Read the note",command = REad_the_book)
b25.grid(row = 4, column = 5)
b26 = Button(f17, text = "Grab the Oat bag",command = Bait_the_horses)
b26.grid(row = 6, column = 5)

#Scene 18
f18 = Frame(root)
l70 = Label(f18, image = pic21)
l70.grid(row = 3, column = 5)
l69 = Label(f18,text = "You grab the bag, and see that the horses are now following you")
l69.grid(row = 4,column = 5)
l71 = Label(f18, text = "I know a very great use of this, you to say to yourself")
l71.grid(row = 5, column = 5)
b27 = Button(f18, image = pic18, command = MAP1)
b27.grid(row = 6, column = 5)

#scene 19
f19 = Frame(root)
btn28 = Button(f19, text = "'The Black Snake Ravine'",command = BSR)
btn28.grid(row = 5, column = 5)
btn29 = Button(f19, text = "Slumpersville",command = Slumpersville)
btn29.grid(row = 10, column = 5)

#scene 20
f20 = Frame(root)
l72 = Label(f20,image = pic7)
l72.grid(row = 3, column = 5)
l73 = Label(f20,image = pic22)
l73.grid(row = 4, column =5)
b30 = Button(f20,text = "Enter the horsery",command = Return_the_horses)
b30.grid(row =5, column =5)

#scene 21
f21 = Frame(root)
l74 = Label(f21, image =pic23 )
l74.grid(row = 2, column =5)
b31 = Button(f21, text = "talk to the owner",command = The_End_of_chapter_1)
b31.grid(row = 3, column =5)

#scene 22
f22 = Frame(root)
l76 = Label(f22, image = pic9)
l76.grid(row = 3,column =1)
l77 = Label(f22, image = pic10)
l77.grid(row = 3, column = 5)
l75 = Label(f22, text = "Told you, I'd do the work", font = ("Arial",13))
l75.grid(row = 4, column =1)
l78 = Label(f22,text = "I'm impressed, here's 5000, gold", font = ("Arial",13))
l78.grid(row = 5, column = 5)
l79 = Label(f22, text = "*You recieve 5000 gold*", font = ("Arial",13))
l79.grid(row =6, column = 3)
l80 = Label(f22, text = "By the way what's with that Upside down horse?", font = ("Arial",13))
l80.grid(row = 7, column = 1)
l81 = Label(f22, text = "Oh it's just that he eats too much locoweed", font = ("Arial",13))
l81.grid(row = 8, column = 5)
l82 = Label(f22, text = "Huh, ok", font = ("Arial",13))
l82.grid(row = 9, column = 1)
b32 = Button(f22, text = "Exit",command = Exit_the_Horsery)
b32.grid(row = 11, column = 3)
#Scene 23
f23 = Frame(root)
pic7
l80 = Label(f23, image = pic7)
l80.grid(row = 3, column = 5)
l81 = Label(f23,image =pic1 )
l81.grid(row = 5, column = 5)
b33 = Button(f23, text = "Enter the Saloon", command = Welcome_to_the_Saloon)
b33.grid(row = 4, column =5)

#Chapter 2 The Saloon
f24=Frame(root)
l82 = Label(f24, image = pic24)
l82.grid(row = 2, column =5)
b34 = Button(f24, text = "Talk to the bartender", command = Talk_to_the_bartender)
b34.grid(row = 3, column =5)

# Talking to the bartender
f25 = Frame(root)
l83 = Label(f25, image = pic25)
l83.grid(row =3, column = 5)
l84 = Label(f25, image =pic9 )
l84.grid(row = 3, column =2)

l85 = Label(f25, text = "Can I help you?", font = ("Arial",13))
l85.grid(row = 4, column = 5)
l86 = Label(f25, text = "I'd like a hard liquor",font = ("Arial",13))
l86.grid(row = 4, column = 2)
l87 = Label(f25, text = "Coming right up",font = ("Arial",13))
l87.grid(row = 5, column = 5)
l88 = Label(f25 , text = "*He hands you your drink*", font = ("Arial",13)) 
l88.grid(row = 5, column = 3)
l89 = Label(f25, text = "Blech! This tastes like you added water in this", font = ("Arial",13))
l89.grid(row = 7, column = 2)
l90 = Label(f25, text = "I'm sorry ever since we stopped recieving supplies of them this what I had to resort to", font = ("Arial",13))
l90.grid(row = 8,column =5)
l91 = Label(f25, text = "I can't deal with this! Tell me everything about you supplier", font = ("Arial",13))
l91.grid(row = 9, column = 2)
l92 = Label(f25, text = "Ok, my supplier is Grand Junction's. It turns out his trains are always being hijacked by the infamous robber Kamisoto Ayato")
l92.grid(row = 10, column=5)
l93 = Label(f25, text = "*He hands you a map showing where the next supply is coming*")
l93.grid(row = 11, column = 3)
b35 = Button(f25, text = "SAY NO MORE!", command = TRAIN)
b35.grid(row = 12, column = 3)

# Scene 26
f26 = Frame(root)
l94 = Label(f26, image =pic7)
l94.grid(row = 5, column = 5)
l95 =Label(f26, image = pic1)
l95.grid(row = 6, column = 5)
b36 = Button(f26, image = pic26, command = THE_station)
b36.grid(row = 7, column = 7)

#THE MAP 3.0
f27 = Frame(root)
btn38= Button(f27, text = "Slumpersville")
btn38.grid(row = 10, column = 5)
b37 = Button(f27, text = "The tracks of the Grand Junction",command = SAVEOURBOWLS)
b37.grid(row =10, column = 2 )

#Scene 28
f28 = Frame(root)
l96 = Label(f28, image = pic27)
l96.grid(row = 5, column = 5)
l97 = Label(f28, text = "You see the Grand Junction. Get on to it now", font = ("Arial", 13))
l97.grid(row = 6,column = 5)
b38 = Button(f28, text = "Climb on and break in",command = Enter_THE_TRain )
b38.grid(row = 7, column = 5)

#Scene 29
f29 = Frame(root)
l98 = Label(f29, image = pic28)
l98.grid(row = 2, column = 5)
l99 = Label(f29, text = "'Hands up where I can see them', Ayato says to thw conductor", font = ("Arial",13))
l99.grid(row =3 ,column =5)
l100 = Label(f29, text = "Oh I don't think it's your lucky day today", font = ("Arial",13))
l100.grid(row = 4,column = 5)
l101 = Label(f29, text = "'I see another challenger approaches?', Ayato says", font = ("Arial",13))
l101.grid(row = 5, column = 5)
b39 = Button(f29, text = "This will be your death day, You say", command = Somehow)
b39.grid(row = 6, column = 5)

#Scene 30 
f30 = Frame(root)
l103 = Label(f30, image = pic29 )
l103.grid(row = 2, column = 5)
l102 = Label(f30, text = "Huh, where'd my weapon go and why am I here?, you say" , font = ("Arial",13))
l102.grid(row = 3, column = 5)
l104 = Label(f30, text = "Say your prayers kid, Ayato says")
l104.grid(row = 4, column= 5)
b40 = Button(f30, text = "NOOOOOOOOOOOOOOOOOOOOOOOO", command = I_WILL_HAVE_ORDER)
b40.grid(row = 5, column = 5)

#scene 31
f31 = Frame(root)
l106 = Label(f31, image = pic30)
l106.grid(row = 2, column = 5)
l107 = Label(f31, text = "I Will Have Order",font = ("Arial",13))
l107.grid(row = 3, column = 5)
l105 = Label(f31, text = "Morax?????")
l105.grid(row = 4, column = 5)
l108 = Label(f31, text = "Yes, I was secretly an archon all this time. I wish not for dominion yet I cannot watch the common folk suffer",font = ("Arial",13))
l108.grid(row = 5, column =5)
b44 = Button(f31, text = "Ok imma do my work now",command =THE_END)
b44.grid(row = 6, column = 5)

#Scene 32
f32 = Frame(root)
l111 = Label(f32, image = pic31)
l111.grid(row = 2, column = 5)
l110 = Label (f32, text = "'Huh Slumpersville already?'. you say to yourself", font = ("Arial",13))
l110.grid(row = 3, column=5)
l112 = Label(f32, text = "Yes and now you secured our supply line You are now the Hero of the town", font = ("Arial", 13))
l112.grid(row = 4, column = 5)
b42 = Button(f32 ,text = 'WHOHOOOO', command = THE_END_SRSLY)
b42.grid(row = 5, column = 5)
# THE END
f33 = Frame(root)
l113 = Label(f33, image = pic32)
l113.grid(row =2,column = 5)

root.mainloop()