from tkinter import *
import tkintermapview

root = Tk()
root.title("System zarządziania siecią portów")
root.geometry("1200x760")


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

label_formularz = Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=2, sticky='w')

label_imie = Label(ramka_formularz, text="Imie: ")
label_imie.grid(row=1, column=0, sticky='w')
entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1, sticky='ew')

label_lokalizacja = Label(ramka_formularz, text="Lokalizacja: ")
label_lokalizacja.grid(row=2, column=0, sticky='w')
entry_lokalizacja = Entry(ramka_formularz)
entry_lokalizacja.grid(row=2, column=1, sticky='ew')

label_posty = Label(ramka_formularz, text="Posty: ")
label_posty.grid(row=3, column=0, sticky='w')
entry_posty = Entry(ramka_formularz)
entry_posty.grid(row=3, column=1, sticky='ew')

label_img_url = Label(ramka_formularz, text="Obrazek: ")
label_img_url.grid(row=4, column=0, sticky='w')
entry_img_url = Entry(ramka_formularz)
entry_img_url.grid(row=4, column=1, sticky='ew')


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

root.mainloop()