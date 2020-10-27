import YTDownloader as yt 
from tkinter import *


def singleSong():
    
    string = e.get()
    yt.singleVideo(string)  

def playlist():
    string = e.get()
    yt.playlistVideos(string,"./")

def fromFile():
    yt.videoFromFiles("./")



root = Tk()
def openNewWindow1(): 
      

    root = Tk()
    global e 
    e = Entry(root)
    e.pack()
    e.focus_set()

    
    b = Button(root,text='okay',bd=10, command = singleSong)
    b.pack(side='top')

def openNewWindow2(): 
      

    root = Tk()
    global e 
    e = Entry(root)
    e.pack()
    e.focus_set()


    
    b = Button(root,text='okay',bd=10,command = playlist)
    b.pack(side='top')

def openNewWindow3(): 
      
    root = Tk()
    global e 

    btnFile = Button(root,text = "Okay", bd = 10,command = fromFile)
    btnFile.pack(side= TOP)




btnSingle = Button(root,text = "Single Video", bd=10, command = openNewWindow1)
btnSingle.pack(side= TOP)

btnPlaylist = Button(root,text = "Playlist", bd = 10, command = openNewWindow2)
btnPlaylist.pack(side= TOP)

btnFile = Button(root,text = "Download from File",bd = 10, command = openNewWindow3)
btnFile.pack(side= TOP)


root.mainloop()