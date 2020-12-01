  
""" KNAPSACK  SOLVER """
from tkinter import Menu, Button, StringVar, OptionMenu, messagebox as msg, filedialog, Tk
from file_parser import fileparser
from greedy import greedy
from item import value, Item, density, weightInverse
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
        self.solution = {}
        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a file",
                                   accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Solve", accelerator='Alt+F5', command=self.solve)
        self.file_menu.add_command(label="Close file", accelerator="Ctrl+F5", command=self.cf)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show Solution", accelerator='Ctrl+F4', command=self.show_solution)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-F4>', lambda event: self.show_solution())
        self.master.bind('<Control-o>', lambda event: self.insertfile())
        self.master.bind('<Alt-F5>', lambda event: self.solve())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F5>', lambda event: self.cf())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())

        self.binsert = Button(self.master, text="Insert a file", command=self.insertfile)
        self.binsert.pack()

        setslist = list(["WeightInverse", "Density", "Value"])
        self.varnumset = StringVar(master)
        self.varnumset.set(setslist[0])
        self.popupsetmenu = OptionMenu(self.master, self.varnumset, *setslist)
        self.popupsetmenu.pack()
    
    
    def cf(self):
        """ closes the .txt file """
        if self.filed == "":
            msg.showerror("ERROR", "NO FILE IMPORTED TO CLOSE")
        else:
            self.filed = ""
            self.solvb.forget()
            msg.showinfo("SUCCESS", "FILE CLOSED")
    def file_verification_gui(self):
        """ inserted gui after verification """
        self.solvb = Button(self.master, text="Solve", command=self.solve)
        self.solvb.pack()

    def file_verification(self):
        """ verifies that the inserted file is a knapsack problem instance """
        if ".txt" in self.filed:
            try:
                self.solution = {}
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
    
    def show_solution(self):
        if self.solution == {}:
            msg.showerror("Error", "THERE IS NO AVAILABLE SOLUTION.\n USE THE SOLVE BUTTON")
        else:
            msg.showinfo("Solution", "Value:"+ str(self.solution.get("Value")) + "Items"+ str(self.solution.get("Items")))



    def solve(self):
        if self.filed == "":
            msg.showerror("ERROR", "NO KNAPSACK PROBLEM INSTANCE INSERTED")
        else:
            listofitems = []
            for i in range(len(self.item)):
                listofitems.append(Item(str(self.item[i]),float(self.item[i]), float(self.weight[i])))
            if self.varnumset.get() == "Value":
                result, totalvalue = greedy(listofitems, int(self.maxW), value)
            elif self.varnumset.get() == "Density":
                result, totalvalue = greedy(listofitems, int(self.maxW), density)
            else:
                result, totalvalue = greedy(listofitems, int(self.maxW), weightInverse)
            self.solution.update({"Value":totalvalue,"Items":str([i.getName() for i in result])})
            msg.showinfo("Solution:", "Value:"+str(totalvalue)+"\n Items:"+str([i.getName() for i in result]))
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