'''
Created on 2021-05-18

@author: Andrzej
'''

import tkinter as tk
from tkinter import filedialog
import os

from lab10.szablon_gui import BazoweGui
from appls.exif_jpg import Exif_dane
from tkinter.constants import DISABLED, NORMAL

ident = "snaps"
to_check_id = "selected_pictures"
to_show_id = "pictures_2_view"


class Muster_Obraz(BazoweGui):
    pass

    def start_pracy(self):
        self.__view_mode = True
        self.to_check = []  # all input snaps
        self.to_show = []  # selected snaps
        self.to_display = []  # what is on the screen
        self.set_pictures2check()
        self.snap_no = -1;
        self.view_button = None
        self.uzupelnij_toolbar()
        self.parent.bind("<Configure>", self.zmiana_rozmiaru)
        nazwa_start = self.konfig["DEFAULT"]["icons"] + "images/" + self.konfig[ident]["obraz_start"]
        self.do_pokazania = Exif_dane(nazwa_start)
        self.obrazBt = tk.Button(self.robocze, text="start")
        self.obrazBt.pack(fill=tk.Y)
        self.stary_rozmiar = (10, 10)
        pass

    def uzupelnij_toolbar(self):
        for image, command in (
                (self.icons + "images/browser.png", self.show_map),
                (self.icons + "images/larrow.gif", self.to_left),
                (self.icons + "images/rarrow.gif", self.to_right),
                (self.icons + "images/uarrow.gif", self.to_top)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tk.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tk.Button(self.toolbar, image=image,
                                   command=command)
                button.grid(row=0, column=len(self.toolbar_images) - 1)  # KOLEJNE ELEMENTY
            except tk.TclError as err:
                print(err)  # gdy kłopoty z odczytaniem pliku
        self.toolbar_size = len(self.toolbar_images)
        self.store_button = tk.Button(self.toolbar, text="Zapamiętaj", command=self.store_snap)
        self.store_button.grid(row=0, column=self.toolbar_size)
        self.toolbar_size += 1
        self.view_button = tk.Button(self.toolbar, text="Selekcja", command=self.change_mode)
        self.change_mode()
        self.view_button.grid(row=0, column=self.toolbar_size)
        self.toolbar_size += 1
        pass

    def store_snap(self):
        if self.snap_no < 0:
            self.ustawStatusBar("brak zdjęć do zapamiętania")
            return
        file_name = self.to_display[self.snap_no]
        if file_name in self.to_show:
            self.ustawStatusBar("już to mam " + file_name)
            return
        self.to_show.append(file_name)
        pass

    def to_left(self):
        test = self.snap_no - 1
        if not self.set_snap_no(test):
            return
        self.dispay_snap()
        pass

    def to_right(self):
        test = self.snap_no + 1
        if not self.set_snap_no(test):
            return
        self.dispay_snap()
        pass

    def to_top(self):
        if not self.set_snap_no(0):
            return
        self.dispay_snap()
        pass

    def set_snap_no(self, wanted):
        if len(self.to_display) == 0:
            self.ustawStatusBar("brak zdjęć do pokazania")
            return False
        if wanted >= 0 and wanted < len(self.to_display):
            self.snap_no = wanted
            return True
        if wanted < 0:
            self.snap_no = len(self.to_display) - 1
            return True
        if wanted >= len(self.to_display):
            self.snap_no = 0
        return True

    def dispay_snap(self):
        file_name = self.to_display[self.snap_no]
        try:
            self.do_pokazania = Exif_dane(file_name)
            self.obrazBt.config(image=self.test_image)
            self.zmiana_rozmiaru(None, False)
            msg = "%s %s (%d/%d)" % (self.do_pokazania, file_name, self.snap_no + 1, len(self.to_display))
            self.ustawStatusBar(msg)
        except:
            self.ustawStatusBar("problem z plikiem: " + file_name)
            return
        pass

    def change_mode(self):
        if not self.view_button:
            return
        self.__view_mode = not self.__view_mode
        self.snap_no = 0
        if self.__view_mode:
            self.view_button.configure(bg="blue", fg="yellow", text="Przegląd")
            self.store_button['state'] = DISABLED
            self.to_display = self.to_show
        else:
            self.view_button.configure(fg="red", bg="yellow", text="Selekcja")
            self.store_button['state'] = NORMAL
            self.to_display = self.to_check
        if len(self.to_display) == 0:
            self.snap_no = -1
        else:
            self.snap_no = 0
        pass

    def zmiana_rozmiaru(self, event, test_size=True):
        event = event
        geometria = self.robocze.winfo_geometry()
        if geometria == "1x1+0+0":
            return
        rozmiar = self.do_pokazania.get_size(self.robocze)
        roznica = rozmiar[0] + rozmiar[1] - self.stary_rozmiar[0] - self.stary_rozmiar[1]
        if abs(roznica) < 6 and test_size:
            return
        self.stary_rozmiar = rozmiar
        self.test_image = self.do_pokazania.ustaw_rozmiar(rozmiar)
        self.obrazBt.config(image=self.test_image)
        pass

    def file_new(self, event=None):
        event = event
        my_filetypes = [('pictures', '.tst')]
        folder2check = self.konfig.get(ident, "ini_save_dir", fallback=None)
        if not folder2check:
            return
        answer = filedialog.askopenfilename(parent=self.parent,
                                            initialdir=folder2check,
                                            title="Please select show:",
                                            filetypes=my_filetypes)
        if not answer:
            return
        with open(answer, 'r') as infile:
            fname = infile.read()
            self.to_show.append(fname)
        self.ustawStatusBar("wczytano selekcję: " + answer)
        pass

    def file_save(self, event=None):
        event = event  # filedialog.asksaveasfilename(
        my_filetypes = [('custom_save', '.tst')]
        folder2check = self.konfig.get(ident, "ini_save_dir", fallback=None)
        if not folder2check:
            return
        answer = filedialog.asksaveasfilename(parent=self.parent,
                                              initialdir=folder2check,
                                              title="Please select a file:",
                                              filetypes=my_filetypes)
        if not answer:
            return
        with open(answer, 'w') as outfile:
            for fname in self.to_show:
                outfile.write(fname)
        self.ustawStatusBar("zapisano selekcję: " + answer)
        pass

    def file_open(self, event=None):
        my_filetypes = [('pictures', '.jpg')]
        folder2check = self.konfig.get(ident, "ini_check_dir", fallback=None)
        if not folder2check:
            return
        answer = filedialog.askopenfilename(parent=self.parent,
                                            initialdir=folder2check,
                                            title="Please select a file:",
                                            filetypes=my_filetypes)
        nk = os.path.split(answer)
        answer = nk[0]
        print(answer)
        self.konfig.set(ident, "ini_check_dir", answer)
        self.set_pictures2check()
        event = event
        pass

    def show_map(self):
        if not self.do_pokazania.drawMap():
            self.ustawStatusBar("brak danych geo lokalizacji")
        pass

    def set_pictures2check(self):
        self.to_check = []
        if not self.konfig.has_section(ident):
            self.konfig.add_section(ident)
        folder2check = self.konfig.get(ident, "ini_check_dir", fallback=None)
        if not folder2check:
            self.ustawStatusBar("Brak folderu:", folder2check)
            return
        for root, dirs, files in os.walk(folder2check, topdown=True):
            dirs = dirs
            for nazwa in files:
                file_name = os.path.join(root, nazwa)
                nk = os.path.split(file_name)
                if not nk[1].upper().endswith(".JPG"):
                    continue
                file_name = os.path.normpath(file_name)
                self.to_check.append(file_name)
        self.ustawStatusBar("%s %d" % ("Liczba wpisanych plików", len(self.to_check)))
        self.to_display = self.to_check
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = Muster_Obraz(root)
    app.start_pracy()
    app.mainloop()
    pass