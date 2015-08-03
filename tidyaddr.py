import tkinter

from tidycsv.utils.address.cleaning import cleanaddress
from tidycsv.utils.io_gui import IO_GUI

root = tkinter.Tk()
g = IO_GUI(io_function=cleanaddress,master=root)
g.mainloop()