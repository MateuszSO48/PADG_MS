import view
import controller

DB_CONFIG = {
    "user": "postgres",
    "password": "postgres",
    "database": "postgres",
    "host": "localhost",
    "port": "5432"
}


if __name__ == '__main__':
    controller.nawiaz_polaczenie(DB_CONFIG)
    controller.wczytaj_dane()
    view.start()