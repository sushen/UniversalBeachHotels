import time
import pandas as pd
from selenium.webdriver.common.by import By
from system_upgread.check_internet_connection import CheckInternetConnection


class Main:
    def run_all_script(self, driver):
        time.sleep(2)
        driver.implicitly_wait(10)
        check_in_date_x_path = "//div[@class='arrival-date dateInput']"
        check_in_element = driver.find_element(By.XPATH, check_in_date_x_path)
        print(check_in_element)
        check_in_element.click()

        time.sleep(2)
        driver.implicitly_wait(10)
        two_thousand_twenty_fore_x_path = "(//span[normalize-space()='2024'])[1]"
        two_thousand_twenty_element = driver.find_elements(By.XPATH, two_thousand_twenty_fore_x_path)
        print(two_thousand_twenty_element)

        while True:

            if len(two_thousand_twenty_element) == 0:
                time.sleep(2)
                driver.implicitly_wait(10)
                next_x_path = "//a[@title='Next']"
                next_element = driver.find_element(By.XPATH, next_x_path)
                next_element.click()
                print(next_element)

                april_x_path = "(//span[normalize-space()='April'])[1]"
                if driver.find_elements(By.XPATH, april_x_path):
                    april_element = driver.find_element(By.XPATH, april_x_path)

                    print(april_element.text)

                    time.sleep(2)
                    driver.implicitly_wait(10)
                    select_check_in_date_x_path = "(//a[@href='#'][normalize-space()='21'])[1]"
                    select_check_in_element = driver.find_element(By.XPATH, select_check_in_date_x_path)
                    print(select_check_in_element)
                    select_check_in_element.click()

                    time.sleep(2)
                    driver.implicitly_wait(10)
                    select_check_out_date_x_path = "(//a[@href='#'][normalize-space()='28'])[1]"
                    select_check_out_element = driver.find_element(By.XPATH, select_check_out_date_x_path)
                    print(select_check_out_element)
                    select_check_out_element.click()

                    time.sleep(2)
                    driver.implicitly_wait(10)
                    search_x_path = "(//button[@type='submit'][normalize-space()='Search'])[2]"
                    search_element = driver.find_element(By.XPATH, search_x_path)
                    print(search_element)
                    search_element.click()

                    time.sleep(2)
                    driver.implicitly_wait(10)
                    internal_double_room_x_path = "//li[@data-roomcode='DBL#INT']//span[@class='price']"
                    internal_double_room_element = driver.find_elements(By.XPATH, internal_double_room_x_path)
                    print(internal_double_room_element)
                    print(len(internal_double_room_element))

                    internal_double_room_prices = []
                    for i in range(len(internal_double_room_element)):
                        print(internal_double_room_element[i].text)
                        price = internal_double_room_element[i].text
                        internal_double_room_prices.append(price)

                        input("Stop .. :")

                    data = {'Price': internal_double_room_prices}
                    df = pd.DataFrame(data)

                    # Specify the file path where you want to save the Excel file
                    file_path = 'room_prices.xlsx'

                    # Save the DataFrame to an Excel file
                    df.to_excel(file_path, index=False)

                    print(f'Prices have been saved to {file_path}')

                    break


if __name__ == "__main__":
    CheckInternetConnection().try_until_connect()
    from driver.driver import Driver
    from login.login import Login

    driver = Driver().driver
    driver.get("https://www.universalbeachhotels.com/en/hoteles/universal-hotel-marques")
    time.sleep(4)
    Login().login(driver)
    Main().run_all_script(driver)
