import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from plistmaker import make_plist


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.open_file_button = tk.Button(self)
        self.open_file_button["command"] = self.open_file
        self.open_file_button["text"] = "OPEN EXCELL"
        self.open_file_button["bg"] = "black"
        self.open_file_button.pack(side="top")

        self.label = tk.Label(self)
        self.label["text"] = "Select your excel file"
        self.label.pack(side="bottom")


    def open_file(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select Excel file",
                                                   filetypes=(("files", "*.xls"), ("files", "*.xlsx"), ("all files", "*.*")))
        set = str(root.filename).split("/")
        set.pop()
        finalDir = ""
        for i in set:
            finalDir += "/" + str(i)

        finalDir += "/"

        f = open("{}your-plist.plist".format(finalDir), "w+")
        f.write(make_plist(root.filename))

        messagebox.showinfo("Plist Maker", "Done! Your plist file near of excel file")



root = tk.Tk()
root.title("Excel to .plist converter")
app = Application(master=root)
app.mainloop()