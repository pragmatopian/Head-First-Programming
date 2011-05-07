from tkinter import *
import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass

def playsound(soundname):
    s = sounds.Sound(soundname)
    wait_finish(s.play())

def click_right():
    playsound("heartbeat.wav")
    playsound("correct.wav")
    numright.set(numright.get() + 1)

def click_wrong():
    playsound("heartbeat.wav")
    playsound("wrong.wav")
    numwrong.set(numwrong.get()+1)

app = Tk()
app.title = ("TVN Game Show") #DW - doesn't display
app.geometry('300x110+200+100')

sounds = pygame.mixer
sounds.init()

numright = IntVar()
numright.set(0)
numwrong = IntVar()
numwrong.set(0)

lblintro = Label(app, text="When you are ready, click on the buttons!", height = 3)
lblintro.pack()

cmdright = Button(app, text = "Right", width = 10, command = click_right)
cmdright.pack(side = 'left', padx = 10, pady = 10)

cmdwrong = Button(app, text = "Wrong", width = 10, command = click_wrong)
cmdwrong.pack(side = 'right', padx = 10, pady = 10)

lblright = Label(app, textvariable = numright)
lblright.pack(side = 'left')

lblwrong = Label(app, textvariable = numwrong)
lblwrong.pack(side = 'right')

app.mainloop()
