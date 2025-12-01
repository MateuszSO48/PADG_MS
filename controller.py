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
            port.docks = input("Podaj nową liczbę stanowisk: ")
            port.description = input("Podaj nowy opis portu: ")

