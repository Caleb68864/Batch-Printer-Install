import os


class BackEnd:

    def removePrinter(self, printer):
        remove = 'rundll32 printui.dll,PrintUIEntry /dn /n {} /q'
        os.system(remove.format(printer))

    def installPrinter(self, printer):
        self.removePrinter(printer)
        add = 'rundll32 printui.dll,PrintUIEntry /in /n {}'
        os.system(add.format(printer))
