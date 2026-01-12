porty:list=[]

pracownicy:list=[]

klienci:list=[]


class Port:
    def __init__(self, port_location:str, docks:int, description:str, img_url:str):
        self.port_location = port_location
        self.docks = docks
        self.description = description
        self.coords = self.get_coordinates()

    def get_coordinates(self):
        import requests
        from bs4 import BeautifulSoup
        url: str = f'https://pl.wikipedia.org/wiki/{self.port_location}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        return [latitude, longitude]


class Pracownik:
    def __init__(self, imie:str, nazwisko:str, pensja:int, work_location:str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.work_location = work_location


class Klient:
    def __init__(self, imie:str, nazwisko:str, miejscowość:str, rok_urodzenia:int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejscowość = miejscowość
        self.rok_urodzenia = rok_urodzenia


