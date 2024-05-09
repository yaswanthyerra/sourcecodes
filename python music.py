import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def skipsong():
    songstatus.set("Skipped")
    mixer.music.skip()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root=Tk()
root.title("Music Player project")

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playing---

playlist=Listbox(root,selectmode=SINGLE,bg="pink",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'D:\songs')
songs=os.listdir()

for i in songs:
    playlist.insert(END,i)

playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('arial',20),bg="green",fg="white",padx=10,pady=10)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=10,pady=10)
pausebtn.grid(row=1,column=1)

skipbtn=Button(root,text="Skip",command=skipsong)
skipbtn.config(font=('arial',20),bg="red",fg="white",padx=10,pady=10)
skipbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=10,pady=10)
Resumebtn.grid(row=1,column=3)

mainloop()
