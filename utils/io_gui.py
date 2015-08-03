import tkinter as tk
import tkinter.filedialog as filedialog

class IO_GUI(tk.Frame):
    def __init__(self,io_function,master=None,title="IO_GUI"):
        master.title = title
        tk.Frame.__init__(self,master)
        self.io_function = io_function
        self.input_file = None
        self.output_file = None
        self.pack()
        self.addButtons()
    def addButtons(self):
        self.input_but = tk.Button(self)
        self.input_but["text"] = "Choose input."
        self.input_but["command"] = self.get_input_file
        self.input_but.pack(side="left")

        self.output_but = tk.Button(self)
        self.output_but["text"] = "Choose output directory."
        self.output_but["command"] = self.get_output_dir
        self.output_but.pack(side="right")

        self.run_but = tk.Button(self)
        self.run_but["text"] = "CLEAN ADDRESSES."
        self.run_but["command"] = self.run_code
        self.run_but["fg"] = "green"
        self.run_but.pack(side="bottom")

        self.QUIT = tk.Button(self, text="CANCEL",fg="red",command=self.master.destroy)
        self.QUIT.pack(side="bottom")

    def get_input_file(self):
        self.input_file = filedialog.askopenfilename()

    def get_output_dir(self):
        self.output_file = filedialog.askdirectory()

    def run_code(self):
        self.io_function(self.input_file,self.output_file)
