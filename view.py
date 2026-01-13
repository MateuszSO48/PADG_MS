from tkinter import *
from tkinter import ttk, messagebox
import tkintermapview
import controller

root = Tk()
root.title("System Zarządzania Portami")
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


def stworz_pole(etykieta, klucz, rzad):
    Label(ramka_formularz, text=etykieta).grid(row=rzad, column=0, sticky='w')
    entry = Entry(ramka_formularz)
    entry.grid(row=rzad, column=1, sticky='w')
    pola_formularza[klucz] = entry


def wyczysc_pola():
    for pole in pola_formularza.values():
        pole.delete(0, END)


def aktualizuj_filtr():
    lista_miast = ["Wszystkie"] + controller.get_port_names()
    combobox_filtrowanie['values'] = lista_miast
    combobox_filtrowanie.current(0)


def odswiez_widok(event=None):
    listbox_lista.delete(0, END)
    map_widget.delete_all_marker()

    lista = controller.get_list(aktualny_tryb)
    filtr = combobox_filtrowanie.get()

    for obiekt in lista:
        tekst = ""
        miasto = ""
        if aktualny_tryb == "Porty":
            tekst = obiekt.port_location
            miasto = obiekt.port_location

        elif aktualny_tryb == "Pracownicy":
            tekst = f"{obiekt.imie} {obiekt.nazwisko} (Praca: {obiekt.work_location})"
            miasto = obiekt.work_location

        elif aktualny_tryb == "Klienci":
            tekst = f"{obiekt.imie} {obiekt.nazwisko} (Z miasta: {obiekt.miejscowosc})"
            miasto = obiekt.miejscowosc

        czy_pokazac = False
        if filtr == "Wszystkie": czy_pokazac = True
        elif aktualny_tryb == "Porty": czy_pokazac = True
        elif miasto == filtr: czy_pokazac = True

        if czy_pokazac:
            listbox_lista.insert(END, tekst)
            if obiekt.coords != [52.0, 21.0]:
                map_widget.set_marker(obiekt.coords[0], obiekt.coords[1], text=tekst)



def zmien_tryb(nowy_tryb):
    global aktualny_tryb
    aktualny_tryb = nowy_tryb

    for widget in ramka_formularz.winfo_children():
        widget.destroy()

    pola_formularza.clear()

    button_dodaj_obiekt.config(text="Dodaj obiekt", command=dodaj_obiekt)
    Label(ramka_formularz, text=f"Formularz: {nowy_tryb}").grid(row=0, column=0, columnspan=2)

    if nowy_tryb == "Porty":
       stworz_pole("Lokalizacja: ", "port_location", 1)
       stworz_pole("Liczba miejsc:", "docks", 2)
       stworz_pole("Opis:", "description", 3)
       label_filtr.grid_remove()
       combobox_filtrowanie.grid_remove()

    elif nowy_tryb == "Pracownicy":
        stworz_pole("Imię : ", "imie", 1)
        stworz_pole("Nazwisko :", "nazwisko", 2)
        stworz_pole("Pensja :", "pensja", 3)
        stworz_pole("Miejsce pracy :", "work_location", 4)
        label_filtr.grid(row=0, column=0, sticky='w')
        combobox_filtrowanie.grid(row=1, column=0, sticky='w')

    elif nowy_tryb == "Klienci":
        stworz_pole("Imię : ", "imie", 1)
        stworz_pole("Nazwisko :", "nazwisko", 2)
        stworz_pole("Miejscowość :", "miejscowosc", 3)
        stworz_pole("Rok urodzenia :", "rok_urodzenia", 4)
        label_filtr.grid(row=0, column=0, sticky='w')
        combobox_filtrowanie.grid(row=1, column=0, sticky='ew')

    aktualizuj_filtr()
    odswiez_widok()


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

        elif aktualny_tryb == "Pracownicy":
            dane = {
                "imie": pola_formularza['imie'].get(),
                "nazwisko": pola_formularza['nazwisko'].get(),
                "pensja": pola_formularza['pensja'].get(),
                "work_location": pola_formularza['work_location'].get(),
            }
            controller.add_pracownik(dane)

        elif aktualny_tryb == "Klienci":
            dane = {
                "imie": pola_formularza['imie'].get(),
                "nazwisko": pola_formularza['nazwisko'].get(),
                "miejscowosc": pola_formularza['miejscowosc'].get(),
                "rok_urodzenia": pola_formularza['rok_urodzenia'].get(),
            }
            controller.add_klient(dane)

        wyczysc_pola()
        aktualizuj_filtr()
        odswiez_widok()

    except Exception as e:
       messagebox.showerror("Bład danych")


def usun_obiekt():
    wybor = listbox_lista.curselection()
    if not wybor:
        return

    i = wybor[0]
    if aktualny_tryb == "Porty":
        controller.remove_port(i)

    elif aktualny_tryb == "Pracownicy":
        controller.remove_pracownik(i)

    elif aktualny_tryb == "Klienci":
        controller.remove_klient(i)

    odswiez_widok()
    aktualizuj_filtr()


def zapisz_zmiany(i):
    try:
        if aktualny_tryb == "Porty":
            dane ={
            "port_location": pola_formularza['port_location'].get(),
            "docks": pola_formularza['docks'].get(),
            "description": pola_formularza['description'].get(),
            }
            controller.update_port(i, dane)

        elif aktualny_tryb == "Pracownicy":
            dane = {
                "imie": pola_formularza['imie'].get(),
                "nazwisko": pola_formularza['nazwisko'].get(),
                "pensja": pola_formularza['pensja'].get(),
                "work_location": pola_formularza['work_location'].get(),
            }
            controller.update_pracownik(i, dane)

        elif aktualny_tryb == "Klienci":
            dane = {
                "imie": pola_formularza['imie'].get(),
                "nazwisko": pola_formularza['nazwisko'].get(),
                "miejscowosc": pola_formularza['miejscowosc'].get(),
                "rok_urodzenia": pola_formularza['rok_urodzenia'].get(),
            }
            controller.update_klient(i, dane)

        messagebox.showinfo("Sukces", "Zaktualizowano obiekt")
        wyczysc_pola()
        odswiez_widok()
        aktualizuj_filtr()

        button_dodaj_obiekt.config(text="Dodaj obiekt", command=dodaj_obiekt)

    except Exception as e:
       messagebox.showerror("Bład, sprawdź dane")


def edytuj_obiekt():
    wybor = listbox_lista.curselection()
    if not wybor:
        return
    i = wybor[0]

    wyczysc_pola()
    obiekt = controller.get_list(aktualny_tryb)[i]

    if aktualny_tryb == "Porty":
        pola_formularza['port_location'].insert(0,obiekt.port_location)
        pola_formularza['docks'].insert(0,str(obiekt.docks))
        pola_formularza['description'].insert(0,obiekt.description)

    elif aktualny_tryb == "Pracownicy":
        pola_formularza['imie'].insert(0,obiekt.imie)
        pola_formularza['nazwisko'].insert(0,obiekt.nazwisko)
        pola_formularza['pensja'].insert(0,str(obiekt.pensja))
        pola_formularza['work_location'].insert(0,obiekt.work_location)

    elif aktualny_tryb == "Klienci":
        pola_formularza['imie'].insert(0,obiekt.imie)
        pola_formularza['nazwisko'].insert(0, obiekt.nazwisko)
        pola_formularza['miejscowosc'].insert(0, obiekt.miejscowosc)
        pola_formularza['rok_urodzenia'].insert(0, str(obiekt.rok_urodzenia))

    button_dodaj_obiekt.config(text="Zapisz zmiany", command=lambda: zapisz_zmiany(i))


def pokaz_szczegoly():
    if aktualny_tryb != "Porty":
        return

    wybor = listbox_lista.curselection()
    if not wybor:
        return

    tekst = listbox_lista.get(wybor[0])
    port = None
    for p in controller.porty:
        if p.port_location in tekst:
            port = p
            break

    if port:
        pracownicy, klienci = controller.filter_details(port.port_location)

        map_widget.delete_all_marker()
        if port.coords != [52.0, 21.0]:
            map_widget.set_marker(port.coords[0], port.coords[1], text=f"Port: {port.port_location}")

        for pracownik in pracownicy:
            if pracownik.coords != [52.0, 21.0]:
                map_widget.set_marker(pracownik.coords[0], pracownik.coords[1], text=f"{pracownik.imie}{pracownik.nazwisko}")

        for klient in klienci:
            if klient.coords != [52.0, 21.0]:
                map_widget.set_marker(klient.coords[0], klient.coords[1], text=f"{klient.imie}{klient.nazwisko}")

            if port.coords != [52.0, 21.0]:
                map_widget.set_position(port.coords[0], port.coords[1])
                map_widget.set_zoom(11)

            informacja = f"Port: {port.port_location} \nOpis: {port.description} \nPracownicy: {len(pracownicy)} \nKlienci: {len(klienci)} "
            messagebox.showinfo("Szczegóły portu", informacja)


def zlokalizuj_obiekt(event=None):
    wybor = listbox_lista.curselection()
    if not wybor: return

    indeks = wybor[0]
    obiekt = controller.get_list(aktualny_tryb)[indeks]

    if obiekt and obiekt.coords != [52.0, 21.0]:
        map_widget.set_position(obiekt.coords[0], obiekt.coords[1])
        map_widget.set_zoom(12)





ramka_przyciski.grid_columnconfigure(0, weight=1)

Button(ramka_przyciski, text="Porty", command=lambda: zmien_tryb("Porty")).grid(row=0, column=0, sticky='ew')
Button(ramka_przyciski, text="Pracownicy", command=lambda: zmien_tryb("Pracownicy")).grid(row=1, column=0, sticky='ew')
Button(ramka_przyciski, text="Klienci", command=lambda: zmien_tryb("Klienci")).grid(row=2, column=0, sticky='ew')


ramka_funkcjonalnosci.grid_columnconfigure((0,1), weight=1)

global button_dodaj_obiekt
button_dodaj_obiekt = Button(ramka_funkcjonalnosci, text="Dodaj obiekt", command=dodaj_obiekt)
button_dodaj_obiekt.grid(row=0, column=0, sticky='ew', padx=1, pady=1)

Button(ramka_funkcjonalnosci, text="Usuń obiekt", command=usun_obiekt).grid(row=0, column=1, sticky='ew')
Button(ramka_funkcjonalnosci, text="Edytuj", command=edytuj_obiekt).grid(row=1, column=0, sticky='ew')
Button(ramka_funkcjonalnosci, text="Pokaż szczegóły", command=pokaz_szczegoly).grid(row=1, column=1, sticky='ew')


ramka_lista.grid_columnconfigure(0, weight=1)
global label_filtr, combobox_filtrowanie

label_filtr = Label(ramka_lista, text="Filtruj według Portu: ")
label_filtr.grid(row=0, column=0, sticky='w')

combobox_filtrowanie = ttk.Combobox(ramka_lista, state="readonly", width=35)
combobox_filtrowanie.grid(row=1, column=0, sticky='ew')
combobox_filtrowanie.bind("<<ComboboxSelected>>", odswiez_widok)


Label(ramka_lista, text="Lista: ").grid(row=2, column=0, sticky='w')

listbox_lista = Listbox(ramka_lista)
listbox_lista.grid(row=3, column=0, sticky='nsew')


listbox_lista.bind('<Double-Button-1>', zlokalizuj_obiekt)
Button(ramka_lista, text="Przybliż", command=zlokalizuj_obiekt).grid(row=4, column=0, sticky='ew', pady=5)


#RAMKA MAPA
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=800, height=720, corner_radius=0)
map_widget.set_position(52.0, 21.0)
map_widget.set_zoom(5)
map_widget.pack(fill="both", expand=True)


zmien_tryb("Porty")

def start():
    root.mainloop()

