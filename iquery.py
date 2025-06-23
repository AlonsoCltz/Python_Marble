from tkinter import *
def printInfo():
    print(slider.get())
window=Tk()
slider=Scale(window,from_=0,to=10)
slider.pack()
Button(window,text='restart',command=printInfo).pack()
window.mainloop()