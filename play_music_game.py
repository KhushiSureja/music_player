#music_player

import pygame
from pygame import mixer
from tkinter import*
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("playing")
    mixer.music.play()

def pausesong():
    songstatus.set("paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("resuming")
    mixer.music.unpause()

root=Tk()
root.title('best music player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist-----

os.chdir(r'D:\myplayList')

playlist=Listbox(root,selectmode=SINGLE,bg="blue",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)
song=os.listdir()
for s in song:
    playlist.insert(END,s)

playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial',20),bg="blue",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="blue",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="blue",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

resumebtn=Button(root,text="resume",command=resumesong)
resumebtn.config(font=('arial',20),bg="blue",fg="white",padx=7,pady=7)
resumebtn.grid(row=1,column=3)

mainloop()


