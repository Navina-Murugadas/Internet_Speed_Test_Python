from tkinter import *
import speedtest
from PIL import ImageTk

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.resizable(0,0)
backgroundImage = ImageTk.PhotoImage(file='purple.jpg.')
bgLabel = Label(sp, image=backgroundImage)
bgLabel.place(x=0, y=0)

lab = Label(sp, text= "INTERNET SPEED TEST", font=("Algerian",28,"bold"), bg='gold', fg='DarkOrchid4')
lab.place(x=45,y=37, height=50, width=410)

lab = Label(sp, text= "Download Speed", font=("Comic Sans MS",28,"bold"), bg='magenta4', fg='goldenrod2')
lab.place(x=60,y=130, height=55, width=380)

lab_down = Label(sp, text= "00", font=("Comic Sans MS",25,"bold"), bg='plum1', fg='red4')
lab_down.place(x=118,y=200, height=50, width=270)

lab = Label(sp, text= "Upload Speed", font=("Comic Sans MS",28,"bold"), bg='magenta4', fg='goldenrod2')
lab.place(x=60,y=290, height=55, width=380)

lab_up = Label(sp, text= "00", font=("Comic Sans MS",25,"bold"), bg='plum1', fg='red4')
lab_up.place(x=118,y=360, height=50, width=270)

button = Button(sp,text="CHECK SPEED", font=("Comic Sans MS",10,"bold"), relief=RAISED, bg="red", command=speedcheck)
button.place(x=177,y=480, height=50, width=150)

sp.mainloop()
