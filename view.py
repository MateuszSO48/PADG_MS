from tkinter import *
from tkinter import ttk, messagebox
import tkintermapview
import controller

root = Tk()
root.title("System zarządziania siecią portów")
root.geometry("1200x760")

aktualny_tryb = "Porty"
pola_formularza= {}

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)


ramka_przyciski = Frame(root)
ramka_formularz = Frame(root)
ramka_funkcjonalnosci = Frame(root)
ramka_lista = Frame(root)
ramka_mapa = Frame(root)


ramka_przyciski.grid(row=0, column=0, sticky='ew', padx=10, pady=5)
ramka_formularz.grid(row=1, column=0, sticky='ew', padx=10, pady=5)
ramka_funkcjonalnosci.grid(row=2, column=0, sticky='ew', padx=10, pady=5)
ramka_lista.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
ramka_mapa.grid(row=0, column=1, rowspan=4, sticky='nsew')


def stworz_pole(tekst, klucz, rzad):
    Label(ramka_formularz, text=tekst).grid(row=rzad, column=0, sticky='w')
    pole = Entry(ramka_formularz)
    pole.grid(row=rzad, column=1, sticky='w')
    pola_formularza[klucz] = pole


def pobieranie_pola():
    return {klucz: pole.get() for klucz, pole in pola_formularza.items()}


def wyczysc_pola():
    for pole in pola_formularza.values():
        pole.delete(0, END)

def aktualizuj_filtr():
    lista_miast = ["Wszystkie"] + controller.get_port_names()
    listbox_filtrowanie['values'] = lista_miast
    listbox_filtrowanie.current = lista_miast[0]


def zmien_tryb(nowy_tryb):
    global aktualny_tryb
    aktualny_tryb = nowy_tryb

    for widget in ramka_formularz.winfo_children():
        widget.destroy()

    pola_formularza.clear()

    Label(ramka_formularz, text=f"Formularz: {nowy_tryb}").grid(row=0, column=0, columnspan=2)

    if nowy_tryb == "Porty":
        Label(ramka_formularz, text="Lokalizacja: ").grid(row=1, column=0, sticky='w')
        entry_loc = Entry(ramka_formularz)
        entry_loc.grid(row=1, column=1, sticky='ew')
        pola_formularza['port_location'] = entry_loc

        Label(ramka_formularz, text="Liczba miejsc : ").grid(row=2, column=0, sticky='w')
        entry_docks = Entry(ramka_formularz)
        entry_docks.grid(row=2, column=1, sticky='ew')
        pola_formularza['docks'] = entry_docks

        Label(ramka_formularz, text="Opis: ").grid(row=3, column=0, sticky='w')
        entry_opis = Entry(ramka_formularz)
        entry_opis.grid(row=3, column=1, sticky='ew')
        pola_formularza['description'] = entry_opis

    elif nowy_tryb == "Pracownicy":
        Label(ramka_formularz, text="Imię: ").grid(row=1, column=0, sticky='w')
        entry_imie = Entry(ramka_formularz)
        entry_imie.grid(row=1, column=1, sticky='ew')
        pola_formularza['imie'] = entry_imie

        Label(ramka_formularz, text="Nazwisko: ").grid(row=2, column=0, sticky='w')
        entry_nazwisko = Entry(ramka_formularz)
        entry_nazwisko.grid(row=2, column=1, sticky='ew')
        pola_formularza['nazwisko'] = entry_nazwisko

        Label(ramka_formularz, text="Pensja: ").grid(row=3, column=0, sticky='w')
        entry_pensja = Entry(ramka_formularz)
        entry_pensja.grid(row=3, column=1, sticky='ew')
        pola_formularza['pensja'] = entry_pensja

        Label(ramka_formularz, text="Miejsce pracy: ").grid(row=4, column=0, sticky='w')
        entry_work = Entry(ramka_formularz)
        entry_work.grid(row=4, column=1, sticky='ew')
        pola_formularza['work_location'] = entry_work

    elif nowy_tryb == "Klienci":
        Label(ramka_formularz, text="Imie: ").grid(row=1, column=0, sticky='w')
        entry_imie = Entry(ramka_formularz)
        entry_imie.grid(row=1, column=1, sticky='ew')
        pola_formularza['imie'] = entry_imie

        Label(ramka_formularz, text="Nazwisko: ").grid(row=2, column=0, sticky='w')
        entry_nazwisko = Entry(ramka_formularz)
        entry_nazwisko.grid(row=2, column=1, sticky='ew')
        pola_formularza['nazwisko'] = entry_nazwisko

        Label(ramka_formularz, text="Miejscowość: ").grid(row=3, column=0, sticky='w')
        entry_miejscowosc = Entry(ramka_formularz)
        entry_miejscowosc.grid(row=3, column=1, sticky='ew')
        pola_formularza['miejscowosc'] = entry_miejscowosc

        Label(ramka_formularz, text="Rok urodzenia: ").grid(row=4, column=0, sticky='w')
        entry_rok = Entry(ramka_formularz)
        entry_rok.grid(row=4, column=1, sticky='ew')
        pola_formularza['rok_urodzenia'] = entry_rok

import controller

def dodaj_obiekt():
    print(f"Tryb: {aktualny_tryb}")

    try:
        if aktualny_tryb == "Porty":
            dane ={
            "port_location": pola_formularza['port_location'].get(),
            "docks": pola_formularza['docks'].get(),
            "description": pola_formularza['description'].get(),
            }
            controller.add_port(dane)

        if aktualny_tryb == "Pracownicy":
            dane = {
                "imie": pola_formularza['imie'].get(),
                "nazwisko": pola_formularza['nazwisko'].get(),
                "pensja": pola_formularza['pensja'].get(),
                "work_location": pola_formularza['work_location'].get(),
            }
            controller.add_pracownik(dane)

        if aktualny_tryb == "Klienci":
            dane = {
                "imie": pola_formularza['imie'].get(),
                "nazwisko": pola_formularza['nazwisko'].get(),
                "miejscowosc": pola_formularza['miejscowosc'].get(),
                "rok_urodzenia": pola_formularza['rok_urodzenia'].get(),
            }
            controller.add_klient(dane)

    except ValueError:
        print("Nie podano obiekto")


#RAMKA PRZYCISKI
ramka_przyciski.grid_columnconfigure(0, weight=1)

button_porty = Button(ramka_przyciski, text="Porty", command=lambda: zmien_tryb("Porty"))
button_porty.grid(row=0, column=0, sticky='ew', pady=2)

button_pracownicy = Button(ramka_przyciski, text="Pracownicy", command=lambda: zmien_tryb("Pracownicy"))
button_pracownicy.grid(row=1, column=0, sticky='ew', pady=2)

button_klienci = Button(ramka_przyciski, text="Klienci", command=lambda: zmien_tryb("Klienci"))
button_klienci.grid(row=2, column=0, sticky='ew', pady=2)


#RAMKA FORMULARZ
ramka_formularz.grid_columnconfigure(1, weight=1)


#RAMKA FUNKCJONALMOŚCI
ramka_funkcjonalnosci.grid_columnconfigure(0, weight=1)
ramka_funkcjonalnosci.grid_columnconfigure(1, weight=1)

button_dodaj_obiekt = Button(ramka_funkcjonalnosci, text="Dodaj obiekt", command=dodaj_obiekt)
button_dodaj_obiekt.grid(row=0, column=0, sticky='ew', padx=1, pady=1)

button_usun_obiekt = Button(ramka_funkcjonalnosci, text="Usuń obiekt", command=usun_obiekt)
button_usun_obiekt.grid(row=0, column=1, sticky='ew', padx=1, pady=1)

button_aktualizuj = Button(ramka_funkcjonalnosci, text="Aktualizuj", command=aktualizuj)
button_aktualizuj.grid(row=1, column=0, sticky='ew', padx=1, pady=1)

button_szczegoly = Button(ramka_funkcjonalnosci, text="Pokaż szczegóły", command=szczegoly)
button_szczegoly.grid(row=1, column=1, sticky='ew', padx=1, pady=1)


#RAMKA LISTA
label_lista = Label(ramka_lista, text="Lista: ")
label_lista.grid(row=0, column=0, sticky='w')

label_filtr = Label(ramka_lista, text="Filtruj według Portu: ")
label_filtr.grid(row=0, column=1, sticky='w')

listbox_filtrowanie = ttk.Combobox(ramka_lista, status="readonly")
listbox_filtrowanie.grid(row=1, column=0, sticky='ew')
listbox_filtrowanie.bind("<<ComboboxSelected>>", odswiez_widok)

ramka_lista.grid_columnconfigure(0, weight=1)
ramka_lista.grid_rowconfigure(1, weight=1)

listbox_lista = Listbox(ramka_lista)
listbox_lista.grid(row=1, column=0, sticky='nsew')


#RAMKA MAPA
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=800, height=720, corner_radius=0)
map_widget.set_position(52.0, 21.0)
map_widget.set_zoom(5)
map_widget.pack(fill="both", expand=True)


#te przyciski będą w main
button_porty.config(command=lambda: zmien_tryb("Porty"))
button_pracownicy.config(command=lambda: zmien_tryb("Pracownicy"))
button_klienci.config(command=lambda: zmien_tryb("Klienci"))
button_dodaj_obiekt.config(command=dodaj_obiekt)

zmien_tryb("Porty")

root.mainloop()

