class Port:
    def __init__(self, location:str, docks:int, description:str, img_url:str):
        self.location = location
        self.docks = docks
        self.description = description
        self.img_url = img_url


def port_info(port_data:list)->None:
    for port in port_data:
        print(f"Port {port.location} ma {port.docks} stanowisk i zawiera opis: {port.description}")


def add_port(port_data:list)->None:
    location:str = input("Podaj miejscowość portu: ")
    docks:int = int(input("Podaj liczbę stanowisk: "))
    description:str = input("Podaj opis portu: ")
    img_url:str = input("Wprowadź adres URL portu: ")
    port_data.append(Port(location=location, docks=docks, description=description, img_url=img_url))


def remove_port(port_data:list)->None:
    tmp_location:str=input("Podaj miejscowość portu do usunięcia: ")
    for port in port_data:
        if port.location == tmp_location:
            port_data.remove(port)


def update_port(port_data:list)->None:
    tmp_location:str=input("Podaj miejscowść portu do aktualizacji: ")
    for port in port_data:
        if port.location == tmp_location:
            port.location = input("Podaj nową miejscowość portu: ")
            port.docks = int(input("Podaj nową liczbę stanowisk: "))
            port.description = input("Podaj nowy opis portu: ")


class Pracownik:
    def __init__(self, imie:str, nazwisko:str, pensja:int, work_location:str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.work_location = work_location


def pracownik_info(pracownik_data:list)->None:
    for pracownik in pracownik_data:
        print(f"{pracownik.imie} {pracownik.nazwisko} zarabia {pracownik.pensja} w miejscowości {pracownik.work_location}")


def add_pracownik(pracownik_data:list)->None:
    imie:str = input("Podaj imie pracownika: ")
    nazwisko:str = input("Podaj nazwisko: ")
    pensja:int = int(input("Podaj pensję pracownika: "))
    work_location:str = input("Podaj miejscowość pracy: ")
    pracownik_data.append(Pracownik(imie=imie, nazwisko=nazwisko, pensja=pensja, work_location=work_location))


def remove_pracownik(pracownik_data:list)->None:
    tmp_imie:str=input("Podaj imie pracownika: ")
    for pracownik in pracownik_data:
        if pracownik.imie == tmp_imie:
            pracownik_data.remove(pracownik)


def update_pracownik(pracownik_data:list)->None:
    tmp_imie:str=input("Podaj imie pracownika: ")
    for pracownik in pracownik_data:
        if pracownik.imie == tmp_imie:
            pracownik.imie = input("Podaj nowe imie pracownika: ")
            pracownik.nazwisko = input("Podaj nowe nazwisko pracownika: ")
            pracownik.pensja = int(input("Podaj nową pensję: "))
            pracownik.work_location = input("Podaj nazwę nowej miejsowości pracy: ")
