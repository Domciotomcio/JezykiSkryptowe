import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Logic import ProgramLogic
import tkinter.messagebox
import configparser
import os
import logging

dane_konfig = "c:/Python/tc.txt"

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.ini")


class MainFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # pliki konfiguracyjne
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE, "UTF8")

        # ustawienie rodzica
        self.parent = master
        # dzięki temu przy zamknięciu okna przez X w prawym górnym rogu program wykona funkcję file_quit
        self.parent.protocol("WM_DELETE_WINDOW", self.file_quit)

        # obiekt ProgramLogic do obsługi logiki programu
        self.logic = ProgramLogic()

        # domyślne wartosci zczytane z configa
        self.zczytaj_configa()

        # tworzenie menu
        self.utworz_bazowe_menu()
        self.dodaj_menu_file()
        self.dodaj_menu_help()

        self.utworz_pasek_narzedzi()
        self.utworz_status()
        self.utworz_okno_robocze()

        # wagi kolumn i wierszy pozwalają na odpowiedni rozmiar odpowienich ramek w środku
        self.parent.columnconfigure(0, weight=999)
        self.parent.columnconfigure(1, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=9999)
        self.parent.rowconfigure(2, weight=1)

    def zczytaj_configa(self):
        domyslne = self.config["DEFAULT"]
        self.geometria_baza = domyslne['bazowa_geometria']
        self.parent.geometry(self.geometria_baza)  # geometria
        self.parent.title(domyslne['glowna_nazwa'])
        # potem może dodaj lepszą ścieżkę
        self.parent.iconbitmap("images/virus.ico")

    def utworz_bazowe_menu(self):
        self.menubar = tk.Menu(self.parent)  # stwórz widget menubar klasy Menu
        self.parent["menu"] = self.menubar  # atrybut "menu" u rodzica ustawiamy na nasze menu

    # poszczególne listy menu w menu
    def dodaj_menu_file(self):
        file_menu = tk.Menu(self.menubar, tearoff=0)  # tearoff decyduje, czy można oddzielić menu
        for label, command, shortcut_text, shortcut in (
                ("New...", self.file_new, "Ctrl+N", "<Control-n>"),
                ("Open...", self.file_open, "Ctrl+O", "<Control-o>"),
                ("Save", self.file_save, "Ctrl+S", "<Control-s>"),
                (None, None, None, None),
                ("Quit", self.file_quit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                file_menu.add_separator()
            else:
                file_menu.add_command(label=label, underline=0,
                                      command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="File", menu=file_menu, underline=0)

    def dodaj_menu_help(self):
        fileMenu = tk.Menu(self.menubar, tearoff=0)
        for label, command, shortcut_text, shortcut in (
                ("New...", self.file_new, "Ctrl+N", "<Control-n>"),
                ("Open...", self.file_open, "Ctrl+O", "<Control-o>"),
                ("Save", self.file_save, "Ctrl+S", "<Control-s>"),
                (None, None, None, None),
                ("Quit", self.file_quit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                                     command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Help", menu=fileMenu, underline=0)

    def utworz_pasek_narzedzi(self):
        self.toolbar_images = []  # obrazki toolbara, muszą być pamiętane stale
        self.toolbar = tk.Frame(self.parent, background='#2f47fa')  # tworzymy ramkę toolbar, do trzymania tam narzędzi

        # ta pętla przedzie po podanej liście ikonek z ich funkcjami i wykona dla nich wszystkie określone niżej zadania
        # lista z warunku pętli pozwala łatwo dodawać ikonki (ich ścieżkę) wraz z funkcją którą będą wywoływać
        # Kolejność ma znaczenie, bo w takiej będziemy dodawać do paska narzędzi
        for image, command in (
                ("images/editdelete.gif", self.file_usun),
                ("images/filenew.gif", self.file_new),
                ("images/fileopen.gif", self.file_open),
                ("images/filesave.gif", self.file_save)):

            # najpierw stworzenie absolutnej ścieżki dla naszych obrazków
            image = os.path.join(os.path.dirname(__file__), image)

            try:
                # stwórz obiekt klasy tk.PhotoImage z obrazkiem i dodaj go do listy naszych obrazków self.toolbar_images
                image = tk.PhotoImage(file=image)
                self.toolbar_images.append(image)

                # teraz przycisk z naszym obrazkiem
                button = tk.Button(self.toolbar, image=image, command=command)

                # przyciski dodajemy po kolei w formie siatki, w zerowym rzędzie i
                # w następnej kolumnie (tutaj dł listy obrazków - 1, bo dodajemy na ostatniej pozycji)
                button.grid(row=0, column=len(self.toolbar_images) - 1)  # KOLEJNE ELEMENTY
            except tkinter.TclError as err:
                print(err)  # gdy kłopoty z odczytaniem pliku

        # na koniec pozostaje dodanie toolbara do naszej głównej ramki, sticky rozciągnie na całej dostępnej przestrzeni
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

    def utworz_status(self):
        self.statusbar = tk.Label(self.parent, text="Linia statusu...", anchor=tkinter.W)
        # self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

    def utworz_okno_robocze(self):
        self.robocze = WorkingWindow(self.parent)
        self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, padx=3, pady=3, sticky=tk.NSEW)

        # self.robocze = tk.Frame(self.parent, background='#00704A')

        # label_frame = tk.LabelFrame(self.robocze, )

        # self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=tk.NSEW)

    # Mogą się przydać, na razie nie najważniejsze
    def file_quit(self, event=None):
        # Świetny sposób na upewnienie się, czy ktoś chce zakończyć działanie programu
        # potem można się upewniać o zapis pliku itd.
        reply = tkinter.messagebox.askyesno(
            "Potwierdź wyjście",
            "Czy na pewno chcesz wyjść?", parent=self.parent)

        event = event

        if reply:  # jeśli faktycznie kończy to reply = True
            geometria = self.parent.winfo_geometry()
            print(type(geometria))
            self.config["DEFAULT"]["bazowa_geometria"] = geometria
            with open(CONFIG_FILE, 'w') as konfig_plik:
                self.config.write(konfig_plik)
            self.parent.destroy()

    def file_new(self, event=None):
        event = event

    def file_open(self, event=None):
        event = event

    def file_save(self, event=None):
        event = event

    def file_usun(self):
        print("FILE_USUN")

    def ustawStatusBar(self, txt):
        self.statusbar["text"] = txt

    def clearStatusBar(self):
        self.statusbar["text"] = ""


class WorkingWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, padx=10, pady=10, background='#529ff7')

        self.parent = master

        self.utworz_okno_ustawien()
        self.utworz_okno_wynikow()

    def utworz_okno_ustawien(self):
        self.frame_ustawien = tk.LabelFrame(self, text="Ustawienia", padx=2, pady=2, background='#ffffff')

        self.utworz_ustawienia_pola()
        self.utworz_ustawienia_check_boxy()
        self.utworz_ustawienia_radio_buttony()
        self.utworz_ustawienia_combobox()
        self.start_button = tk.Button(self.frame_ustawien, text="Start", padx=2, pady=2, background="green")

        self.frame_pola.grid(row=0, column=0, rowspan=2)
        self.frame_boxy.grid(row=0, column=1)
        self.frame_radio.grid(row=1, column=1)
        self.frame_combobox.grid(row=2, column=0, columnspan=1)
        self.start_button.grid(row=2, column=1)  # biała czcionka, mniej zielonego, całe miejsce

        self.frame_ustawien.grid(row=0, column=0)

    def utworz_ustawienia_pola(self):
        self.frame_pola = tk.LabelFrame(self.frame_ustawien, text="Ustawienia pola", padx=2, pady=2,
                                        background='#ffffff')

        self.label1 = tk.Label(self.frame_pola, text="selekcja zakresu dat")
        self.label1.grid(column=0, row=0)
        self.label2 = tk.Label(self.frame_pola, text="Początkowy dzień")
        self.label2.grid(column=0, row=1)
        self.label3 = tk.Label(self.frame_pola, text="Ostatni dzień")
        self.label3.grid(column=0, row=2)
        self.label4 = tk.Label(self.frame_pola, text="Początkowy miesiąc")
        self.label4.grid(column=0, row=3)
        self.label5 = tk.Label(self.frame_pola, text="Ostatni miesiąc")
        self.label5.grid(column=0, row=4)
        self.label6 = tk.Label(self.frame_pola, text="Podaj kraj")
        self.label6.grid(column=0, row=5)
        self.label7 = tk.Label(self.frame_pola, text="Podaj kontynent")
        self.label7.grid(column=0, row=6)

        # ustawianie entry_text
        self.entry_text1 = tk.StringVar()
        self.entry_text1.set("tekst1")
        self.entry_text2 = tk.StringVar()
        self.entry_text2.set("tekst2")
        self.entry_text3 = tk.StringVar()
        self.entry_text3.set("tekst3")
        self.entry_text4 = tk.StringVar()
        self.entry_text4.set("tekst4")
        self.entry_text5 = tk.StringVar()
        self.entry_text5.set("tekst5")
        self.entry_text6 = tk.StringVar()
        self.entry_text6.set("tekst6")

        # ustawianie pol do wprowadzania
        self.start_day_entry = tk.Entry(self.frame_pola, textvariable=self.entry_text1)
        self.start_day_entry.grid(column=1, row=0)
        self.end_day_entry = tk.Entry(self.frame_pola, textvariable=self.entry_text2)
        self.end_day_entry.grid(column=1, row=1)
        self.start_month_entry = tk.Entry(self.frame_pola, textvariable=self.entry_text3)
        self.start_month_entry.grid(column=1, row=2)
        self.end_month_entry = tk.Entry(self.frame_pola, textvariable=self.entry_text4)
        self.end_month_entry.grid(column=1, row=3)
        self.country_entry = tk.Entry(self.frame_pola, textvariable=self.entry_text5)
        self.country_entry.grid(column=1, row=4)
        self.continent_entry = tk.Entry(self.frame_pola, textvariable=self.entry_text6)
        self.continent_entry.grid(column=1, row=5)

    def utworz_ustawienia_check_boxy(self):  # command są nie potrzebne
        self.frame_boxy = tk.LabelFrame(self.frame_ustawien, text="Ustawienia boxow", padx=2, pady=2,
                                        background='#ffffff')

        self.cb1 = tk.IntVar()
        self.cb2 = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(self.frame_boxy, variable=self.cb1, text="Czy sortować po dacie?", onvalue=1, offvalue=0, command=self.funkcje_boxa)
        self.checkbox1.grid(column=0, row=0)
        self.checkbox2 = tk.Checkbutton(self.frame_boxy, variable=self.cb2, text="Sortowanie odwrotne", onvalue=1, offvalue=0, command=self.funkcje_boxa)
        self.checkbox2.grid(column=0, row=1)

        self.var_cases_deaths = tk.IntVar()
        self.checkbox3 = tk.Checkbutton(self.frame_boxy, variable=self.var_cases_deaths, text="Wybierz zachorowania", onvalue=1, offvalue=0, command=self.funkcje_boxa)
        self.checkbox3.grid(column=0, row=2)

    def utworz_ustawienia_radio_buttony(self):
        self.frame_radio = tk.LabelFrame(self.frame_ustawien, text="Ustawienia radio buttonow", padx=2, pady=2, background='#ffffff')

        # pozwoli wybrać 1. zachorowania 2. śmierci
        self.zmienna_radiowa = tk.IntVar()
        self.zmienna_radiowa.set(1)
        self.radio_button1 = tk.Radiobutton(self.frame_radio, text='Zachorowania', variable=self.zmienna_radiowa,
                                            value=1).pack()
        self.radio_button2 = tk.Radiobutton(self.frame_radio, text='Śmierci', variable=self.zmienna_radiowa,
                                            value=2).pack()

    def utworz_ustawienia_combobox(self):
        self.frame_combobox = tk.LabelFrame(self.frame_ustawien, text="Ustawienia comboxow", padx=2, pady=2, background='#ffffff')

        self.combobox_value = tk.StringVar()
        self.combobox_value.set("wybór daty")

        self.cb = ttk.Combobox(self.frame_combobox, textvariable=self.combobox_value)

        self.cb['values'] = ['wybór daty', 'wybór miesiąca', 'wybór daty początkowej i końcowej']
        self.cb['state'] = 'readonly'
        self.cb.pack()

        self.cb.bind('<<ComboboxSelected>>', self.funkcje_comboboxa)

    def utworz_okno_wynikow(self):
        self.frame_wynikow = tk.LabelFrame(self, text="Wyniki", padx=2, pady=2, background='#ffffff')
        self.l1 = tk.Label(self.frame_wynikow, text="TEAXT").pack()

        self.frame_wynikow.grid(row=0, column=1)




    def funkcje_comboboxa(self, event):
        print("COS")

        #switch z opcjamy wygaszania dat

        showinfo(
           title='Result',
           message=f'Wybierasz wybór daty przez {self.combobox_value.get()}!'
        )

    def funkcje_boxa(self):
        print('box')
        print(self.cb1.get())
        print('drop:', self.combobox_value.get())


def logger():
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def tworz_configfile():
    print(os.path.isfile(CONFIG_FILE))

    if not os.path.isfile(CONFIG_FILE):
        print("tworzę plik ini")
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'size_x': 1000,
                             'size_y': 800,
                             'bazowa_geometria': '1000x800+50+50',
                             'glowna_nazwa': "Coronavirus Program"}
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
    else:
        print("*.ini już istnieje")


if __name__ == '__main__':
    logger()
    tworz_configfile()

    root = tk.Tk()
    app = MainFrame(master=root)
    # app = WorkingWindow(master=root)
    app.mainloop()
