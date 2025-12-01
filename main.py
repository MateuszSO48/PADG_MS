from controller import *
from model import porty

def main():
    while True:
        print("********************************MENU**************************************")
        print("0. Wyjście z programu")
        print("1. Wyświetlanie portu")
        print("2. Dodaj port")
        print("3. Usuń port")
        print("4. Aktualizuj port")
        print("**************************************************************************")

        tmp_choice:int=int(input("Wybierz opcję z MENU: "))
        if tmp_choice == 0:
            break
        if tmp_choice == 1:
            print("Wybrano funkcję wyświetlenia portów")
            port_info(porty)
        if tmp_choice == 2:
            print("Wybrano funckję dodawania portu: ")
            add_port(porty)
        if tmp_choice == 3:
            print("Wybrano funckję usuwania portu: ")
            remove_port(porty)
        if tmp_choice == 4:
            print("Wybrano funkcję aktualizowania portu: ")
            update_port(porty)


if __name__ == "__main__":
    main()

