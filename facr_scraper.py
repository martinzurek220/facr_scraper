from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
import os

from twocaptcha import TwoCaptcha


def get_code(sitekey: str, url: str) -> dict:
    """
    Funkce ziska capcha kod ze zadaneho url s capchou

    Priklad vystupu:

    {'CapchaId': '71914160706', 'code': '03A...75w'}

    :param sitekey: "sitekey z html kodu"
    :param url: "url s capchou"
    :return: {slovnik s kodem}
    """
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('APIKEY_2CAPTCHA', '6a9f5831289bfb362b04f134cbd24fd0')
    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)
    except Exception as e:
        print(e)
    else:
        return result


def capcha_solver(browser: webdriver, sitekey: str, url: str) -> None:
    """
    Funkce pouzije ziskany capcha kod, vlozi ho do html kodu a klikne na tl. Pokracovat.

    :param browser: webdriver
    :param sitekey: "sitekey z html kodu"
    :param url: "url s capchou"
    :return: None
    """
    token = get_code(sitekey, url)
    code = token['code']
    print(code)

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "g-recaptcha-response"))
    )

    time.sleep(3)

    # Vlozeni code do HTML kodu
    browser.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'"
    )

    time.sleep(3)

    # Nalezeni a stisknuti tlacitka potvrdit
    button_pokracovat = browser.find_element(By.CSS_SELECTOR, 'a[id="MainContent_btnLogin"]')
    button_pokracovat.click()

    time.sleep(1000)


def main():
    sitekey = "6LdleRoUAAAAAFPzy5u9zlmtLy4qKT_Jb8EItoad"
    url = "https://is.fotbal.cz/security-valid.aspx?hidemenu=1&ret=%2fzapasy%2fzapis-o-utkani-report.aspx%3fzapas%3d18c8bd4f-cff6-40be-a67a-c30428d3e027%26zapis%3d1%26noprint%3d1%26btnprint%3d1%26.htm"

    browser = webdriver.Chrome()
    browser.get(url)

    capcha_solver(browser, sitekey, url)


if __name__ == "__main__":
    main()
