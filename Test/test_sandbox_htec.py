import HtmlTestRunner
from selenium import webdriver
import random
import time
import unittest
unittest.TestLoader.sortTestMethodsUsing = None

# Kreiranje listi 'tehnologies', 'seniority', 'teams' kako bih ih kasnije unio u polja
technologies = ('HTML/CSS', 'Python', 'Javascript', 'Ruby', 'SQL')
seniorities = ('Intern', 'Junior', 'Medior', 'Senior')
teams = ('PM', 'BE', 'FE')
people = ('John Stockton', 'Annie Hall', 'Karl Malone', 'Tracy McGrady', 'Jason Williams')


class SandTest(unittest.TestCase):

    #Kreiram metod za otvaranje stranice u Chrome-u, i maksimiziram prozor
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://qa-sandbox.ni.htec.rs/login")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    #Kreiram test za login
    def test_11_login(self):
        # Trazim placeholder za email sa imenom email i unosim svoju adresu
        username = self.driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div[2]/div[2]/input")
        username.send_keys("marko.goronja@gmail.com")

        # Trazim placeholder za lozinku sa imenom password i unosim svoju lozinku
        pw = self.driver.find_element_by_name("password")
        pw.clear()
        pw.send_keys("qaskillcheck")

        # Potvrđujem unos email adrese i lozinke
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/button').click()
        time.sleep(2)

    #Kreiram test za klik na playground iz menija
    def test_12_playground(self):
        # Klik na "Playground" opciju iz menija
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div/div[2]/div[2]/a[3]/div[1]/div/img').click()

    #Kreiram test za dodavanje novog projekta i unos naziva
    def test_13_new_project(self):
        #Klik na "New project"
        self.driver.find_element_by_link_text('New Project').click()

        #Unos naziva projekta i potvrda unosa klikom na "Submit" dugme
        title = self.driver.find_element_by_name("title")
        title.clear()
        title.send_keys("Projekat")
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[2]/button').click()

    #Kreiram test za popunjavanje tehnologija
    def test_14_technologies_fill(self):
        #Popunjavanje 'Technologies'
        tehnologija = self.driver.find_element_by_name('technology')
        for i in technologies:
            tehnologija.clear()
            tehnologija.send_keys(i)
            self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[2]/button').click()
            time.sleep(2)

    #Kreiram test za popunjavanje senioriteta
    def test_15_seniorities_fill(self):
        # Popunjavanje 'Seniorities'
        senioritet = self.driver.find_element_by_name('seniority')
        for i in seniorities:
            senioritet.clear()
            senioritet.send_keys(i)
            self.driver.find_element_by_xpath(
                '/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[2]/button').click()
            time.sleep(2)

    #Kreiram test za popunjavanje naziva timova
    def test_16_teams(self):
        # Popunjavanje 'Teams'
        timovi = self.driver.find_element_by_name('team')
        for i in teams:
            timovi.clear()
            timovi.send_keys(i)
            self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/button').click()
            time.sleep(1)

    #Kreiram test za popunjavanje 1. osobe
    def test_17_persons_fill(self):
        #Popunjavanje 'Person'

        time.sleep(5)
        ljudi = self.driver.find_element_by_name('person')

        ljudi.send_keys("John Stockton")

        #Nasumični izbor "tehnologije"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 4))).click()
        time.sleep(1)

        #Nasumični izbor "senioriteta"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[2]/div').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 3))).click()
        time.sleep(1)

        #Nasumični izbor "tima"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[4]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 2))).click()
        time.sleep(1)

        self.driver.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[5]/button').click()

    # Kreiram test za popunjavanje 2. osobe
    def test_18_persons_fill(self):
        # Popunjavanje 'Person'
        ljudi = self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[2]/input')

        time.sleep(1)
        ljudi.send_keys("Annie Hall")

        # Nasumični izbor "tehnologije"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 4))).click()
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        time.sleep(1)

        # Nasumični izbor "senioriteta"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[2]/div').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 3))).click()
        time.sleep(1)

        # Nasumični izbor "tima"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[4]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 2))).click()
        time.sleep(1)

        self.driver.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[5]/button').click()
        time.sleep(2)

    # Kreiram test za popunjavanje 3. osobe
    def test_19_persons_fill(self):
        # Popunjavanje 'Person'
        ljudi = self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[2]/input')

        time.sleep(1)
        ljudi.send_keys("Karl Malone")

        # Nasumični izbor "tehnologije"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 4))).click()
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        time.sleep(1)

        # Nasumični izbor "senioriteta"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[2]/div').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 3))).click()
        time.sleep(1)

        # Nasumični izbor "tima"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[4]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 2))).click()
        time.sleep(1)

        self.driver.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[5]/button').click()
        time.sleep(2)

    # Kreiram test za popunjavanje 4. osobe
    def test_21_persons_fill(self):
        # Popunjavanje 'Person'
        ljudi = self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[2]/input')

        time.sleep(1)
        ljudi.send_keys("Tracy McGrady")

        # Nasumični izbor "tehnologije"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 4))).click()
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        time.sleep(1)

        # Nasumični izbor "senioriteta"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[2]/div').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 3))).click()
        time.sleep(1)

        # Nasumični izbor "tima"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[4]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 2))).click()
        time.sleep(1)

        self.driver.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[5]/button').click()
        time.sleep(2)

    # Kreiram test za popunjavanje 5. osobe
    def test_22_persons_fill(self):
        # Popunjavanje 'Person'
        ljudi = self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[2]/input')

        time.sleep(1)
        ljudi.send_keys("Jason Williams")

        # Nasumični izbor "tehnologije"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 4))).click()
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/button').click()
        time.sleep(1)

        # Nasumični izbor "senioriteta"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[2]/div').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 3))).click()
        time.sleep(1)

        # Nasumični izbor "tima"
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[4]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_id('picky-option-' + str(random.randint(0, 2))).click()
        time.sleep(1)

        self.driver.find_element_by_xpath\
        ('//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/div[5]/button').click()
        time.sleep(2)

    def test_23_project_fill(self):
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/button/span').click()
        self.driver.find_element_by_id('picky-option-selectall').click()
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[2]/button').click()

    def test_24_title_rename(self):
        # Promjena naziva projekta

        self.driver.find_element_by_name('title').send_keys(u'\ue009' + u'\ue003')
        self.driver.find_element_by_name('title').send_keys('Novo ime')
        self.driver.find_element_by_xpath\
        ('/html/body/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[2]/button').click()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/../../Desktop/test'))
