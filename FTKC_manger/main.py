from tkinter import *
from PIL import ImageTk, Image
import subprocess
root = Tk()
root.title('FTCCM')
root.geometry('205x205')
root.resizable(False, False)
new_PLC_image_file = Image.open('images\\new_PLC_project.png')
new_PLC_image_file_resize = new_PLC_image_file.resize((200, 200))
new_PLC_image = ImageTk.PhotoImage(new_PLC_image_file_resize)
format_type = StringVar()

def do_it():
    subprocess.Popen("python cp.py", creationflags=subprocess.CREATE_NO_WINDOW)
Button(root, image=new_PLC_image,command=do_it).place(x=0,y=0)
root.mainloop()
#do not use this one
