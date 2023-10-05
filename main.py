from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('FTCM')
root.geometry('405x220')
root.resizable(False, False)
new_PLC_image_file = Image.open('images\\new_PLC_project_py.png')
new_PLC_image_file_resize = new_PLC_image_file.resize((100, 100))
new_PLC_image = ImageTk.PhotoImage(new_PLC_image_file_resize)
format_type = StringVar()

def do_it():
    os.system('start cmd /k "python cp.py"')
Button(root, image=new_PLC_image,command=do_it).place(x=0,y=0)
new_PLC_image_file1 = Image.open('images\\new_PLC_project_c.png')
new_PLC_image_file_resize1 = new_PLC_image_file1.resize((100, 100))
new_PLC_image1 = ImageTk.PhotoImage(new_PLC_image_file_resize1)
format_type1 = StringVar()

def do_it2():
    os.system('start cmd /k "cd FTCC_manger & cp.py"')
Button(root, image=new_PLC_image1,command=do_it2).place(x=100,y=0)
new_PLC_image_file2 = Image.open('images\\new_PLC_project_java.png')
new_PLC_image_file_resize2 = new_PLC_image_file2.resize((100, 100))
new_PLC_image2 = ImageTk.PhotoImage(new_PLC_image_file_resize2)
format_type2 = StringVar()
def do_it3():
    os.system('start cmd /k "cd FTJC_manger & cp.py"')
Button(root, image=new_PLC_image2,command=do_it3).place(x=200,y=0)
new_PLC_image_file3 = Image.open('images\\new_PLC_project_JS.png')
new_PLC_image_file_resize3 = new_PLC_image_file3.resize((100, 100))
new_PLC_image3 = ImageTk.PhotoImage(new_PLC_image_file_resize3)
format_type3 = StringVar()
def do_it4():
    os.system('start cmd /k "cd FTJSC_manger & cp.py"')
Button(root, image=new_PLC_image3,command=do_it4).place(x=300,y=0)
new_PLC_image_file4 = Image.open('images\\new_PLC_project_kotlin.png')
new_PLC_image_file_resize4 = new_PLC_image_file4.resize((100, 100))
new_PLC_image4 = ImageTk.PhotoImage(new_PLC_image_file_resize4)
format_type4 = StringVar()
def do_it5():
    os.system('start cmd /k "cd FTKC_manger & cp.py"')
Button(root, image=new_PLC_image4,command=do_it5).place(x=0,y=110)

new_PLC_image_file5 = Image.open('images\\new_PLC_project_html.png')
new_PLC_image_file_resize5 = new_PLC_image_file5.resize((100, 100))
new_PLC_image5 = ImageTk.PhotoImage(new_PLC_image_file_resize5)
format_type5 = StringVar()
def do_it6():
    os.system('start cmd /k "cd FTHC_manger & cp.py"')
Button(root, image=new_PLC_image5,command=do_it6).place(x=100,y=110)

new_PLC_image_file6 = Image.open('images\\new_PLC_project_batch.png')
new_PLC_image_file_resize6 = new_PLC_image_file6.resize((100, 100))
new_PLC_image6 = ImageTk.PhotoImage(new_PLC_image_file_resize6)
format_type6 = StringVar()
def do_it7():
    os.system('start cmd /k "cd FTBC_manger & cp.py"')
Button(root, image=new_PLC_image6,command=do_it7).place(x=200,y=110)
new_PLC_image_file7 = Image.open('images\\new_PLC_project.png')
new_PLC_image_file_resize7 = new_PLC_image_file7.resize((100, 100))
new_PLC_image7 = ImageTk.PhotoImage(new_PLC_image_file_resize7)
format_type7 = StringVar()
def do_it8():
    os.system('start cmd /k "GLCprojectcreator.py"')
Button(root, image=new_PLC_image7,command=do_it8).place(x=300,y=110)
root.mainloop()

