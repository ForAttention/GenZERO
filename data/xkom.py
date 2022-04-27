from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from data.personal import CreatePerson
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup





class XKom:
    """Długo szukałem strony gdzie można wykonac jakieś logowanie (z 'rejestracja') bez problemu"""

    def __init__(self, email_instance_user):
        self.email_instance_user = email_instance_user

    def all_in_class(self):
        XKom.register(self)
        time.sleep(10)
        XKom.add_to_cart(self)
        XKom.fill_data_in_cart(self)

    def start_convert(self):
        global browser
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)
        browser.get("https://www.x-kom.pl")
        browser.maximize_window()
        time.sleep(4)
        # browser.find_element(By.XPATH, "//div[@id='react-portals']/div[4]/div/div[@role='dialog']//button[.='W "
        #                                "porządku']").click()
        browser.find_element(By.XPATH, "/html//div[@id='react-portals']//div[@role='dialog']//button[.='W porządku']").click()
        time.sleep(2)
        XKom.conversation(self)

    def register(self):
        """Wystarczy nam sam ChromeDriverManager z install, zapewne każdy korzysta lub ma przeglądarkę Google Chrome
            W przypadku przykładu - nie chcę wrzucać na gita plików .exe (chromedriver.exe)

            Od wersji 4.0 (jakoś po nowym roku) nie można już używać klasycznego find_element_by_class_name ;_;"""

        global browser
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)
        browser.get("https://www.x-kom.pl")
        browser.maximize_window()
        time.sleep(3)

        browser.find_element(By.XPATH, "/html//div[@id='react-portals']//div[@role='dialog']//button[.='W porządku']").click()
        browser.find_element(By.XPATH, "/html//div[@id='app']/div[1]/header/div[1]/div[4]/div/div[2]/div/div["
                                            "1]/a[@href='/konto']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div/div[1]/div/div[2]//a[@href='/rejestracja']").click()
        time.sleep(3)
        browser.find_element(By.NAME, "firstName").send_keys(CreatePerson.first_name())
        browser.find_element(By.NAME, "lastName").send_keys(CreatePerson.last_name())
        browser.find_element(By.NAME, "email").send_keys(self.email_instance_user)
        browser.find_element(By.NAME, "password").send_keys(CreatePerson.password())
        browser.find_element(By.XPATH, "/html//div[@id='app']/div/div[1]/div/div[1]//form//div[@class='ldtoi0-6 "
                                       "loocTj']").click()
        browser.find_element(By.XPATH, "//div[@id='app']/div/div[1]/div/div[1]//form//button[@type='submit']/span["
                                       ".='Załóż konto']").click()
        browser.find_element(By.XPATH, "/html//div[@id='app']/div[1]//a[@title='x-kom.pl']/span[1]/img[@alt='x-kom - "
                                       "Sklep komputerowy']").click()

    def add_to_cart(self):
        """Nie posiadam na tn moment serwera pocztowego więc zademonstruje jak na razie poruszanie się po sklepie"""
        """Proszę za mną"""
        browser.find_element(By.XPATH, "/html//div[@id='app']/div[1]//nav/ul/li[4]/a[@role='menuitem']/div["
                                       ".='Podzespoły komputerowe']").click()
        browser.find_element(By.XPATH, "/html//div[@id='app']/div[2]/div[2]/div[2]/div[2]/div[2]/div[4]/a["
                                       "@href='/g-5/c/345-karty-graficzne.html']//img[@alt='Karty graficzne']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "/html//div[@id='app']/div[2]/div[4]/div[2]/div[1]/div[1]/div/div/div/div/div["
                                       "1]/div/div/div").click()
        browser.find_element(By.XPATH, "/html//div[@id='app']/div[2]/div/div[1]/div[3]/div[2]//button[@title='Dodaj do koszyka']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html//div[@id='react-portals']//div[@role='dialog']//a[@href='/koszyk']").click()
        browser.find_element(By.XPATH, "/html//div[@id='app']/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[3]/button").click()

    def fill_data_in_cart(self):
        """Wypełnimy jakieś dane, zobaczymy co się wydarzy"""
        browser.find_element(By.NAME, "recipientName").send_keys(CreatePerson.first_name() + " " + CreatePerson.last_name())
        browser.find_element(By.NAME, "recipientStreet").send_keys(CreatePerson.street() + " " + CreatePerson.house_number())
        browser.find_element(By.NAME, "recipientPostalCode").send_keys(CreatePerson.postal_code())
        browser.find_element(By.NAME, "recipientCity").send_keys(CreatePerson.city())
        browser.find_element(By.NAME, "recipientEmail").send_keys(self.email_instance_user)
        browser.find_element(By.NAME, "recipientPhoneNumber").send_keys(CreatePerson.phone())
        time.sleep(1)
        """Przechodzimy do podsumowania"""

        """X-Kom to react, co się objawia problemem z klikaniem kluczowych przcisków"""
        """W taki sposób szukam rozwiązania"""
        aaa = browser.find_elements(By.XPATH, "/html//div[@id='app']/div//form/div/div[3]/div/div[1]/div[4]/div[4]/button")
        bbb = browser.find_elements(By.CSS_SELECTOR, "[class='sc-15ih3hi-0 pvj85d-4 cCPDSX']")
        ccc = browser.find_elements(By.CSS_SELECTOR, ".cCPDSX.pvj85d-4.sc-15ih3hi-0")

        print(len(aaa))
        print(len(bbb)) # to printuje te jedynki
        print(len(ccc))

        """Jest tyle opcji wyboru ponieważ nie zawsze działa jeden sposób ;_;"""
        if len(aaa) > 0:
            browser.find_element(By.XPATH, "/html//div[@id='app']/div//form/div/div[3]/div/div[1]/div[4]/div[4]/button").click()
            return
        elif len(bbb) > 0:
            browser.find_element(By.CSS_SELECTOR, "[class='sc-15ih3hi-0 pvj85d-4 cCPDSX']").click()
            return
        elif len(ccc) > 0:
            browser.find_element(By.CSS_SELECTOR, ".cCPDSX.pvj85d-4.sc-15ih3hi-0").click()

    def conversation(self):
        """Moduł ten będzie prowadził rozmowę z konsultantem z x-kom'a
        Nie wiem czy to zadziała, pisze komentarz przed napisaniem kodu :O
        Ale mam ochotę dla prezentaji napisać banalnego bota
        Który wciśnie konsultantowi fotowoltaikę

        pro edit: myslę, że na potrzeby tego modułu zrobię osobny start dla rozmowy
        Będzie to moduł: start_convert
        Będzie w nim otwieranie przegladarki (instalacja drivera - max_window i inne)
        I od razu przejście do tego modułu
        Aby nie przechodzić całego procesu w klasie"""

        """Zaczniemy od otwarcia komówrki z dymkiem"""
        browser.find_element(By.XPATH, "//div[@id='react-portals']//button").click()
        time.sleep(2)

        """Teraz musimy znaleźć pole tekstowe i wprowadzić do niego wyrazy
        nalepiej zapisać to jako zmienna i się później odnosić do tego jako inputText"""
        """test"""
        print("Zaczynamy odpytywnaie")
        some_text = ["Jesteś 2 w kolejce",
                     "Niedługo połączy się z Tobą doradca."]
        boologic = False
        lenght = 0
        welcome = 0
        looking_for = 0 # kiedys się przydasz
        name = ""
        wait = 0
        priv_ask = 0
        while boologic != True:
            table = []
            print(f"Zerujemu tablicę = {len(table)}")
            print(f"Nasza długość length wynosi = {lenght}")

            """Plan jest taki aby olać asynchroniczne moduły wraz z wbudowaną komendą od selenium
            W pętli while odpytujemy non stop stronę, xkom dodaje nowe pliki div i span z podobną klasą
            liczymy ile jest na stronie, kazda odpowiedź konsultanta to dodatkowy div/span
            Jeżeli zostanie wykryty > od poprzedniej puli to analizujemy tekst"""

            """Pobieramy całą stronę"""
            content = browser.page_source
            """content będzie naszym requestem aby nie rzucać tak ciastkami za pomocą requests"""

            bs41 = BeautifulSoup(content, "lxml")
            bs44 = bs41.body.find_all('span', {"class": "sc-154u2ib-4 cDszJB"})
            """Jak się okazało istnieje tag span gdzie klasa ma zawsze taką samą nazwę i występuje tylko w tym chacie"""
            # syntax = re.findall("^[sc-154u2ib-3]<?/", str(bs41))
            for z in bs44:
                """zapisujemy po kolei wszystkie 'teksty' z chatu do tablicy table """
                zet = BeautifulSoup(str(z), "lxml")
                wu = zet.find("span").get_text()
                print(wu)
                if str(wu) in table:
                    continue
                table.append(wu)
            """Tutaj ustalamy warunki, na początku wchodzimy do warunku powitania, po jego spełnienu ustalają się 
            wszystkie zmienne """
            newtext = browser.find_elements(By.NAME, "message")
            print(f"Nasza długość length po skrobaniu wynosi = {lenght}")
            print(f"Nasza długość tablicy po skrobaninu wynosi = {len(table)}")
            if len(table) > lenght and len(table) != 0:
                if lenght < len(table):
                    """Musimy to tutaj zrównać, inaczej nie ma jak dodać tego do lenght a nasz główny if zawsze będzie sie wykonywał"""
                    lenght = 0
                    lenght += len(table)

                if welcome == 0:
                    newtext[0].send_keys("Witam, mam pytanie dotyczące sprzętu, czy jestem połączony z konsultantem?")
                    browser.find_element(By.XPATH, "/html//div[@id='react-portals']//form/button").click()
                    """Ustalamy że welcome już nie będzie równe zero aby ponownie nie wpaść do warunku"""
                    welcome += 1
                    """Ustalamy pierwszą długość tablicy , każda nowa wiadomość to kolejny element"""
                    lenght += 1
                    print(f"dodalismy do lenght 1 = {len(table)}")

                """Powstaje wyjątek, czasem mogę być któryś w kolejce, element nie będzie 3 tylko 5"""
                if name == "":
                    if some_text[0] in table or some_text[1] in table:
                        if len(table) >= 4:
                            """Tutaj wyciągniemy z chatu imię konsultanta
                                Jest to zwykle 3 element tablicy table, imię jest na końcu"""
                            name = table[4][27:]
                            print(f"Pobrano imię konsultanta - {name}")
                            wait += 1
                    else:
                        if len(table) == 3:
                            """Tutaj wyciągniemy z chatu imię konsultanta
                                Jest to zwykle 3 element tablicy table, imię jest na końcu
                                Ten else jest na wypadek kiedy bedę któryś w kolejce"""
                            name = table[2][27:]
                            print(f"Pobrano imię konsultanta - {name}")

                if name != "":
                    if wait == 1:
                        if len(table) == 6:
                            print("Wysyłamy pierwsze zapytanie o falownik do fotowoltaiki :)")
                            newtext[0].send_keys(f"Cześć {name}, czy macie może w ofercie falowniki do fotowoltaiki?")
                            browser.find_element(By.XPATH, "/html//div[@id='react-portals']//form/button").click()
                            lenght += 1
                    if wait == 0:
                        if len(table) == 4:
                            print("Wysyłamy pierwsze zapytanie o falownik do fotowoltaiki :)")
                            newtext[0].send_keys(f"Cześć {name}, czy macie może w ofercie falowniki do fotowoltaiki?")
                            browser.find_element(By.XPATH, "/html//div[@id='react-portals']//form/button").click()
                            lenght += 1

                if priv_ask == 0:
                    if wait == 1:
                        if len(table) >= 7:
                            print("Wysyłamy drugie zapytanie o falownik do fotowoltaiki :)")
                            newtext[0].send_keys(f"{name} a może sam szukasz godnego polecenia sprzętu do odbioru energii ze słońca?"
                                                 f"Chyba możemy się dogadać - dobrze, że się znaleźliśmy :D ")
                            browser.find_element(By.XPATH, "/html//div[@id='react-portals']//form/button").click()
                            lenght += 1
                    if wait == 0:
                        if len(table) >= 6:
                            print("Wysyłamy drugie zapytanie o falownik do fotowoltaiki :)")
                            newtext[0].send_keys(
                                f"{name} a może sam szukasz godnego polecenia sprzętu do odbioru energii ze słońca?"
                                f"Chyba możemy się dogadać - dobrze, że się znaleźliśmy :D ")
                            browser.find_element(By.XPATH, "/html//div[@id='react-portals']//form/button").click()
                            lenght += 1

                    """Więcej nie będę rozpisywał żeby mi nie zablokowali IP albo wrzucili ma black_list"""
                    ""'Za pomocą ifów można to rozbudowywać, lub napisa pod to klasę, jeżeli ktoś chce stworzyć ' \
                    'poważny system relacji z konsultantem'
                    """Ja robiłem to dla zabawy więc za pomocą ifów chciałem pokazać tylko żę się da"""
                time.sleep(5)
            time.sleep(5)
            """To jest teraz bardzo ważne, tablica table będzie zerowana co cykl pętli while, natomiast zminna 
            lenght musi trzymac poprzednią wartość ilości elementów """

