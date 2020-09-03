"""
knapsack instance generator
"""
from tkinter import Label, Text, Button, Tk, Menu
from tkinter import filedialog, END
from tkinter import messagebox as msg
import random as rd
def helpmenu():
    """ help menu """
    msg.showinfo("HELP", "HELP ")
def aboutmenu():
    """ about """
    msg.showinfo("About", "About \nVersion 1.0")
class KnapsackInstanceGenerator():
    """
    frontal face recognition class
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Knapsack Instance Generator")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Generate", accelerator='Ctrl+O', command=self.gen)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)

        self.itemleb = Label(self.master, text="Enter the number of items")
        self.itemleb.pack()
        self.itemtext = Text(self.master, height=1, width=3)
        self.itemtext.pack()

        self.maxweightleb = Label(self.master, text="Enter the max weight")
        self.maxweightleb.pack()
        self.maxweighttext = Text(self.master, height=1, width=3)
        self.maxweighttext.pack()

        self.geb = Button(self.master, text="GENERATE", command=self.gen)
        self.geb.pack()

        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-o>', lambda event: self.gen())

    def save_to_file(self, filename):
        """ saves the instance to a .txt file"""
        with open(filename, 'w') as f:
            f.write(str(self.itemtext.get(1.0, END)) +' ' + str(self.maxweighttext.get(1.0, END))+ "\n")
            for _ in range(int(self.itemtext.get(1.0, END))):
                f.write(str(rd.randint(10, 1000)) + ' ' + str(rd.randint(10, 1000)) + "\n")

    
    def gen(self):
        """ generates the instance"""
        try:
            if (int(self.itemtext.get(1.0, END)) > 1) and (int(self.maxweighttext.get(1.0, END)) > 0):
                filenamesave = filedialog.asksaveasfilename(initialdir="/",
                                                            title="Select file",
                                                            filetypes=(("txt files", "*.txt"),
                                                                       ("all files", "*.*")))
                if ".txt" in filenamesave:
                    self.save_to_file(filenamesave)
                else:
                    msg.showerror("Abort", "Abort")
            else:
                msg.showerror("Value Error", "Number of iteams must be higher than 1 and max weight must be higher than 0")
        except ValueError:
            msg.showerror("Value Error", "Number of iteams must be higher than 1 and max weight must be higher than 0")
        self.itemtext.delete(1.0, END)
        self.maxweighttext.delete(1.0, END)
        
    def exitmenu(self):
        """ exit menu"""
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    KnapsackInstanceGenerator(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()