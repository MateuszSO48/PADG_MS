from model import Port, Pracownik, Klient
from model import get_coordinates
import psycopg2

polaczenie = None

porty = []
pracownicy = []
klienci = []


def nawiaz_polaczenie(config):
    global polaczenie
    polaczenie = psycopg2.connect(**config)
    print("Połączono z bazą danych pomyślnie.")


def wczytaj_dane():
    global porty, pracownicy, klienci
    porty.clear()
    pracownicy.clear()
    klienci.clear()

    cursor = polaczenie.cursor()

    SQL = "SELECT id, lokalizacja, doki, opis, lat, lon FROM porty"
    cursor.execute(SQL)
    for wiersz in cursor.fetchall():
        nowy_port = Port(wiersz[1], wiersz[2], wiersz[3], id=wiersz[0], saved_coords=[wiersz[4], wiersz[5]])
        porty.append(nowy_port)

    SQL = "SELECT id, imie, nazwisko, pensja, miejsce_pracy, lat, lon FROM pracownicy"
    cursor.execute(SQL)
    for wiersz in cursor.fetchall():
        nowy_pracownik = Pracownik(wiersz[1], wiersz[2], wiersz[3], wiersz[4],id=wiersz[0], saved_coords=[wiersz[5], wiersz[6]])
        pracownicy.append(nowy_pracownik)

    SQL = "SELECT id, imie, nazwisko, miejscowosc, rok_urodzenia, lat, lon FROM klienci"
    cursor.execute(SQL)
    for wiersz in cursor.fetchall():
        nowy_klient = Klient(wiersz[1], wiersz[2], wiersz[3], wiersz[4], id=wiersz[0], saved_coords=[wiersz[5], wiersz[6]])
        klienci.append(nowy_klient)



def get_list(tryb):
    if tryb == 'Porty':
        return porty
    elif tryb == 'Pracownicy':
        return pracownicy
    else:
        return klienci


def get_port_names():
    names = []
    for port in porty:
        names.append(port.port_location)
    return names


def filter_details(miasto):
    lista_pracownikow = []
    for pracownik in pracownicy:
        if pracownik.work_location == miasto:
            lista_pracownikow.append(pracownik)

    lista_klientow = []
    for klient in klienci:
        if klient.miejscowosc == miasto:
            lista_klientow.append(klient)

    return lista_pracownikow, lista_klientow


def add_port(port_data)->None:
    temp = Port(port_data['port_location'], int(port_data['docks']), port_data['description'])

    cursor = polaczenie.cursor()
    SQL = f"INSERT INTO porty (lokalizacja, doki, opis, lat, lon) VALUES ('{temp.port_location}', {temp.docks}, '{temp.description}', {temp.coords[0]}, {temp.coords[1]})"
    cursor.execute(SQL)
    polaczenie.commit()
    wczytaj_dane()


def add_pracownik(pracownik_data)->None:
    temp = Pracownik(pracownik_data['imie'], pracownik_data['nazwisko'], int(pracownik_data['pensja']), pracownik_data['work_location'])

    cursor = polaczenie.cursor()
    SQL = f"INSERT INTO pracownicy (imie, nazwisko, pensja, miejsce_pracy, lat, lon) VALUES ('{temp.imie}', '{temp.nazwisko}', {temp.pensja}, '{temp.work_location}', {temp.coords[0]}, {temp.coords[1]})"
    cursor.execute(SQL)
    polaczenie.commit()
    wczytaj_dane()


def add_klient(klient_data)->None:
    temp = Klient(klient_data['imie'], klient_data['nazwisko'], klient_data['miejscowosc'], int(klient_data['rok_urodzenia']))

    cursor = polaczenie.cursor()
    SQL = f"INSERT INTO klienci (imie, nazwisko, miejscowosc, rok_urodzenia, lat, lon) VALUES ('{temp.imie}', '{temp.nazwisko}', '{temp.miejscowosc}', {temp.rok_urodzenia}, {temp.coords[0]}, {temp.coords[1]})"
    cursor.execute(SQL)
    polaczenie.commit()
    wczytaj_dane()


def remove_port(i:int)->None:
    if i < len(porty):
        objekt_id = porty[i].id
        cursor = polaczenie.cursor()
        SQL = f"DELETE FROM porty WHERE id={objekt_id}"
        cursor.execute(SQL)
        polaczenie.commit()
        wczytaj_dane()


def remove_pracownik(i:int)->None:
    if i < len(pracownicy):
        objekt_id = pracownicy[i].id
        cursor = polaczenie.cursor()
        SQL = f"DELETE FROM pracownicy WHERE id={objekt_id}"
        cursor.execute(SQL)
        polaczenie.commit()
        wczytaj_dane()


def remove_klient(i:int)->None:
    if i < len(klienci):
        obj_id = klienci[i].id
        cursor = polaczenie.cursor()
        SQL = f"DELETE FROM klienci WHERE id={obj_id}"
        cursor.execute(SQL)
        polaczenie.commit()
        wczytaj_dane()


def update_port(i:int, port_data:dict)->None:
    port = porty[i]
    coords = get_coordinates(port_data['port_location'])

    cursor = polaczenie.cursor()
    SQL = f"UPDATE porty SET lokalizacja='{port_data['port_location']}', doki={int(port_data['docks'])}, opis='{port_data['description']}', lat={coords[0]}, lon={coords[1]} WHERE id={port.id}"
    cursor.execute(SQL)
    polaczenie.commit()
    wczytaj_dane()


def update_pracownik(i:int, pracownik_data:list)->None:
    pracownik = pracownicy[i]
    coords = get_coordinates(pracownik_data['work_location'])

    cursor = polaczenie.cursor()
    SQL = f"UPDATE pracownicy SET imie='{pracownik_data['imie']}', nazwisko='{pracownik_data['nazwisko']}', pensja={int(pracownik_data['pensja'])}, miejsce_pracy='{pracownik_data['work_location']}', lat={coords[0]}, lon={coords[1]} WHERE id={pracownik.id}"
    cursor.execute(SQL)
    polaczenie.commit()
    wczytaj_dane()


def update_klient(i:int, klient_data:list)->None:
    klient = klienci[i]
    coords = get_coordinates(klient_data['miejscowosc'])

    cursor = polaczenie.cursor()
    SQL = f"UPDATE klienci SET imie='{klient_data['imie']}', nazwisko='{klient_data['nazwisko']}', miejscowosc='{klient_data['miejscowosc']}', rok_urodzenia={int(klient_data['rok_urodzenia'])}, lat={coords[0]}, lon={coords[1]} WHERE id={klient.id}"
    cursor.execute(SQL)
    polaczenie.commit()
    wczytaj_dane()



