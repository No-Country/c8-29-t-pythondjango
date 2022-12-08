import time

import pyautogui
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from explicity_wait import ExplicitWaitType
import pandas as pd
import datetime
import math
from api_job import send_jobs


class Automation:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(
            "https://indeed.com/")
        self.driver.implicitly_wait(0.7)
        self.action = ActionChains(self.driver)
        self.wait = ExplicitWaitType(self.driver)
        self.df = pd.DataFrame(columns=['title', 'subtitle', 'sub_subtitle', 'location', 'company', 'salary', 'type', 'description',
                                        'date_publish', 'url_postulacion'])

    def search_job(self,job, location):
        input_search_job = self.wait.waitForElement(locator='text-input-what')
        self.wait.sendKeys(job, input_search_job)
        search_buttom = self.wait.waitForElement(locator='//*[@id="jobsearch"]/button', locatorType='xpath')
        location_element = self.wait.waitForElement(locator='text-input-where')
        self.wait.sendKeys(location, location_element)
        self.wait.elementClick(search_buttom)
        time.sleep(3)

    def extract_data(self, name, location):
        continuar = True
        n = 1
        set_remoto = self.wait.waitForElement(locator='//*[@id="filter-remotejob"]/div[1]', locatorType='xpath')
        self.wait.elementClick(set_remoto)
        pyautogui.press("down")
        pyautogui.press("enter")
        while continuar:

            time.sleep(2)
            title_click = self.wait.waitForElement(locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a',locatorType='xpath')
            title_click_texto = self.wait.get_text(title_click)
            card_job = self.wait.waitForElement(
                locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a',
                locatorType='xpath')
            self.wait.elementClick(card_job)
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0,	500);	")
            time.sleep(1)
            title = self.wait.waitForElement(
                locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a',
                locatorType='xpath')
            title = self.wait.get_text(title)
            # print(title)
            subtitle = self.wait.waitForElement(
                locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/div[1]'
                        '/div/table[1]/tbody/tr/td/div[2]', locatorType='xpath')
            subtitle = self.wait.get_text(subtitle)
            company_type = self.format_name_company(subtitle)

            print(f"subtitle:{subtitle}")
            sub_subtitle = self.wait.waitForElement(
                locator=f'//*[@id="mosaic-provider-jobcards"]/ul/li[{n}]/div/div[1]/div/'
                        'div[1]/div/table[1]/tbody/tr/td/div[3]', locatorType='xpath')
            sub_subtitle = self.wait.get_text(sub_subtitle)
            salary = self.format_salary(sub_subtitle)
            print(f"sub_subtitle:{sub_subtitle}")
            description = self.wait.waitForElement(locator='//*[@id="jobDescriptionText"]', locatorType='xpath')
            description = self.wait.get_text(description)
            # print(description)
            print("--------------------------------")

            date_publish = self.wait.waitForElement(locator='//*[@id="hiringInsightsSectionRoot"]/p[3]/span[2]',
                                                    locatorType='xpath')
            date_publish = self.wait.get_text(date_publish)
            if date_publish is None:
                date_publish = self.wait.waitForElement(locator='//*[@id="hiringInsightsSectionRoot"]/p/span[2]',
                                                        locatorType='xpath')
                date_publish = self.wait.get_text(date_publish)
                date_publish = self.format_date(date_publish)
                print(f"date con formato: {date_publish}")
            else:
                date_publish = self.format_date(date_publish)
            if subtitle is not None or sub_subtitle is not None:
                print(title_click_texto)
                self.driver.execute_script("window.scrollBy(0,	-300);	")
                self.action.context_click(card_job).perform()
                time.sleep(1)
                pyautogui.press("down")
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(2)
                try:
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    url_postulacion = self.driver.current_url
                    self.driver.close()
                    time.sleep(1)
                    self.driver.switch_to.window(self.driver.window_handles[0])
                except:
                    pass
                else:
                    if subtitle == None or sub_subtitle == None:
                        pass
                    else:

                        # self.write(title=title,subtitle=subtitle,sub_subtitle=sub_subtitle,type=company_type[1],salary=salary,
                        #            company=company_type[0], description=description, date_publish=date_publish,
                        #            url_postulacion=url_postulacion, name=name, location=location)
                        self.write(title=title, subtitle=subtitle, sub_subtitle=sub_subtitle, type="Remoto",
                                   salary=salary,
                                   company=company_type[0], description=description, date_publish=date_publish,
                                   url_postulacion=url_postulacion, name=name, location=location)
                        send_jobs(title, sub_subtitle, description, date_publish, subtitle, url_postulacion,"Remoto", company_type[0],salary, location)
            print(n)
            if n == 15:
                time.sleep(5)
                next_page = self.wait.waitForElement(locator='//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[6]/a', locatorType='xpath')
                if next_page is not None:
                    n = 1
                    self.wait.elementClick(next_page)
                else:
                    continuar = False
                    self.driver.close()
                    return
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
            if len(dias) >= 2:
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

    def format_salary(self,subtitle):
        if subtitle is None:
            return ""
        count = 0
        subtitle_list = subtitle.split("\n")
        for salary in subtitle_list:
            for caracter in salary:
                if caracter.isnumeric():
                    count += 1
            if count > 3:
                return salary
            else:
                count = 0
        if subtitle == "Tiempo completo":
            return "Salario sin especificar"
        return subtitle

    def format_name_company(self, text):
        if text is None:
            return ""
        text_list = text.split("\n")
        if "Remoto" in text_list:
            return text_list[0], "Remoto"
        return text_list[0], "Presencial"


    def write(self, title, sub_subtitle, description, date_publish, subtitle, url_postulacion, type, company, salary, name, location):
        self.df = self.df.append({"title": title, 'subtitle':subtitle, 'sub_subtitle':sub_subtitle, "location":location,
                                  'description':description, 'date_publish': date_publish,
                                  'url_postulacion':url_postulacion, "type":type, "company":company, "salary":salary},
                                 ignore_index=True)
        self.df.to_csv(f"{name}{datetime.datetime.now().date()}.csv")



