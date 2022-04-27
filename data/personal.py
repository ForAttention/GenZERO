import random


class CreatePerson:
    """
    Plik z danymi:
    * mail
    * hasło
    * imię
    * nazwisko

    """
    global email
    global syntax
    syntax = 'qwertyuiopasdfghjklzxcvbnm'

    def mail(self=None):
        """Protonmail podniósł jakość Captchy do wersji 'h' z 're', jest to problem jak na razie nie do obejścia"""
        #    """Zakładamy konto pocztowe na serwerze protonmail """
        #
        # browser = webdriver.Chrome(ChromeDriverManager().install())
        # browser.implicitly_wait(10)
        # browser.get("https://protonmail.com")
        # browser.maximize_window()
        #
        # browser.find_element(By.XPATH, "//div[@id='bs-example-navbar-collapse-1']/ul[@class='nav navbar-nav "
        #                                "navbar-right']//a[@href='signup']").click()
        # browser.find_element(By.XPATH, "//div[@id='signup-plans']/div[@role='tablist']/div[1]/div[@role='tab']//div["
        #                                "@class='col-sm-1 col-xs-2']").click()
        # browser.find_element(By.XPATH, "/html//button[@id='freePlan']").click()
        #
        # frame_signup = browser.find_elements(By.TAG_NAME, 'iframe')
        #
        # print(f"Liczba ramek na tej stronie jest równa {len(frame_signup)}")
        #
        # browser.switch_to.frame(frame_signup[0])
        #
        # browser.find_element(By.ID, "username").send_keys(CreatePerson.first_name())
        # browser.find_element(By.ID, "password").send_keys(CreatePerson.password())
        # browser.find_element(By.ID, "repeat-password").send_keys(CreatePerson.password())
        # browser.find_element(By.XPATH, "/html//div[@class='app-root']/div[3]//form[@name='accountForm']/button["
        #                                "@type='submit']").click()
        # browser.switch_to.default_content()
        #
        # browser.find_element(By.XPATH, "/html//div[@class='app-root']/div[3]//form[@name='recoveryForm']/button["
        #                                "@type='button']").click()
        # browser.find_element(By.XPATH, "/html//div[@class='modal-two']/dialog//button[@class='button "
        #                                "button-solid-norm w100']").click()
        #
        # browser.find_element(By.XPATH, "/html//div[@class='modal-two']/dialog//button[@class='button "
        #                                "button-solid-norm w100']").click()
        #
        # frame_recaptha_white_window = browser.find_elements(By.TAG_NAME, "iframe")
        # browser.switch_to.frame(frame_recaptha_white_window[0])
        # frame_recaptha = browser.find_elements(By.TAG_NAME, "iframe")
        # browser.switch_to.frame(frame_recaptha[0])
        # """Nie oceniajcie mnie po tym"""
        # id_recaptha = browser.find_elements(By.ID, "checkbox")
        # xpath_recaptha = browser.find_elements(By.XPATH, "/html//div[@id='checkbox']")
        # if len(id_recaptha) > 0:
        #     try:
        #         browser.find_element(By.ID, "checkbox").click()
        #         print("Po id obiektu")
        #     except Exception:
        #         pass
        # elif len(xpath_recaptha) > 0:
        #     try:
        #         browser.find_element(By.XPATH, "/html//div[@id='checkbox']").click()
        #     except Exception:
        #         pass

        """Generujemy fejkowe maile aby się nie powtarzały
            Wykorzystam fakt że podczas tworzenia konta od razu jest się zalogownym"""
        front_monkey = ""
        for a in range(11):
            x = random.randrange(start=0, stop=25)
            front_monkey = front_monkey + syntax[x]

        globals()['email'] = front_monkey + "@wp.pl"
        # print(email)
        return email

    def phone(self=None):
        return "698342334"

    def first_name(self=None):
        return "Test"

    def last_name(self=None):
        return "Testowy"

    def password(self=None):
        return "Bartek.123"

    def street(self=None):
        return "Roosevelta"

    def house_number(self=None):
        return "25"

    def city(self=None):
        return "Poznań"

    def postal_code(self=None):
        return "60-829"
