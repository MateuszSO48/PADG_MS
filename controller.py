from model import Port, Pracownik, Klient

def port_info(port_data:list)->None:
    for port in port_data:
        print(f"Port {port.port_location} ma {port.docks} stanowisk i zawiera opis: {port.description}")


def add_port(port_data:list)->None:
    port_location:str = input("Podaj miejscowość portu: ")
    docks:int = int(input("Podaj liczbę stanowisk: "))
    description:str = input("Podaj opis portu: ")
    port_data.append(Port(port_location=port_location, docks=docks, description=description, img_url=img_url))


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

def pracownicy_portu(port_data:list, pracownik_data:list)->None:
    print("Dostępne porty: ")
    for port in port_data:
     print(f"Port: {port.port_location}")
    pracownicy_portu_choice:str = input("Podaj nazwę portu, którego pracowników chcesz sprawdzić: ")
    if pracownik_data:
        pracownicy_danego_portu = [pracownik for pracownik in pracownik_data if pracownik.work_location == pracownicy_portu_choice]
    if pracownicy_portu:
        print(f"Pracownnicy portu {pracownicy_portu_choice}: ")
        for pracownik in pracownicy_danego_portu:
                print(f" Pracownik - {pracownik.imie} {pracownik.nazwisko} zarabiający {pracownik.pensja} ")
    else:
            print("Brak przypisanych pracowników ")


def klienci_portu(port_data:list, klient_data:list)->None:
    print("Aktualne porty: ")
    for port in port_data:
        print(f"Port: {port.port_location}")
    klienci_portu_choice:str = input("Podaj nazwę portu, którego klientów chcesz sprawdzić: ")
    if klient_data:
        klienci_danego_portu = [klient for klient in klient_data if klient.miejscowość == klienci_portu_choice]
    if klienci_portu:
        print(f"Klienci portu: {klienci_portu_choice}: ")
        for klient in klienci_danego_portu:
            print(f" Klient - {klient.imie} {klient.nazwisko} urodzonony {klient.rok_urodzenia}")


def pracownik_info(pracownik_data:list)->None:
    for pracownik in pracownik_data:
        print(f"{pracownik.imie} {pracownik.nazwisko} zarabia {pracownik.pensja} w miejscowości {pracownik.work_location}")


def add_pracownik(pracownik_data:list, port_data:list)->None:
    print("Dostępne porty: ")
    for port in port_data:
        print(f"Port {port.port_location}: {port.description}")

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


def add_klient(klient_data:list, port_data:list)->None:
    print("Dostępne porty: ")
    for port in port_data:
        print(f"Port {port.port_location}: {port.description}")
    imie:str = input("Podaj imie klienta: ")
    nazwisko:str = input("Podaj nazwisko klienta: ")
    miejscowość:str = input("Podaj miejscowość klienta: ")
    rok_urodzenia:int = int(input("Podaj rok urodzenia klienta: "))
    klient_data.append(Klient(imie=imie, nazwisko=nazwisko, miejscowość=miejscowość, rok_urodzenia=rok_urodzenia))


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
