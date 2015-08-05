import tidyaddr.utils
import tkinter
root = tkinter.Tk()
def io_test(input,output):
    print("input" + input)
    print("output" + output)
g = tidyaddr.utils.IO_GUI(io_function=io_test,master=root)
g.mainloop()
