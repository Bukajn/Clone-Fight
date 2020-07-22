from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Launcher")
root.geometry("400x200")
root.resizable(False,False)

app = Frame(root, width =400,height=200)
app.grid()

img = ImageTk.PhotoImage(Image.open("./static/tytul.png"))
img = img._PhotoImage__photo.subsample(2)
panel = Label(app, image = img)
panel.place(x=10,y=10)

root.mainloop()