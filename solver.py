  
""" KNAPSACK  SOLVER """
from tkinter import Menu, Button, StringVar, OptionMenu, messagebox as msg, filedialog, Tk
from file_parser import fileparser
from greedy import greedy
from item import value, Item
def helpmenu():
    """ help menu """
    msg.showinfo("Help", "A knapsack Problem solver")

def aboutmenu():
    """ about menu """
    msg.showinfo("About", "Version 1.0")

class KnapsackSolver():
    """ KNAPSACK SOLVER CLASS """
    def __init__(self, master):
        self.master = master
        self.master.title("KNAPSACK_SOLVER")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.filed = ""

        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a file",
                                   accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Solve", accelerator='Alt+F5', command=self.solve)
        self.file_menu.add_command(label="Close file", accelerator="Ctrl+F5")
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>', lambda event: self.insertfile())
        self.master.bind('<Alt-F5>', lambda event: self.solve())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        #self.master.bind('<Control-F5>', lambda event: self.cf())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())

        self.binsert = Button(self.master, text="Insert a file", command=self.insertfile)
        self.binsert.pack()

    def file_verification(self):
        """ verifies that the inserted file is a knapsack problem instance """
        if ".txt" in self.filed:
            try:
                self.solvb = Button(self.master, text="Solve", command=self.solve)
                self.solvb.pack()
                self.nofi, self.maxW, self.item, self.weight = fileparser(self.filed)
                msg.showinfo("SUCCESS",
                             "THE FILE SUCCESSFULLY INSERTED ")
            except ValueError:
                msg.showerror("ERROR", "NO KNAPSACK PROBLEM INSTANCE INSERTED")
                self.filed = ""
        else:
            msg.showerror("Error", "NO TXT FILE ADDED")

    def insertfile(self):
        """ user inserts a .txt file (problem instance ) """
        if self.filed == "":
            self.filed = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                    filetypes=(("txt files", "*.txt"),
                                                               ("all files", "*.*")))
            self.file_verification()
        else:
            msg.showerror("ERROR", "YOU NEED TO CLOSE THE FILE")
    
    def solve(self):
        listofitems = []
        for i in range(len(self.item)):
            listofitems.append(Item(int(self.item[i]), int(self.weight[i])))
        result, totalvalue = greedy(listofitems, int(self.maxW), value)
        msg.showinfo("Solution:", str(totalvalue))

    def exitmenu(self):
        """ exit """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()

def main():
    """ main function """
    root = Tk()
    KnapsackSolver(root)
    root.mainloop()
if __name__ == '__main__':
    main()