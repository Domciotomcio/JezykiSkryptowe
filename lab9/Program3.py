import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = u"Dzień dobry\n(Kliknij mnie)"
        self.hi_there["command"] = self.say_hi # co wykonać: nazwa funkcji
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy) # inny sposób wiązania
        self.quit.pack(side="bottom")

    def say_hi(self):
        print(u"Witajcie, moi drodzy studenci!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
