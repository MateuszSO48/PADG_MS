from controller import *
from model import porty, pracownicy

def main():
    while True:
        print("Wyświetlanie, dodawanie, usuwanie, aktualizacja czego chcesz przeprowadzić: ")
        print("0. Wyjście")
        print("1. Portów")
        print("2. Pracowników")
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
                else:
                    print("Niepoprawny wybór")

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
                    add_pracownik(pracownicy)
                if tmp_choice == 3:
                    remove_pracownik(pracownicy)
                if tmp_choice == 4:
                    update_pracownik(pracownicy)
                else:
                    print("Niepoprawny wybór")

        else:
            print("Niepoprawna opcja")


if __name__ == "__main__":
    main()

