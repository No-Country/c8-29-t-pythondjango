import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from explicity_wait import ExplicitWaitType
import pandas as pd
import datetime
import math


class Automation:
    def __init__(self):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(
            "https://mx.indeed.com/")
        self.driver.implicitly_wait(0.7)
        self.wait = ExplicitWaitType(self.driver)
        self.df = pd.DataFrame(columns=['title', 'subtitle', 'sub_subtitle', 'description', 'date_publish', 'url_postulacion'])

    def search_job(self):
        input_search_job = self.wait.waitForElement(locator='text-input-what')
        self.wait.sendKeys("Python", input_search_job)
        search_buttom = self.wait.waitForElement(locator='//*[@id="jobsearch"]/button', locatorType='xpath')
        self.wait.elementClick(search_buttom)
        time.sleep(3)

    def extract_data(self):
        continuar = True
        n = 1
        while continuar:
            card_job = self.wait.waitForElement(
                locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a',
                locatorType='xpath')
            self.wait.elementClick(card_job)
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0,	1000);	")
            title = self.wait.waitForElement(
                locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a',
                locatorType='xpath')
            title = self.wait.get_text(title)
            # print(title)
            subtitle = self.wait.waitForElement(
                locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/div[1]'
                        '/div/table[1]/tbody/tr/td/div[2]', locatorType='xpath')
            subtitle = self.wait.get_text(subtitle)
            # print(subtitle)
            sub_subtitle = self.wait.waitForElement(
                locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/'
                        'div[1]/div/table[1]/tbody/tr/td/div[3]', locatorType='xpath')
            sub_subtitle = self.wait.get_text(sub_subtitle)
            # print(sub_subtitle)
            description = self.wait.waitForElement(locator='//*[@id="jobDescriptionText"]', locatorType='xpath')
            description = self.wait.get_text(description)
            # print(description)
            print("--------------------------------")

            date_publish = self.wait.waitForElement(locator='//*[@id="hiringInsightsSectionRoot"]/p[3]/span[2]',
                                                    locatorType='xpath')
            date_publish = self.wait.get_text(date_publish)
            print(f"date sin formato: {date_publish}")
            if date_publish is None:
                date_publish = self.wait.waitForElement(locator='//*[@id="hiringInsightsSectionRoot"]/p/span[2]',
                                                        locatorType='xpath')
                date_publish = self.wait.get_text(date_publish)
                date_publish = self.format_date(date_publish)
                print(f"date con formato: {date_publish}")
            else:
                date_publish = self.format_date(date_publish)
            print(f"date con formato: {date_publish}")
            buttom_postularse = self.wait.waitForElement(
                locator='#jobsearch-ViewJobButtons-container > div.jobsearch-ButtonContainer-inlineBlock.icl-u-lg-inlineBlock > div > div > span',
                locatorType='css')
            self.wait.elementClick(buttom_postularse)
            if buttom_postularse is None:
                buttom_postularse = self.wait.waitForElement(
                    locator='#jobsearch-ViewJobButtons-container > div.icl-u-lg-inlineBlock.viewJobButtonLinkContainer',
                    locatorType='css')
                self.wait.elementClick(buttom_postularse)
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            url_postulacion = self.driver.current_url
            self.driver.close()
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[0])
            if n == 15:
                next_page = self.wait.waitForElement(locator='//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/'
                                                             'nav/div[6]/a/svg', locatorType='xpath')
                if next_page is not None:
                    n = 1
                    self.wait.elementClick(next_page)
                else:
                    continuar = False
            n += 1

    def format_date(self, date):
        if date is None:
            return datetime.datetime.now().date()
        date = date.split(" ")
        if len(date) != 4:
            return datetime.datetime.now().date()
        if "Hoy" in date:
            date = {datetime.datetime.now().date()}
            return date
        elif "días" in date:
            dias = date[2]
            dias = dias[0] + dias[1]
            if int(dias) > int(str(datetime.datetime.now().day)):
                dias = int(str(datetime.datetime.now().day)) - int(dias)
                date = f"{datetime.datetime.now().year}-{datetime.datetime.now().month-1}-{int(31 - math.fabs(int(dias)))}"
                return date
            date = f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{int(str(datetime.datetime.now().day)) - math.fabs(int(dias))}"
            return date
        elif "1" in date:
            date = datetime.datetime.now().date()
            return date
        else:
            date = datetime.datetime.now().date()
            return date


    def write(self, title, sub_subtitle, description, date_publish, subtitle, url_postulacion):
        self.df = self.df.append({"title": title, 'subtitle':subtitle, 'sub_subtitle':sub_subtitle, 'description':description, 'date_publish': date_publish, 'url_postulacion':url_postulacion},
                                 ignore_index=True)
        self.df.to_csv("part_number_sin_imagenes.csv")


