"""
knapsack instance generator
"""
from tkinter import Label, Text, Button, Tk, Menu, IntVar, Radiobutton
from tkinter import filedialog, END
from tkinter import simpledialog
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
    
    def gen(self):
        pass
        
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