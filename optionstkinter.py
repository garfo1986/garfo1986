import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Checkbutton en tkinter")
        
        self.checkbox = ttk.Checkbutton(self, text="Opción 1")
        self.checkbox.place(x=40, y=70)
        
        self.place(width=300, height=200)

        self.checkbox2 = ttk.Checkbutton(self, text="Opción 2")
        self.checkbox2.place(x=40, y=100)
        
        self.place(width=300, height=200)

        self.checkbox3 = ttk.Checkbutton(self, text="Opción 3")
        self.checkbox3.place(x=40, y=130)
        
        self.place(width=300, height=200)
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()