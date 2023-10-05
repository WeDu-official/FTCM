import os
import tkinter as tk
r = tk.Tk()
r.title('create project')
r.geometry('300x53')
class first():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('GLC normal project')
        self.root.geometry('300x100')
        tk.Label(self.root, text='write the project path').pack()
        self.code_text = tk.Text(self.root,width=self.root.winfo_screenwidth(),height=1, bg='white', insertbackground='black', fg='black', font=("Arial", 12))
        self.code_text.pack()
        tk.Button(self.root, text='create it', command=self.create).pack()
        self.root.mainloop()
    def scan_folder2(self,folder_path):
        file_list = []
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_list.append(os.path.join(root, file_name))
        return file_list
    def create(self):
        creation_location1 = self.code_text.get("1.0",tk.END)
        creation_location = creation_location1[:-1]

        print(creation_location)
        print("starting creation of GLC project[1/2]")
        os.mkdir(creation_location)
        print("project folder created")
        os.mkdir(f"{creation_location}\\GLC")
        print("GLC folder in project created")
        print("start files scanning")
        files_list2 = self.scan_folder2("GLC")
        print("files scanned")
        print("starting creation of GLC project[2/2]")
        for listnum in files_list2:
            print(f"{listnum}")
            print(f"starting {listnum} operation")
            print(f"start read the scanned {listnum}")
            var1 = open(f"{listnum}", "r")
            print(f"the scanned {listnum} reading operation ended")
            print("creating file in project")
            var2 = open(f"{creation_location}\\{listnum}", "x")
            print("creating file in project completed")
            print("starting transport the copied scanned file contained to new project file")
            var3 = open(f"{creation_location}\\{listnum}", "w")
            var3.write(var1.read())
            print("transport completed")
            print("starting closing file operations")
            var1.close()
            var2.close()
            var3.close()
            print("closing completed")
        print("")
        print("THE GLC COMPLETED PROJECT CREATION")
tk.Button(r, text="create normal GLC project",bg='red',width=r.winfo_screenwidth(),command=first).pack()
class second():
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.title('GLC programming language project')
        self.root2.geometry('300x200')
        tk.Label(self.root2, text='write your programming language project path').pack()
        self.path = tk.Text(self.root2, bg='white', insertbackground='black',width=self.root2.winfo_screenwidth(),height=1, fg='black', font=("Arial", 12))
        self.path.pack()
        tk.Label(self.root2, text='write your programming language name no spaces').pack()
        self.language_name = tk.Text(self.root2, bg='white', insertbackground='black', width=self.root2.winfo_screenwidth(),
                            height=1, fg='black', font=("Arial", 12))
        self.language_name.pack()
        tk.Label(self.root2, text='write the programming language file format').pack()
        self.file_formato = tk.Text(self.root2, bg='white', insertbackground='black', width=self.root2.winfo_screenwidth(),
                            height=1, fg='black', font=("Arial", 12))
        self.file_formato.pack()
        tk.Button(self.root2, text='create it', command=self.create2).pack()
        self.root2.mainloop()

    def edit_line(self,file_name, line_number, new_text):
        """Edits the specified line in the given Python file.

        Args:
          file_name: The name of the Python file to edit.
          line_number: The number of the line to edit.
          new_text: The new text to write to the file.
        """

        with open(file_name, "r") as f:
            source_code = f.read()

        lines = source_code.split("\n")
        lines[line_number - 1] = new_text

        with open(file_name, "w") as f:
            f.write("\n".join(lines))
    def scan_folder2(self,folder_path):
        file_list = []
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_list.append(os.path.join(root, file_name))
        return file_list
    def create2(self):
        creation_location1 = self.path.get("1.0",tk.END)
        creation_location2 = self.language_name.get("1.0",tk.END)
        creation_location = creation_location1[:-1] + "\\" + creation_location2[:-1]
        file_format1 = self.file_formato.get("1.0",tk.END)
        file_format = file_format1[:-1]
        print("starting creation of GLC project[1/3]")
        os.mkdir(f"{creation_location}")
        print("project folder created")
        os.mkdir(f"{creation_location}\\GLC")
        print("GLC folder in project created")
        print("start files scanning")
        files_list2 = self.scan_folder2("GLC")
        print("files scanned")
        print("starting creation of GLC project[2/3]")
        for listnum in files_list2:
            print(f"{listnum}")
            print(f"starting {listnum} operation")
            print(f"start read the scanned {listnum}")
            var1 = open(f"{listnum}", "r")
            print(f"the scanned {listnum} reading operation ended")
            print("creating file in project")
            var2 = open(f"{creation_location}\\{listnum}", "x")
            print("creating file in project completed")
            print("starting transport the copied scanned file contained to new project file")
            var3 = open(f"{creation_location}\\{listnum}", "w")
            var3.write(var1.read())
            print("transport completed")
            print("starting closing file operations")
            var1.close()
            var2.close()
            var3.close()
            print("closing completed")
        print("starting creation of GLC project[3/3]")
        print(f"starting edit on {creation_location}\\GLC\\GLClang.py")
        self.edit_line(f'{creation_location}\\GLC\\GLClang.py',37,f'''    with open('main.{file_format}', 'r') as la2:''')
        self.edit_line(f'{creation_location}\\GLC\\GLClang.py',48,f'''    with open('main.{file_format}', 'w') as la:''')
        self.edit_line(f'{creation_location}\\GLC\\GLClang.py',56,f'''    with open('main.{file_format}', 'w') as la:''')
        self.edit_line(f'{creation_location}\\GLC\\GLClang.py',62,f'''    with open('main.{file_format}', 'w') as la:''')
        self.edit_line(f'{creation_location}\\GLC\\GLClang.py',152,f'''    oldb = open('main.{file_format}', 'w')''')
        print(f"edit of {creation_location}\\GLC\\GLClang.py completed")
        print(f"starting edit on {creation_location}\\GLC\\run_system_functions.py")
        self.edit_line(f'{creation_location}\\GLC\\run_system_functions.py',591,f'''        ma = open''' + '''(f'{file_name_without_file_format}''' + f'''.{file_format}','x')''')
        self.edit_line(f'{creation_location}\\GLC\\run_system_functions.py',632,f'''        ma = open''' + '''(f'{file_name_without_file_format}''' + f'''.{file_format}','x')''')
        print(f'creating {creation_location}\\GLC\\main.{file_format} file')
        main_filec = open(f'{creation_location}\\GLC\\main.{file_format}','x')
        main_filec.close()
        print(f'the file {creation_location}\\GLC\\main.{file_format} created')
        print(f'removing {creation_location}\\GLC\\main.gcf')
        os.remove(f'{creation_location}\\GLC\\main.gcf')
        print(f"{creation_location}\\GLC\\main.gcf got removed")
        print("")
        print("THE GLC COMPLETED PROJECT CREATION")
tk.Button(r, text="create GLC programming language project",bg='red',width=r.winfo_screenwidth(),command=second).pack()
r.mainloop()