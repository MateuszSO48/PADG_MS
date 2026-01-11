from controller import *
from model import porty, pracownicy, klienci


def main():
    while True:
        print("Wyświetlanie, dodawanie, usuwanie, aktualizacja czego chcesz przeprowadzić: ")
        print("0. Wyjście")
        print("1. Portów")
        print("2. Pracowników")
        print("3. Klienci")
        function_choice = int(input("Wybierz opcję: "))

        if function_choice == 0:
            break

        if function_choice == 1:
            while True:
                print("********************************MENU PORTÓW**************************************")
                print("0. Powrót")
                print("1. Wyświetlanie portów")
                print("2. Dodaj port")
                print("3. Usuń port")
                print("4. Aktualizuj port")
                print("5. Wyświetlenie pracowników danego portu")
                print("6. Wyświetelnie klientów danego portu")
                print("*********************************************************************************")
                tmp_choice = int(input("Wybierz opcję: "))

                if tmp_choice == 0:
                    break
                if tmp_choice == 1:
                    port_info(porty)
                if tmp_choice == 2:
                    add_port(porty)
                if tmp_choice == 3:
                    remove_port(porty)
                if tmp_choice == 4:
                   update_port(porty)
                if tmp_choice == 5:
                    pracownicy_portu(porty, pracownicy)
                if tmp_choice == 6:
                    klienci_portu(porty, klienci)


        if function_choice == 2:
            while True:
                print("********************************MENU PRACOWNIKÓW*********************************")
                print("0. Powrót")
                print("1. Wyświetlanie pracowników")
                print("2. Dodaj pracownika")
                print("3. Usuń pracownika")
                print("4. Aktualizuj pracownika")
                print("*********************************************************************************")

                tmp_choice = int(input("Wybierz opcję: "))

                if tmp_choice == 0:
                    break
                if tmp_choice == 1:
                    pracownik_info(pracownicy)
                if tmp_choice == 2:
                    add_pracownik(pracownicy, porty)
                if tmp_choice == 3:
                    remove_pracownik(pracownicy)
                if tmp_choice == 4:
                    update_pracownik(pracownicy, porty)



        if function_choice ==3:
            while True:
                print("********************************MENU KLIENTÓW*********************************")
                print("0. Powrót")
                print("1. Wyświetlanie klientów")
                print("2. Dodaj klienta")
                print("3. Usuń klienta")
                print("4. Aktualizuj klienta")
                print("*********************************************************************************")

                tmp_choice = int(input("Wybierz opcję: "))

                if tmp_choice == 0:
                    break
                if tmp_choice == 1:
                    klient_info(klienci)
                if tmp_choice == 2:
                    add_klient(klienci, porty)
                if tmp_choice == 3:
                    remove_klient(klienci)
                if tmp_choice == 4:
                    update_klient(klienci, porty)

        else:
            print("Niepoprawna opcja")


if __name__ == "__main__":
    main()

