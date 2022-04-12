from data.xkom import XKom
from data.personal import CreatePerson
global browser


if __name__ == "__main__":

    print("Witaj, do wyboru są dwie opcje: \n")
    print("1. Poruszanie się po stronie \n2. Rozmowa z konsultantem \n")
    while True:
        decy = input("Wybierz cyfrę aby wykonać: ")
        try:
            if int(decy) > 2:
                print(f"Nie ma takiego wyboru, jest 1 albo 2, nie ma nic pod {int(decy)}")
                continue
            elif int(decy) == 1:
                User = XKom(email_instance_user=CreatePerson.mail())
                User.all_in_class()
                exit()

            elif int(decy) == 2:
                User = XKom(email_instance_user=CreatePerson.mail())
                User.start_convert()
                exit()
        except ValueError:
            print(f"Muisz wpisać liczbę od 1 do 2, nie {decy}")

else:
    print("Nie importuj mnie, uruchom mnie jak normalny program hello_world.py")
    exit()
