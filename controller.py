from model import Port, Pracownik, Klient
from model import get_coordinates

porty = []
pracownicy = []
klienci = []


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
    port_location = port_data['port_location']
    docks = int(port_data['docks'])
    description = port_data['description']
    porty.append(Port(port_location=port_location, docks=docks, description=description))


def add_pracownik(pracownik_data)->None:
    imie = pracownik_data['imie']
    nazwisko = pracownik_data['nazwisko']
    pensja = int(pracownik_data['pensja'])
    work_location = pracownik_data['work_location']
    pracownicy.append(Pracownik(imie=imie, nazwisko=nazwisko, pensja=pensja, work_location=work_location))


def add_klient(klient_data)->None:
    imie = klient_data['imie']
    nazwisko = klient_data['nazwisko']
    miejscowosc = klient_data['miejscowosc']
    rok_urodzenia = int(klient_data['rok_urodzenia'])
    klienci.append(Klient(imie=imie, nazwisko=nazwisko, miejscowosc=miejscowosc, rok_urodzenia=rok_urodzenia))


def remove_port(i:int)->None:
    if i < len(porty):
        porty.pop(i)


def remove_pracownik(i:int)->None:
    if i < len(pracownicy):
        pracownicy.pop(i)


def remove_klient(i:int)->None:
    if i < len(klienci):
        klienci.pop(i)


def update_port(i:int, port_data:dict)->None:
    port = porty[i]
    port.port_location = port_data['port_location']
    port.docks = int(port_data['docks'])
    port.description = port_data['description']
    port.coords = get_coordinates(port.port_location)


def update_pracownik(i:int, pracownik_data:list)->None:
    pracownik = pracownicy[i]
    pracownik.imie = pracownik_data['imie']
    pracownik.nazwisko = pracownik_data['nazwisko']
    pracownik.pensja = int(pracownik_data['pensja'])
    pracownik.work_location = pracownik_data['work_location']
    pracownik.coords = get_coordinates(pracownik.work_location)


def update_klient(i:int, klient_data:list)->None:
    klient = klienci[i]
    klient.imie = klient_data['imie']
    klient.nazwisko = klient_data['nazwisko']
    klient.miejscowosc = klient_data['miejscowosc']
    klient.rok_urodzenia = int(klient_data['rok_urodzenia'])
    klient.coords = get_coordinates(klient.miejscowosc)



