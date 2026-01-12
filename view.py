from tkinter import *
import tkintermapview

root = Tk()
root.title("System zarządziania siecią portów")
root.geometry("1200x760")

aktualny_tryb = "Porty"
pola_formularza= {}

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)

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


#RAMKA PRZYCISKI
ramka_przyciski.grid_columnconfigure(0, weight=1)

button_porty = Button(ramka_przyciski, text="Porty")
button_porty.grid(row=0, column=0, sticky='ew', pady=2)

button_pracownicy = Button(ramka_przyciski, text="Pracownicy")
button_pracownicy.grid(row=1, column=0, sticky='ew', pady=2)

button_klienci = Button(ramka_przyciski, text="Klienci")
button_klienci.grid(row=2, column=0, sticky='ew', pady=2)


#RAMKA FORMULARZ
ramka_formularz.grid_columnconfigure(1, weight=1)


#RAMKA FUNKCJONALMOŚCI
ramka_funkcjonalnosci.grid_columnconfigure(0, weight=1)
ramka_funkcjonalnosci.grid_columnconfigure(1, weight=1)

button_dodaj_obiekt = Button(ramka_funkcjonalnosci, text="Dodaj obiekt")
button_dodaj_obiekt.grid(row=0, column=0, sticky='ew', padx=1, pady=1)

button_usun_obiekt = Button(ramka_funkcjonalnosci, text="Usuń obiekt")
button_usun_obiekt.grid(row=0, column=1, sticky='ew', padx=1, pady=1)

button_aktualizuj = Button(ramka_funkcjonalnosci, text="Aktualizuj")
button_aktualizuj.grid(row=1, column=0, sticky='ew', padx=1, pady=1)

button_szczegoly = Button(ramka_funkcjonalnosci, text="Pokaż szczegóły")
button_szczegoly.grid(row=1, column=1, sticky='ew', padx=1, pady=1)


#RAMKA LISTA
label_lista = Label(ramka_lista, text="Lista: ")
label_lista.grid(row=0, column=0, sticky='w')


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

