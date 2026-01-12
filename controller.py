from model import Port, Pracownik, Klient

porty = []
pracownicy = []
klienci = []


def port_info(port_data:list)->None:
    for port in port_data:
        print(f"Port {port.port_location} ma {port.docks} stanowisk i zawiera opis: {port.description}")


def add_port(port_data:dict)->None:
    port_location = port_data['port_location']
    docks = int(port_data['docks'])
    description = port_data['description']
    porty.append(Port(port_location=port_location, docks=docks, description=description))
    print(f"Dodano port: {port_location}")


def remove_port(port_data:list)->None:
    tmp_location:str=input("Podaj miejscowość portu do usunięcia: ")
    for port in port_data:
        if port.port_location == tmp_location:
            port_data.remove(port)
            break

def update_port(port_data:list)->None:
    tmp_location:str=input("Podaj miejscowść portu do aktualizacji: ")
    for port in port_data:
        if port.port_location == tmp_location:
            port.port_location = input("Podaj nową miejscowość portu: ")
            port.docks = int(input("Podaj nową liczbę stanowisk: "))
            port.description = input("Podaj nowy opis portu: ")
            break


def pracownik_info(pracownik_data:list)->None:
    for pracownik in pracownik_data:
        print(f"{pracownik.imie} {pracownik.nazwisko} zarabia {pracownik.pensja} w miejscowości {pracownik.work_location}")


def add_pracownik(pracownik_data:dict)->None:
    imie = pracownik_data['imie']
    nazwisko = pracownik_data['nazwisko']
    pensja = int(pracownik_data['pensja'])
    work_location = pracownik_data['work_location']
    pracownicy.append(Pracownik(imie=imie, nazwisko=nazwisko, pensja=pensja, work_location=work_location))
    print(pracownicy)


def remove_pracownik(pracownik_data:list)->None:
    tmp_imie:str=input("Podaj imie pracownika: ")
    for pracownik in pracownik_data:
        if pracownik.imie == tmp_imie:
            pracownik_data.remove(pracownik)


def update_pracownik(pracownik_data:list, port_data:list)->None:
    tmp_imie:str=input("Podaj imie pracownika: ")
    print("Dostępne porty: ")
    for port in port_data:
        print(f"Port {port.port_location}: {port.description}")

    for pracownik in pracownik_data:
        if pracownik.imie == tmp_imie:
            pracownik.imie = input("Podaj nowe imie pracownika: ")
            pracownik.nazwisko = input("Podaj nowe nazwisko pracownika: ")
            pracownik.pensja = int(input("Podaj nową pensję: "))
            pracownik.work_location = input("Podaj nazwę nowej miejsowości pracy: ")


def klient_info(klient_data: list) -> None:
    for klient in klient_data:
        print(f"Klient {klient.imie} {klient.nazwisko} z miejscowości {klient.miejscowość} urodził się w {klient.rok_urodzenia}")


def add_klient(klient_data:dict)->None:
    imie = klient_data['imie']
    nazwisko = klient_data['nazwisko']
    miejscowosc = klient_data['miejscowosc']
    rok_urodzenia = int(klient_data['rok_urodzenia'])
    klienci.append(Klient(imie=imie, nazwisko=nazwisko, miejscowosc=miejscowosc, rok_urodzenia=rok_urodzenia))


def remove_klient(klient_data:list)->None:
    tmp_imie:str=input("Podaj imie klienta: ")
    for klient in klient_data:
        if klient.imie == tmp_imie:
            klient_data.remove(klient)

def update_klient(klient_data:list, port_data:list)->None:
    tmp_imie:str=input("Podaj imie klienta do zaaktualzowania: ")
    print("Dostępne porty: ")
    for port in port_data:
        print(f"Port {port.port_location}: {port.description}")
    for klient in klient_data:
        if klient.imie == tmp_imie:
            klient.imie = input("Podaj nowe imie klienta: ")
            klient.nazwisko = input("Podaj nowe nazwisko klienta: ")
            klient.miejscowość = input("Podaj nową miejscowość klienta: ")


#dodanie funkcji obsługującej lokalizację

