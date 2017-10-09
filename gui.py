from tkinter import Tk, Label, Listbox, Checkbutton, Button, Entry, StringVar, Scrollbar, END, Variable
from backend import BackEnd
from printer import Printer


class GUI:

    def add_printers_command(self):
        for printer in self.checkboxes:
            if(len(self.checkboxes[printer].get()) > 0):
                #print(self.checkboxes[printer].get())
                self.lblStatus['text'] = "Installing: {}".format(self.checkboxes[printer].get())
                self.be.installPrinter(self.checkboxes[printer].get())
                self.lblStatus['text'] = "Installed: {}".format(self.checkboxes[printer].get())
            else:
                self.lblStatus['text'] = "No Printers Selected"


    def addPrinterOption(self, printer, path, grid=[]):
        #print("Add Printer Option")
        self.checkboxes[printer] = Variable()
        checkbutton = Checkbutton(self.window, text=printer, width=self.btnwidth, anchor="w", variable=self.checkboxes[printer], offvalue="", onvalue=path)
        checkbutton.grid(row=grid[0], column=grid[1])

    def on_closing(self):
        self.p.close()
        self.window.destroy()

    def __init__(self):
        self.p = Printer()


        self.btnwidth = 35
        self.be = BackEnd()
        self.printers = self.p.getPrinters()
        self.checkboxes = {}
        self.window = Tk()
        self.window.wm_title("Batch Printer Install")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        row = 0
        for printer in self.printers:
            self.addPrinterOption(printer.name, printer.path, [row, 0])
            row += 1

        row += 1
        btnAddPrinters = Button(self.window, text="Add Printers", width=self.btnwidth, command=self.add_printers_command)
        btnAddPrinters.grid(row=row, column=0, sticky='we')
        row += 1
        self.lblStatus = Label()
        self.lblStatus.grid(row=row, column=0, sticky='we')
