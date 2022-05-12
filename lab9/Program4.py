import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.pokaz_var = tk.StringVar()
        self.pokaz_var.set("wartość początkowa")
        self.pokaz = tk.Label(self, textvariable=self.pokaz_var, relief=tk.RAISED)
        self.pokaz.pack()
        self.enter_var = tk.StringVar()
        self.enter_var.set("?")
        self.enter = tk.Label(self, textvariable=self.enter_var, relief=tk.SUNKEN)
        self.enter.pack()
        self.wprowadz = tk.Entry()
        self.wprowadz.pack()
        # inny sposób przypisania
        self.wprowadz["textvariable"] = self.pokaz_var
        # dowiązanie funkcji do obsługi nowej linii
        self.wprowadz.bind('<Key-Return>',
                           self.pokaz_zawartosc)

    def pokaz_zawartosc(self, event):
        self.enter_var.set(self.pokaz_var.get())


if __name__ == '__main__':
    mp = App()
    mp.mainloop()
