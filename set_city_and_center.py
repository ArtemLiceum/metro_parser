from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from data import DELAY


def set_city(driver, city_xpath):
    try:
        change = WebDriverWait(driver, DELAY).until(  # текущий адрес
            EC.element_to_be_clickable((By.XPATH, '//*[@id="layout"]/div/div/div[1]/header/div[2]/div[1]/div[2]/button/address'))
        )
        change.click()

        modal_element = driver.find_element(By.XPATH,
                '//*[@id="__layout"]/div/div/div[9]/div[2]/div'
        )
        driver.switch_to.frame(modal_element)

        choose_myself = WebDriverWait(driver, DELAY).until(  # самовывоз
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div/div[9]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]'))
        )
        choose_myself.click()

        change_city = WebDriverWait(driver, DELAY).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div/div[9]/div[2]/div/div[1]/div/div[1]/div/div[2]/div[1]/span'))
        )
        change_city.click()

        choose_city = WebDriverWait(driver, DELAY).until(
            EC.element_to_be_clickable((By.XPATH, city_xpath))
        )
        choose_city.click()

        enter_change = WebDriverWait(driver, DELAY).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div/div[9]/div[2]/div/div[1]/div/div[1]/div/button'))
        )
        enter_change.click()

        driver.switch_to.default_content()
    except Exception as e:
        print(f'Возникла ошибка в set_city(): {e}')


def set_center(driver, centre_XPath):
    try:
        change = driver.find_element(By.XPATH,
             (
                 '//*[@id="__layout"]/div/div/div[1]/header/div[2]/div[1]/div[2]/button/address'  # текущий адрес
             )
        )
        change.click()
        time.sleep(DELAY)

        modal_element = driver.find_element(By.XPATH,
                '//*[@id="__layout"]/div/div/div[9]/div[2]/div'
        )
        driver.switch_to.frame(modal_element)

        choose_myself = driver.find_element(By.XPATH,
            (
                '//*[@id="__layout"]/div/div/div[9]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]'  # самовывоз
            )
        )
        choose_myself.click()
        time.sleep(DELAY)

        choose_center = driver.find_element(By.XPATH, centre_XPath)  # выбираем центр
        choose_center.click()
        time.sleep(DELAY)

        enter_change = driver.find_element(
            By.XPATH,
            (
                '//*[@id="__layout"]/div/div/div[9]/div[2]/div/div[1]/div/div[1]/div/button'  # выбрать
            )
        )
        enter_change.click()
        time.sleep(DELAY)
        driver.switch_to.default_content()
    except Exception as e:
        print(f'Возникла ошибка в set_center(): {e}')