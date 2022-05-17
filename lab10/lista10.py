import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Logic import ProgramLogic
import tkinter.messagebox
import configparser
import os
import logging
from datetime import datetime

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
        self.parent.iconbitmap("images/virus.ico")

        # zczytanie parametrów do obiektu logic
        param_list = [
            int(domyslne['day_start']),
            int(domyslne['day_end']),
            int(domyslne['month_start']),
            int(domyslne['month_end']),
            domyslne['country'],
            domyslne['continent'],
            int(domyslne['data_select_type']),
            int(domyslne['cases_type']),
            int(domyslne['sort_type']),
            domyslne['reverse_sort_flag'],
            domyslne['total_flag'],
        ]

        ProgramLogic.set_param(param_list)

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
        self.toolbar = tk.Frame(self.parent, background='#969696')  # tworzymy ramkę toolbar, do trzymania tam narzędzi

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
        self.statusbar = tk.Label(self.parent, text="Linia statusu...", anchor=tkinter.W, background='#969696')
        # self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

    def utworz_okno_robocze(self):
        self.robocze = WorkingWindow(self.parent)
        self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, padx=10, pady=1, sticky=tk.NSEW)

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
        tk.Frame.__init__(self, master, padx=10, pady=10, bg="#a9bbdb")

        self.parent = master

        self.utworz_okno_ustawien()
        self.utworz_okno_wynikow()

        self.start_button = tk.Button(self, text="Start", padx=2, pady=2, background="#1f992f",
                                      command=self.funkcje_start_button)
        self.start_button.grid(row=1, column=0, padx=5, pady=5,
                               sticky=tk.NSEW)  # biała czcionka, mniej zielonego, całe miejsce

        self.frame_ustawien.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.frame_okno_wynikow.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=999)
        self.rowconfigure(0, weight=999)

    def utworz_okno_ustawien(self):
        self.frame_ustawien = tk.LabelFrame(self, text="Ustawienia", pady=10, padx=10)

        self.utworz_ustawienia_pola()
        self.utworz_ustawienia_check_boxy()
        self.utworz_ustawienia_radio_buttony()
        self.utworz_ustawienia_combobox()

        self.frame_pola.grid(row=1, column=0, padx=2, sticky=tk.N + tk.S + tk.W + tk.E)
        self.frame_boxy.grid(row=0, column=1, padx=2, sticky=tk.N + tk.S + tk.W + tk.E)
        self.frame_radio.grid(row=1, column=1, padx=2, sticky=tk.N + tk.S + tk.W + tk.E)
        self.frame_combobox.grid(row=0, column=0, padx=2, sticky=tk.N + tk.S + tk.W + tk.E)

    def utworz_ustawienia_pola(self):
        self.frame_pola = tk.LabelFrame(self.frame_ustawien, text="Ustaw poszczególne parametry", padx=5, pady=5)

        self.label2 = tk.Label(self.frame_pola, text="Początkowy dzień")
        self.label2.grid(column=0, row=0)
        self.label3 = tk.Label(self.frame_pola, text="Ostatni dzień")
        self.label3.grid(column=0, row=1)
        self.label4 = tk.Label(self.frame_pola, text="Początkowy miesiąc")
        self.label4.grid(column=0, row=2)
        self.label5 = tk.Label(self.frame_pola, text="Ostatni miesiąc")
        self.label5.grid(column=0, row=3)
        self.label6 = tk.Label(self.frame_pola, text="Podaj kraj")
        self.label6.grid(column=0, row=4)
        self.label7 = tk.Label(self.frame_pola, text="Podaj kontynent")
        self.label7.grid(column=0, row=5)

        # ustawianie entry_text
        self.start_day_text = tk.StringVar()
        self.start_day_text.set(ProgramLogic.day_start)
        self.end_day_text = tk.StringVar()
        self.end_day_text.set(ProgramLogic.day_end)
        self.start_month_text = tk.StringVar()
        self.start_month_text.set(ProgramLogic.month_start)
        self.end_month_text = tk.StringVar()
        self.end_month_text.set(ProgramLogic.month_end)
        self.country_text = tk.StringVar()
        self.country_text.set(ProgramLogic.country)
        self.contintent_text = tk.StringVar()
        self.contintent_text.set(ProgramLogic.continent)

        # ustawianie pol do wprowadzania
        self.start_day_entry = tk.Entry(self.frame_pola, textvariable=self.start_day_text)
        self.start_day_entry.grid(column=1, row=0)
        self.end_day_entry = tk.Entry(self.frame_pola, textvariable=self.end_day_text)
        self.end_day_entry.grid(column=1, row=1)
        self.start_month_entry = tk.Entry(self.frame_pola, textvariable=self.start_month_text)
        self.start_month_entry.grid(column=1, row=2)
        self.end_month_entry = tk.Entry(self.frame_pola, textvariable=self.end_month_text)
        self.end_month_entry.grid(column=1, row=3)
        self.country_entry = tk.Entry(self.frame_pola, textvariable=self.country_text)
        self.country_entry.grid(column=1, row=4)
        self.continent_entry = tk.Entry(self.frame_pola, textvariable=self.contintent_text)
        self.continent_entry.grid(column=1, row=5)

    def utworz_ustawienia_check_boxy(self):  # command są nie potrzebne
        self.frame_boxy = tk.LabelFrame(self.frame_ustawien, text="Zaznaczyć w razie potrzeby", padx=2, pady=2)

        self.cb1 = tk.IntVar()
        self.cb2 = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(self.frame_boxy, variable=self.cb1, text="Czy zsumować dane?", onvalue=1,
                                        offvalue=0, command=self.funkcje_boxa)
        self.checkbox1.grid(column=0, row=0)
        self.checkbox2 = tk.Checkbutton(self.frame_boxy, variable=self.cb2, text="Sortowanie odwrotne", onvalue=1,
                                        offvalue=0, command=self.funkcje_boxa)
        self.checkbox2.grid(column=0, row=1)

    def utworz_ustawienia_radio_buttony(self):
        self.frame_radio = tk.LabelFrame(self.frame_ustawien, text="Wybierz opcję", padx=2, pady=2)

        # pozwoli wybrać 1. zachorowania 2. śmierci
        self.radio_sort_label = tk.Label(self.frame_radio, text="Wybór przypadków").pack()
        self.radio_cases_var = tk.IntVar()
        self.radio_cases_var.set(1)
        self.radio_button1 = tk.Radiobutton(self.frame_radio, text='Zachorowań', variable=self.radio_cases_var,
                                            value=1).pack()
        self.radio_button2 = tk.Radiobutton(self.frame_radio, text='Śmierci', variable=self.radio_cases_var,
                                            value=2).pack()

        # pozwoli wybrać sortowanie 1. po przypadkach, 2. po dacie
        self.radio_sort_label = tk.Label(self.frame_radio, text="Wybór sortowania").pack()

        self.radio_sort_var = tk.IntVar()
        self.radio_sort_var.set(1)
        self.radio_button3 = tk.Radiobutton(self.frame_radio, text='Po Dacie', variable=self.radio_sort_var,
                                            value=1).pack()
        self.radio_button4 = tk.Radiobutton(self.frame_radio, text='Po Przypadkach', variable=self.radio_sort_var,
                                            value=2).pack()

    def utworz_ustawienia_combobox(self):
        self.frame_combobox = tk.LabelFrame(self.frame_ustawien, text="Wybierz tryb wprowadzania daty", padx=2, pady=2)

        choose_name_dic = {
            1: 'wybór daty',
            2: 'wybór miesiąca',
            3: 'wybór daty początkowej i końcowej'
        }

        self.combobox_value = tk.StringVar()
        print(type(ProgramLogic.data_select_type))
        self.combobox_value.set(choose_name_dic[ProgramLogic.data_select_type])

        self.cb = ttk.Combobox(self.frame_combobox, textvariable=self.combobox_value)

        self.cb['values'] = ['wybór daty', 'wybór miesiąca', 'wybór daty początkowej i końcowej']
        self.cb['state'] = 'readonly'
        self.cb.pack(fill=tk.BOTH)

        self.cb.bind('<<ComboboxSelected>>', self.funkcje_comboboxa)

    def utworz_okno_wynikow(self):
        self.frame_okno_wynikow = tk.LabelFrame(self, text="Wyniki", padx=2, pady=2)
        self.frame_ustawien_wynikow = tk.LabelFrame(self.frame_okno_wynikow, text="Wyniki przy poniższych ustawieniach",
                                                    padx=2, pady=2)
        self.frame_ustawien_wynikow.pack(fill=tk.X)

        self.frame_wynikow = tk.LabelFrame(self.frame_okno_wynikow, text="Właściwe wyniki", padx=2, pady=2)
        self.frame_wynikow.pack(fill=tk.X)

        self.act_time = tk.StringVar()
        self.act_time.set("czas")
        self.set_res_label1 = tk.Label(self.frame_ustawien_wynikow, textvariable=self.act_time).pack(anchor=tk.W)

        self.start_dat_res = tk.StringVar()
        self.start_dat_res.set("data początkowa")
        self.set_res_label2 = tk.Label(self.frame_ustawien_wynikow, textvariable=self.start_dat_res).pack(anchor=tk.W)

        self.end_dat_res = tk.StringVar()
        self.end_dat_res.set("data końcowa")
        self.set_res_label3 = tk.Label(self.frame_ustawien_wynikow, textvariable=self.end_dat_res).pack(anchor=tk.W)

        self.country_continent_res = tk.StringVar()
        self.country_continent_res.set("kraj,  kontynent")
        self.set_res_label4 = tk.Label(self.frame_ustawien_wynikow,
                                       textvariable=self.country_continent_res).pack(anchor=tk.W)

        self.act_set_var = tk.StringVar()
        self.act_set_var.set("Ustawienia")
        self.set_res_label5 = tk.Label(self.frame_ustawien_wynikow,
                                       textvariable=self.act_set_var).pack(anchor=tk.W)

        self.label_wynikow_data = tk.Label(self.frame_wynikow, text="liczba przypadków, data")
        self.label_wynikow_data.pack(side=tk.TOP, anchor=tk.W)

        self.t = tk.Text(self.frame_wynikow)
        self.wynik_scrollbar = tk.Scrollbar(self.frame_wynikow)

        # if jeśli sortowania odwrocone, wszystkie wyniki itp zeby wyswietlic

    def funkcje_comboboxa(self, event):
        print("COS")

        # switch z opcjamy wygaszania dat

        showinfo(
            title='Result',
            message=f'Wybierasz wybór daty przez {self.combobox_value.get()}!'
        )

    def funkcje_boxa(self):
        print('box')
        print(self.cb1.get())
        print('drop:', self.combobox_value.get())

    def funkcje_start_button(self):
        # posprawdzaj czy dobrze powprowadzane

        if not self.sprawdz_poprawnosc():
            return

        print("Dodaje param")
        param_list = [
            int(self.start_day_text.get()),
            int(self.end_day_text.get()),
            int(self.start_month_text.get()),
            int(self.end_month_text.get()),
            self.country_text.get(),
            self.contintent_text.get(),
            1,  # Data select type
            self.radio_cases_var.get(),
            self.radio_sort_var.get(),
            self.cb2.get(),
            self.cb1.get()
        ]

        ProgramLogic.set_param(param_list)
        ProgramLogic.default_steps()


        self.odswiez_okno_wynikow()
        print("Klinieto Start button")

    def sprawdz_poprawnosc(self):
        error_text = ""

        # czy data przed nie jest po dacie po
        first = int(self.start_month_text.get()) * 1000 + int(self.start_day_text.get())
        second = int(self.end_month_text.get()) * 1000 + int(self.end_day_text.get())

        print(first)
        print(second)

        if first > second:
            tkinter.messagebox.showerror("Błąd","Podana data startowa jest późniejsza od końcowej")
            return False

        # sprawdz poprawność daty
        try:
            newDate = datetime(2020, int(self.start_month_text.get()), int(self.start_day_text.get()))
        except ValueError:
            tkinter.messagebox.showerror("Błąd", "Podana data startowa jest nieprawidłowa")
            return False

        try:
            newDate = datetime(2020, int(self.end_month_text.get()), int(self.end_day_text.get()))
        except ValueError:
            tkinter.messagebox.showerror("Błąd", "Podana data końcowa jest nieprawidłowa")
            return False

        # czy dany kraj jest na danym kontynencie
        if not ProgramLogic.check_country_and_continent(self.country_text.get(), self.contintent_text.get()):
            tkinter.messagebox.showerror("Błąd", "Danego kraju nie ma na danym Kontynencie")
            return False




        return True

    def odswiez_okno_wynikow(self):
        # usun poprzednie okno
        self.t.destroy()
        self.wynik_scrollbar.destroy()

        # zakutalizuj ustawienia
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.act_time.set("czas wykonania: " + current_time)
        self.start_dat_res.set("Data początkowa: "
                               + self.start_day_text.get() + '.' + self.start_month_text.get() + '.2020')
        self.end_dat_res.set("Data końcowa: "
                             + self.end_day_text.get() + '.' + self.end_month_text.get() + '.2020')
        self.country_continent_res.set(
            "Kraj: " + self.country_text.get() + ", Kontynent: " + self.contintent_text.get())
        # self.country_continent_res.set("Kontynent: " + self.contintent_text.get())

        act_set = "Zastowano ustawienia: "

        if ProgramLogic.cases_type == 1:
            act_set += "Przypadki zachorowań, "
        else:
            act_set += "Przypadki śmierci, "

        if ProgramLogic.sort_type == 1:
            act_set += "Sortowanie po datach"
        else:
            act_set += "Sortowanie po przypadkach"

        if ProgramLogic.reverse_sort_flag:
            act_set += ", Sortowanie odwrotne"

        self.act_set_var.set(act_set)

        self.wynik_scrollbar = tk.Scrollbar(self.frame_wynikow)
        self.wynik_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.t = tk.Text(self.frame_wynikow, wrap=tk.NONE,
                    yscrollcommand=self.wynik_scrollbar.set)

        self.t.pack(fill=tk.BOTH)

        for el in ProgramLogic.covid_list:
            if ProgramLogic.cases_type == 1:
                text = "{:10d}".format(el[4]) + ", " + "{:02d}".format(el[0]) + "." + "{:02d}".format(el[1]) + ".2020"
            else:
                text = "{:10d}".format(el[5]) + ", " + "{:02d}".format(el[0]) + "." + "{:02d}".format(el[1]) + ".2020"
            self.t.insert(tk.END, text + "\n")



        self.wynik_scrollbar.config(command=self.t.yview)

        self.t['state'] = tk.DISABLED


def logger():
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def tworz_configfile():
    if not os.path.isfile(CONFIG_FILE):
        print("Nie znaleziono pliku konfiguracyjnego, tworzę plik ini")
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'size_x': 1000,
                             'size_y': 800,
                             'bazowa_geometria': '1000x800+50+50',
                             'day_start': 1,
                             'month_start': 1,
                             'year_start': 2020,
                             'day_end': 31,
                             'month_end': 12,
                             'year_end': 2020,
                             'country': 'Poland',
                             'continent': 'Europe',
                             'data_select_type': 1,
                             'cases_type': 1,
                             'sort_type': 1,
                             'reverse_sort_flag': False,
                             'total_flag': False,
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
    app.mainloop()

    # dodaj opcję sumowania
    # niech przyciski i menu coś robią
    # na dole pasek niech coś wyświetla
    # jak styknie czasu dodać sprawdzanie kraju
    # i oczywiście sprawdzanie ścieżek, może być ważne, ścieżka ini, covidowa z info,
    # wyszarzanie pól po wybraniu comboboxa
