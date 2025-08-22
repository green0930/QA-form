import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    def load(self):
        self.driver.get(self.url)

    def fill_first_name(self, first_name):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(By.ID, "LastName").send_keys(last_name)

    def fill_mobile_number(self, number):
        self.driver.find_element(By.ID, "userNumber").send_keys(number)

    def select_gender(self, gender):
        self.driver.find_element(By.XPATH,"f//label[text()='{gender_label}']").click()

    def select_hobby(self, hobby_label="Music"):
        self.driver.find_element(By.XPATH,f"//label[text()='{hobby_label}']").click()

    def upload_file(self, filename = "sample.png"):
        upload_element = self.driver.find_element(By.ID, "uploadPicture")
        file_path = os.path.abspath(filename)
        upload_element.send_keys(file_path)

    def submit_form(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.ID, "submit")

    def select_date_of_birth(self, month="June", year="1990", day="21"):
        self.driver.find_element(By.ID, "dateOfBirthInput").click()

        # select year
        year_select = self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_select.click()
        year_select.find_element(By.XPATH,f"//option[@value='{year}']").click()

        # select month
        month_select = self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
        month_select.click()
        month_select.find_element(By.XPATH, f"//option[text()='{month}']").click()

        # Select day (ignore leading 0s or duplicates)
        day_selector = f"//div[contains(@class, 'react-datepicker__day') and text()='{int(day)}']"
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, day_selector))
        ).click()

    def select_subject(self, subject_name="Maths"):
        subject_input = self.driver.find_element(By.ID, "subjectsInput")
        subject_input.send_keys(subject_name)
        subject_input.send_keys(Keys.RETURN)

    def select_state(self, state="NCR"):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        state_field = self.driver.find_element(By.ID, "react-select-3-input")
        state_field.send_keys(state)
        state_field.send_keys(Keys.RETURN)

    def select_city(self, city="Delhi"):
        city_field = self.driver.find_element(By.ID, "react-select-4-input")
        city_field.send_keys(city)
        city_field.send_keys(Keys.RETURN)