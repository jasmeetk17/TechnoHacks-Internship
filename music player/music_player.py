import tkinter
import pygame
import customtkinter
from PIL import Image,ImageTk
from threading import *
import time 
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root=customtkinter.CTk()
root.title('Music Player')
root.geometry('400x480')

#pymixer used for the audio liabrary in python
pygame.mixer.init()

#list of songs and images
list_of_songs=['D:\TechnoHacks EduTech Projects\music player\music\Photo.wav','D:\TechnoHacks EduTech Projects\music player\music\everybody hurts.wav']
list_of_images=['D:\TechnoHacks EduTech Projects\music player\img\Photo.png','D:\TechnoHacks EduTech Projects\music player\img\\no name.png']

n=0

#get details of album
def get_album_cover(song_name,n):

    image1=Image.open(list_of_images[n])
    image2=image1.resize((250,250))
    load=ImageTk.PhotoImage(image2)
    label1=tkinter.Label(root,image=load)
    label1.image=load
    label1.place(relx=.19,rely=.06)

    stripped_string=song_name[51:-4]
    song_name_label=tkinter.Label(text=stripped_string,bg='#222222',fg='white')
    song_name_label.place(relx=.4,rely=.6)

#progress
def progress():
    
    a=pygame.mixer.Sound(list_of_songs[n])
    song_len=a.get_length()*3
    for i in range(0,math.ceil(song_len)):
        time.sleep(.3)
        progressbar.set(pygame.mixer.music.get_pos()/1000000)

#threading
def threading():
    t1=Thread(target=progress)
    t1.start()

#funtionality of playing music
def play_music():
    threading()
    global n
    current_song=n
    if n>2:
        n=0
    song_name=list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)

    print(get_album_cover(song_name,n))

    n+=1

#functionality of skiping music
def skip_forward():
    play_music()

#functionality of skiping backward
def skip_backward():
    global n
    n-=2
    play_music()

#change volume
def volume(value):
    pygame.mixer.music.set_volume(value)

#stop
def stop():
    pygame.mixer.music.stop()

#when the screen close the music will stop functionality
def stop_music_on_close():
    pygame.mixer.music.stop()
    root.destroy()


#playbutton
play_button=customtkinter.CTkButton(master=root,text="Play",command=play_music,width=130)
play_button.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

#skipforwad
skip_f=customtkinter.CTkButton(master=root,text=">",command=skip_forward,width=2)
skip_f.place(relx=0.7,rely=0.7,anchor=tkinter.CENTER)

#skipforwad
skip_b=customtkinter.CTkButton(master=root,text="<",command=skip_backward,width=2)
skip_b.place(relx=0.3,rely=0.7,anchor=tkinter.CENTER)

#slider
slider=customtkinter.CTkSlider(master=root,from_=0,to=6,command=volume,width=210)
slider.place(relx=0.5,rely=0.78,anchor=tkinter.CENTER)

#progressbar
progressbar=customtkinter.CTkProgressBar(master=root,progress_color='#32a85a',border_width=.1,width=250)
progressbar.place(relx=.5,rely=.85,anchor=tkinter.CENTER)

#stop button
stop=customtkinter.CTkButton(master=root,text="Stop",command=stop,width=2)
stop.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)

# Bind window closing event to stop music and close window
root.protocol("WM_DELETE_WINDOW", stop_music_on_close)

root.mainloop()