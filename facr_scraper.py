"""
Pro rucni testovani kodu je potreba odkomentovat funkci xxx a rucne stahnout html kody
do souboru html_zdrojove_kody_rucne_stazene.py

Html kod kdyz ho stahuju pres selenium, je ten, co vidim v prohlizeci, kdyz si ho manualne otevru.
Html kod, kdyz ho stahuju pres beautifulsoup ma trosku jinou strukturu.
Pro stazeni html kodu pouzit selenium a pote parsovat skrz beautifulsoup.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
import os
import csv
import re
import json

import requests
from bs4 import BeautifulSoup

from twocaptcha import TwoCaptcha

import html_zdrojove_kody_rucne_stazene as ht


class DomaciHosteError(Exception):
    pass


def get_code(sitekey: str, url_s_capcha: str) -> dict:
    """
    Funkce ziska capcha kod ze zadaneho url s capchou

    Priklad vystupu:

    {'CapchaId': '71914160706', 'code': '03A...75w'}

    :param sitekey: "sitekey z html kodu"
    :param url_s_capcha: "url s capchou"
    :return: {slovnik s kodem}
    """
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('APIKEY_2CAPTCHA', '6a9f5831289bfb362b04f134cbd24fd0')
    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url_s_capcha)
    except Exception as e:
        print(e)
    else:
        return result


def capcha_solver(browser: webdriver, sitekey: str, url_s_capcha: str) -> None:
    """
    Funkce pouzije ziskany capcha kod, vlozi ho do html kodu a klikne na tl. Pokracovat.

    :param browser: webdriver
    :param sitekey: "sitekey_z_html_kodu"
    :param url_s_capcha: "url_s_capchou"
    :return: None
    """
    token = get_code(sitekey, url_s_capcha)
    code = token['code']
    # print(code)

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "g-recaptcha-response"))
    )

    time.sleep(3)

    # Vlozeni code do HTML kodu
    browser.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'"
    )

    time.sleep(3)

    # Nalezeni a stisknuti tlacitka Pokracovat
    button_pokracovat = browser.find_element(By.CSS_SELECTOR, 'a[id="MainContent_btnLogin"]')
    button_pokracovat.click()

    time.sleep(2)


def stahni_html_kod_seleinum(browser: webdriver, url_adresa: str):
    """
    Funkce stahne html kod z webu knihovnou Selenium.
    Vrati html kod ve formatu string, pripraveny k parsovani knihovnou beautifulsoup.

    " " "
    <html><body>
    ... telo ...
    </body></html>
    " " "

    :param browser: webdriver
    :param url_adresa: "url_adresa"
    :return: "html_kod_ve_formatu_string"
    """
    print(f"Stahuji data z URL adresy: {url_adresa}")
    browser.get(url_adresa)
    str_html = browser.page_source

    return str_html


def stahni_html_kod(url_adresa: str) -> BeautifulSoup:
    """
    Funkce stahne html kod z webu. Vrati naparsovany kod, pripraveny k prohledavani.

    Beautifulsoup =
    <html><body>
    ... telo ...
    </body></html>

    :param url_adresa: "url_adresa"
    :return: objekt BeautifulSoup
    """
    print(f"Stahuji data z URL adresy: {url_adresa}")
    odpoved = requests.get(url_adresa)

    return BeautifulSoup(odpoved.text, "html.parser")


def stahni_html_kod_rucne(html_kod: str) -> BeautifulSoup:
    """
    Funkce prevede rucne stazeny html kod na naparsovany objekt Beautifulsoup, ve kterem uz je mozno vyhledavat.

    Beautifulsoup =
    <html><body>
    ... telo ...
    </body></html>

    :param html_kod: "html kod"
    :return: objekt BeautifulSoup
    """
    return BeautifulSoup(html_kod, "html.parser")


def naparsuj_html_kod_ze_stringu(html_kod: str) -> BeautifulSoup:
    """
    Funkce prevede html kod ve formatu string na naparsovany objekt Beautifulsoup, ve kterem uz je mozno vyhledavat.

    Beautifulsoup =
    <html><body>
    ... telo ...
    </body></html>

    :param html_kod: "html kod"
    :return: objekt BeautifulSoup
    """
    return BeautifulSoup(html_kod, "html.parser")


def stahni_odkazy_na_zapisy(browser: webdriver, url_soutez: str) -> list:
    """
    Funkce stahne odkazy na vsechny zapisy v soutezi.

    Priklad vystupu:
    ['https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=cb0b2f5b...=1&.htm',
     'https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=2427a903...=1&.htm',
     'https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=a31f61d1...=1&.htm']

    :param browser: webdriver
    :param url_soutez: "url_adresa_souteze"
    :return: [[odkaz1], [odkaz2], [odkaz3], ...]
    """
    odkazy_na_zapisy = []
    odkaz_na_zapis_prvni_cast = "https://is.fotbal.cz"
    html = stahni_html_kod_seleinum(browser, url_soutez)
    # bs_obj = naparsuj_html_kod_ze_stringu(ht.url_souteze)  # Nacteni url_souteze ze souboru
    bs_obj = naparsuj_html_kod_ze_stringu(html)  # Nacteni url_souteze z webu
    vsechny_tabulky = bs_obj.find_all("table", {"class": "soutez-zapasy"})
    for jedna_tabulka in vsechny_tabulky:
        trs = jedna_tabulka.find_all("tr")
        for idx, tr in enumerate(trs):
            if idx == 0:
                continue
            else:
                odkaz_na_zapis_druha_cast = tr.find("a").get("href").replace("..", "")
                odkazy_na_zapisy.append(odkaz_na_zapis_prvni_cast + odkaz_na_zapis_druha_cast)
    # print(odkazy_na_zapisy)
    # print(len(odkazy_na_zapisy))

    return odkazy_na_zapisy


# TODO prepsat return v dostring
def stahni_html_a_naparsuj_vsechny_zapisy_v_soutezi(browser: webdriver, odkazy_na_zapisy: list):
    """
    Funkce stahne ze vsech zapisu html kod, naparsuje do objektu BeautifulSoup a uloží do listu.

    Priklad vystupu:
    [objekt_BeautifulSoup1, objekt_BeautifulSoup2, objekt_BeautifulSoup3, ...]

    :param browser: webdriver
    :param odkazy_na_zapisy: odkazy_na_zapisy
    :return: [[naparsovany_zapis1], [naparsovany_zapis2], [naparsovany_zapis3], ...]
    """
    zapisy = []
    for odkaz_na_zapis in odkazy_na_zapisy:
        str_html = stahni_html_kod_seleinum(browser, odkaz_na_zapis)
        bs_obj = naparsuj_html_kod_ze_stringu(str_html)
        zapisy.append([str_html, bs_obj])

    return [zapisy]


def naparsuj_vsechny_zapisy_ze_stringu_v_listu(str_zapisy: list):
    zapisy = []
    for str_zapis in str_zapisy:
        bs_obj = naparsuj_html_kod_ze_stringu(str_zapis)
        zapisy.append([str_zapis, bs_obj])

    return zapisy


def uloz_vsechny_stazene_html_kody_ve_stringu_do_jsonu(slovnik_se_zapisy):
    # print(slovnik_se_zapisy)
    with open('myfile.json', 'w', encoding='utf8') as json_file:
        json.dump(slovnik_se_zapisy, json_file, indent=2, ensure_ascii=False, allow_nan=True)


def nacti_zapisy_z_jsonu():
    with open('myfile.json', 'r', encoding='utf8') as json_file:
        j = json.load(json_file)
        print(j)
        print(type(j["2022110A4C0104"]))

    zapis = j["2022110A4C0104"]

    return zapis


def ziskej_data_ze_zapisu(naparsovany_zapis):
    data_hlavicka_zapisu = stahni_hlavicku_zapisu(naparsovany_zapis)
    cislo_utkani = data_hlavicka_zapisu[1][0]
    data_vysledky = stahni_tabulku_vysledky(naparsovany_zapis)
    data_hraci_domaci = stahni_tabulku_hraci(naparsovany_zapis, "domaci")
    data_hraci_hoste = stahni_tabulku_hraci(naparsovany_zapis, "hoste")
    data_funkcionari_domaci = stahni_tabulku_funkcionari(naparsovany_zapis, "domaci")
    data_funkcionari_hoste = stahni_tabulku_funkcionari(naparsovany_zapis, "hoste")
    data_osobni_tresty_domaci = stahni_tabulku_osobni_tresty(naparsovany_zapis, "domaci")
    data_osobni_tresty_hoste = stahni_tabulku_osobni_tresty(naparsovany_zapis, "hoste")
    data_strelci_domaci = stahni_tabulku_strelci(naparsovany_zapis, "domaci")
    data_strelci_hoste = stahni_tabulku_strelci(naparsovany_zapis, "hoste")

    print(f"Zpracovávám zápis z utkání číslo: {cislo_utkani}")

    data_zapis = [
        cislo_utkani, data_hlavicka_zapisu, data_vysledky, data_hraci_domaci, data_hraci_hoste, data_funkcionari_domaci,
        data_funkcionari_hoste, data_osobni_tresty_domaci, data_osobni_tresty_hoste, data_strelci_domaci,
        data_strelci_hoste
    ]

    return data_zapis


def vygeneruj_csv_soubor_z_jednoho_zapisu(zpracovany_jeden_zapis):
    cislo_utkani = zpracovany_jeden_zapis[0]
    vygeneruj_csv_soubor(f"{cislo_utkani}_hlavicka_zapisu.csv", zpracovany_jeden_zapis[1])
    vygeneruj_csv_soubor(f"{cislo_utkani}_vysledky.csv", zpracovany_jeden_zapis[2])
    vygeneruj_csv_soubor(f"{cislo_utkani}_hraci_domaci.csv", zpracovany_jeden_zapis[3])
    vygeneruj_csv_soubor(f"{cislo_utkani}_hraci_hoste.csv", zpracovany_jeden_zapis[4])
    vygeneruj_csv_soubor(f"{cislo_utkani}_funkcionari_domaci.csv", zpracovany_jeden_zapis[5])
    vygeneruj_csv_soubor(f"{cislo_utkani}_funkcionari_hoste.csv", zpracovany_jeden_zapis[6])
    vygeneruj_csv_soubor(f"{cislo_utkani}_osobni_tresty_domaci.csv", zpracovany_jeden_zapis[7])
    vygeneruj_csv_soubor(f"{cislo_utkani}_osobni_tresty_hoste.csv", zpracovany_jeden_zapis[8])
    vygeneruj_csv_soubor(f"{cislo_utkani}_strelci_domaci.csv", zpracovany_jeden_zapis[9])
    vygeneruj_csv_soubor(f"{cislo_utkani}_strelci_hoste.csv", zpracovany_jeden_zapis[10])


def stahni_zapis_temp(html_kod_str: str):
    bs_obj = stahni_html_kod_rucne(html_kod_str)
    # print(bs_obj)
    hraci_domaci = bs_obj.find("td", {"class": "hl1 first"})
    # h = hraci_domaci.find_all("tr")
    print(hraci_domaci.text)


def temp_zkusebni_stazeni_zapisu(browser, url_technicky_doprovod):
    # browser.get(url_prvni_zapis)
    # html_1 = browser.page_source
    # time.sleep(2)
    # print(html_1)
    # # html je class str
    # # print(type(html_1))
    # # stahni_zapis_temp(html_1)
    # print("======================================================================================================")
    #
    # browser.get(url_druhy_zapis)
    # html_2 = browser.page_source
    # time.sleep(2)
    # print(html_2)
    # # html je class str
    # # print(type(html_2))
    # # stahni_zapis_temp(html_2)
    # print("======================================================================================================")
    #
    # browser.get(url_treti_zapis)
    # html_3 = browser.page_source
    # time.sleep(2)
    # print(html_3)
    # # html je class str
    # # print(type(html_3))
    # # stahni_zapis_temp(html_3)
    # print("======================================================================================================")

    browser.get(url_technicky_doprovod)
    html_4 = browser.page_source
    time.sleep(2)
    print(html_4)
    # html je class str
    # print(type(html_4))
    # stahni_zapis_temp(html_4)
    print("======================================================================================================")


def naparsuj_zapis(str_zapis):
    return naparsuj_html_kod_ze_stringu(str_zapis)


def stahni_hlavicku_zapisu(naparsovany_zapis: BeautifulSoup) -> list:
    """
    Funkce vygeneruje hlavicku zapisu.

    Priklad vystupu:
    [['Soutěž', 'Kolo', 'Číslo', 'Číslo utkání', 'Ročník', 'Den', 'Čas'],
     ['23  M-2/C', '8', 'A4C', '2022110A4C0806', '2022', '08.10.2022', '10:15']]

    Prvni pozice je hlavicka, v druhe pozici jsou informace o zapase.

    :param naparsovany_zapis: objekt BeautifulSoup
    :return: [[informace_o_zapasu_hlavicka], [informace_o_zapasu]]
    """
    tabulka_hlavicka = naparsovany_zapis.find("div", {"class": "book zapis-report"}).tbody.tbody

    data_hlavicka_hlavicka = ["Číslo utkání", "Soutěž", "Kolo", "Číslo", "Číslo utkání", "Ročník", "Den", "Čas"]

    soutez = tabulka_hlavicka.find("tr", {"class": "first odd"}).td.text.strip("\n ")
    kolo = tabulka_hlavicka.find("tr", {"class": "first odd"}).find("td", {"class": "last"}).text.strip("\n ")
    cislo = tabulka_hlavicka.tr.find_next_sibling().td.text.strip("\n ")
    cislo_utkani = tabulka_hlavicka.tr.find_next_sibling().find("td", {"class": "last"}).text.strip("\n ")
    rocnik = tabulka_hlavicka.find("tr", {"class": "last odd"}).td.text.strip("\n ")
    den_cas = tabulka_hlavicka.find("tr", {"class": "last odd"}).find("td", {"class": "last"}).text.strip("\n ")
    den, cas = den_cas.split()

    data_hlavicka_obsah = [cislo_utkani, soutez, kolo, cislo, cislo_utkani, rocnik, den, cas]

    # print(f"Hlavička zápisu: {[data_hlavicka_hlavicka, data_hlavicka_obsah]}")

    return [data_hlavicka_hlavicka, data_hlavicka_obsah]


def stahni_tabulku_vysledky(naparsovany_zapis: BeautifulSoup) -> list:
    """
    Funkce vygeneruje vysledky utkani.

    Priklad vystupu:
    [['Domácí - číslo', 'Domácí - text', 'Hosté - číslo', 'Hosté - text', ...],
     ['10A0031', 'Sportovní klub Dolní Měcholupy,o.s.', '1040221', 'FK Dukla Jižní Město z.s. "B"', ...]]

    :param naparsovany_zapis: objekt BeautifulSoup
    :return: [[vysledky_zapasu_hlavicka], [vysledky_zapasu]]
    """
    tabulka_vysledky = naparsovany_zapis.find("div", {"class": "book zapis-report"})\
        .find("table", {"class": "vysledky"})

    data_vysledky_hlavicka = [
        "Domácí - číslo", "Domácí - text", "Hosté - číslo", "Hosté - text", "R jméno", "R - číslo", "AR1 - jméno",
        "AR1 - číslo", "AR2 - jméno", "AR2 - číslo", "4R - jméno", "4R - číslo", "DFA - jméno", "DFA - číslo",
        "TD - jméno", "TD - číslo", "Stadion", "Výsledek utkání", "Poločas utkání", "Diváků", "Doba hry 1. poločas",
        "Doba hry 2. poločas", "Povrch hr. pl.", "Zápis vložil - jméno", "Zápis vložil - číslo", "RA"
    ]

    # TODO co je (N) u AR1 a AR2? Odstranit to?
    domaci_cislo_text = tabulka_vysledky.find("tr", {"class": "first odd"}).find("td", {"class": "hl1 first"}).b.text
    domaci_cislo, domaci_text = domaci_cislo_text.split("-")
    domaci_cislo = domaci_cislo.strip()
    domaci_text = domaci_text.strip()
    # Smaze mezery navic mezi nazvem tymu a "B"
    domaci_text = re.sub(r"\s{2,}", " ", domaci_text)
    hoste_cislo_text = tabulka_vysledky.find("tr", {"class": "first odd"}).find("td", {"class": "hl1 last"}).b.text
    hoste_cislo, hoste_text = hoste_cislo_text.split("-")
    hoste_cislo = hoste_cislo.strip()
    hoste_text = hoste_text.strip()
    # Smaze mezery navic mezi nazvem tymu a "B"
    hoste_text = re.sub(r"\s{2,}", " ", hoste_text)
    r_jmeno = tabulka_vysledky.tr.find_next_sibling().td.find_next_sibling().text
    r_cislo = tabulka_vysledky.tr.find_next_sibling().td.find_next_sibling().find_next_sibling().text
    ar1_jmeno = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().td.find_next_sibling().text
    ar1_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().td.find_next_sibling()\
        .find_next_sibling().text
    ar2_jmeno = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().td\
        .find_next_sibling().text
    ar2_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().td\
        .find_next_sibling().find_next_sibling().text
    r4_jmeno = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .td.find_next_sibling().text
    r4_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .td.find_next_sibling().find_next_sibling().text
    dfa_jmeno = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .find_next_sibling().td.find_next_sibling().text
    dfa_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .find_next_sibling().td.find_next_sibling().find_next_sibling().text
    td_jmeno = tabulka_vysledky.find("tr", {"class": "last odd"}).td.find_next_sibling().text
    td_cislo = tabulka_vysledky.find("tr", {"class": "last odd"}).td.find_next_sibling().find_next_sibling().text
    stadion = tabulka_vysledky.tr.find_next_sibling().find("td", {"class": "last"}).text.replace("Stadion: ", "")
    # TODO budou v tabulce pokutove kopy?
    vysledek_utkani_temp = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().td.find_next_sibling()\
        .find_next_sibling().find_next_sibling().find("span", {"class": "vysledek-utkani"})\
        .text.strip("\n ").split("\n")
    vysledek_utkani = vysledek_utkani_temp[0]
    # pokutove_kopy = vysledek_utkani_temp[1].strip(" ")
    polocas_utkani = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find("td", {"class": "last"})\
        .find("span", {"class": "vysledek-utkani"}).text.strip("\n ")
    divaku = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling()\
        .find("td", {"class": "last"}).text.strip("\n ").replace("Diváků: ", "")
    # Odstraneni prebytecnych mezer - odstrani jednu a vice mezer a nahradi ji zadnou mezerou
    divaku = re.sub(r"\s+", "", divaku)
    doba_hry_prvni_polocas, doba_hry_druhy_polocas = tabulka_vysledky.tr.find_next_sibling().find_next_sibling()\
        .find_next_sibling().find_next_sibling().td.find_next_sibling().find_next_sibling().find_next_sibling()\
        .text.replace("Doba hry:", "").split(";")
    doba_hry_prvni_polocas = doba_hry_prvni_polocas.strip()
    doba_hry_druhy_polocas = doba_hry_druhy_polocas.strip()
    povrch_hr_pl = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .find("td", {"class": "last"}).text.replace("Povrch hr. pl.:", "")
    zapis_vlozil_jmeno, zapis_vlozil_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling()\
        .find_next_sibling().find_next_sibling().find_next_sibling().find("td", {"class": "last"})\
        .text.replace("Zápis vložil: ", "").strip("\n ").split("(")
    zapis_vlozil_jmeno = zapis_vlozil_jmeno.strip(" ")
    zapis_vlozil_cislo = zapis_vlozil_cislo.strip(") ")
    # TODO co je RA a v jakém formátu to bude? Zatím tam jsou jen dvě závorky ()
    ra = tabulka_vysledky.find("tr", {"class": "last odd"}).find("td", {"class": "last"}).text\
        .replace("RA:", "").strip("\n ")

    data_vysledky_obsah = [
        domaci_cislo, domaci_text, hoste_cislo, hoste_text, r_jmeno, r_cislo, ar1_jmeno, ar1_cislo, ar2_jmeno,
        ar2_cislo, r4_jmeno, r4_cislo, dfa_jmeno, dfa_cislo, td_jmeno, td_cislo, stadion, vysledek_utkani,
        polocas_utkani, divaku, doba_hry_prvni_polocas, doba_hry_druhy_polocas, povrch_hr_pl, zapis_vlozil_jmeno,
        zapis_vlozil_cislo, ra
    ]

    # print(f"Výsledky zápasu : {[data_vysledky_hlavicka, data_vysledky_obsah]}")

    return [data_vysledky_hlavicka, data_vysledky_obsah]


def stahni_tabulku_hraci(naparsovany_zapis: BeautifulSoup, domaci_hoste: str) -> list:
    """
    Funkce vygeneruje vsechny hrace v zapase.

    Priklad vystupu:
    [['Číslo', 'Příjmení a jméno', 'Post', 'ID', '1. Střídání', '2. Střídání', '1. ŽK', '2. ŽK', 'ČK', 'BR'],
    ['1', 'Benda Filip', 'B', '91051991', '79', '50', '', '', '', '1']]

    V prvni pozici je hlavicka, v druhe a dalsi pozici jsou informace o jednotlivych hracich.

    :param naparsovany_zapis: objekt BeautifulSoup
    :param domaci_hoste: "domaci" / "hoste"
    :return: [[hraci_hlavicka],[hrac1], [hrac2], ...]
    """
    if domaci_hoste == "domaci":
        hraci = naparsovany_zapis.find("div", {"class": "book zapis-report"})\
            .find("table", {"class": "vysledky hraci"}).tbody.tr.td.find_all("tr")
        popis = "Hráči domácí:"
    elif domaci_hoste == "hoste":
        hraci = naparsovany_zapis.find("div", {"class": "book zapis-report"})\
            .find("table", {"class": "vysledky hraci"}).tbody.tr.find("td", {"class": "hl1 last"}).find_all("tr")
        popis = "Hráči hosté:"
    else:
        raise DomaciHosteError("Domaci/hoste error")

    data_hraci = []
    data_hraci_hlavicka = [
        "Číslo", "Příjmení a jméno", "Post", "ID", "1. Střídání", "2. Střídání", "1. ŽK", "2. ŽK", "ČK", "BR"
    ]
    data_hraci.append(data_hraci_hlavicka)

    # Stazeni dat jednoho hrace
    for hrac in hraci:
        jeden_hrac = []
        zapis_do_statistik = False
        tds = hrac.find_all("td")
        for idx, td in enumerate(tds, start=1):
            if idx == 2:
                temp = td.text.strip().split("\n")
                temp[0] = temp[0].strip()
                temp[1] = temp[1].strip()
                jeden_hrac.extend(temp)
            else:
                jeden_hrac.append(td.text)
            zapis_do_statistik = True

        if zapis_do_statistik:
            data_hraci.append(jeden_hrac)

    # print(f"{popis} {data_hraci}")

    return data_hraci


def stahni_tabulku_funkcionari(naparsovany_zapis: BeautifulSoup, domaci_hoste: str) -> list:
    """
    Funkce vygeneruje vsechny funkcionare v zapase.

    Priklad vystupu:
    [['Funkce', 'Příjmení a jméno', 'ID', '1. ŽK', '2. ŽK'],
    ['Hlavní pořadatel', 'Chadima Václav', '54030121', '', '']]

    V prvni pozici je hlavicka, v druhe a dalsi pozici jsou informace o jednotlivych funkcionarich.

    :param naparsovany_zapis: objekt BeautifulSoup
    :param domaci_hoste: "domaci" / "hoste"
    :return: [[funkcionari_hlavicka],[funkcionar1], [funkcionar2], ...]
    """
    if domaci_hoste == "domaci":
        funkcionari = naparsovany_zapis.find("div", {"class": "book zapis-report"}).table\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find("td", {"class": "hl1 first"}).find_all("tr")
        popis = "Funkcionáři domácí:"
    elif domaci_hoste == "hoste":
        funkcionari = naparsovany_zapis.find("div", {"class": "book zapis-report"}).table\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find("td", {"class": "hl1 last"}).find_all("tr")
        popis = "Funkcionáři hosté:"
    else:
        raise DomaciHosteError()

    data_funkcionari = []
    data_funkcionari_hlavicka = ["Funkce", "Příjmení a jméno", "ID", "1. ŽK", "2. ŽK"]
    data_funkcionari.append(data_funkcionari_hlavicka)

    for idx, tr in enumerate(funkcionari):
        if idx == 0:
            continue
        else:
            tds = tr.find_all("td")
            jeden_funkcionar = []
            for td in tds:
                temp = td.text.strip().split("\n")
                jeden_funkcionar.extend(temp)
            data_funkcionari.append(jeden_funkcionar)

    # print(f"{popis} {data_funkcionari}")

    return data_funkcionari


def stahni_tabulku_osobni_tresty(naparsovany_zapis: BeautifulSoup, domaci_hoste: str) -> list:
    """
    Funkce vygeneruje vsechny osobni tresty v zapase.

    Priklad vystupu:
    [['Příjmení a jméno', 'ID', 'Minuta', 'Popis'], ['Přída Jakub', '05010125', '83', 'Červená karta během zápasu,
    Druhé napomenutí během utkání, První ŽK hráč D6 obdržel v 75. minutě poté, co bezohledným způsobem podrazil nohy
    hráči H8 v PÚ. Druhou ŽK hráč obdržel v 83. minutě za bezohledné kopnutí.']]

    V prvni pozici je hlavicka, v druhe a dalsi pozici jsou informace o jednotlivych osobnich trestech.

    :param naparsovany_zapis: objekt BeautifulSoup
    :param domaci_hoste: "domaci" / "hoste"
    :return: [[osobni_tresty_hlavicka],[osobni_trest1], [osobni_trest2], ...]
    """
    if domaci_hoste == "domaci":
        osobni_tresty = naparsovany_zapis.find("div", {"class": "book zapis-report"}).table\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find("td", {"class": "hl1 first"}).find_all("tr")
        popis = "Osobní tresty domácí:"
    elif domaci_hoste == "hoste":
        osobni_tresty = naparsovany_zapis.find("div", {"class": "book zapis-report"}).table\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find("td", {"class": "hl1 last"}).find_all("tr")
        popis = "Osobní tresty hosté:"
    else:
        raise DomaciHosteError

    data_osobni_tresty = []
    data_osobni_tresty_hlavicka = ["Příjmení a jméno", "ID", "Minuta", "Popis"]
    data_osobni_tresty.append(data_osobni_tresty_hlavicka)

    for idx, tr in enumerate(osobni_tresty):
        if idx == 0:
            continue
        else:
            tds = tr.find_all("td")
            jeden_osobni_trest = []
            if idx % 2 != 0:
                for td in tds:
                    temp = td.text.strip().split("\n")
                    jeden_osobni_trest.extend(temp)
            else:
                for td in tds:
                    temp = td.text.strip().split("\n")
                    data_osobni_tresty[idx-1].extend(temp)

            data_osobni_tresty.append(jeden_osobni_trest)

    # TODO mam v listu jedny prazdne zavorky navic
    # print(f"{popis} {data_osobni_tresty}")

    return data_osobni_tresty


def stahni_tabulku_strelci(naparsovany_zapis: BeautifulSoup, domaci_hoste: str) -> list:
    """
    Funkce vygeneruje vsechny strelce v zapase.

    Priklad vystupu:
    [['Pořadí', 'Příjmení a jméno', 'Typ', 'ID', 'Minuta'], ['1', 'Gunár Milan', 'Branka', '93092453', '52']]

    V prvni pozici je hlavicka, v druhe a dalsi pozici jsou informace o jednotlivych brankach.

    Promenna domaci_hoste vybere, kteri strelci se maji vygenerovat.

    :param naparsovany_zapis: objekt BeautifulSoup
    :param domaci_hoste: "domaci" / "hoste"
    :return: [[strelci_hlavicka],[branka1], [branka2], ...]
    """
    if domaci_hoste == "domaci":
        # "table", class_="vysledky hraci", id="" - najde vsechny "table" s "class", ale bez "id"
        strelci = naparsovany_zapis.find("div", {"class": "book zapis-report"}).table\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find("td", {"class": "hl1 first"}).find_all("tr")
        popis = "Střelci domácí:"
    elif domaci_hoste == "hoste":
        # "table", class_="vysledky hraci", id="" - najde vsechny "table" s "class", ale bez "id"
        strelci = naparsovany_zapis.find("div", {"class": "book zapis-report"}).table\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="")\
            .find_next_sibling("table", class_="vysledky hraci", id="") \
            .find("td", {"class": "hl1 last"}).find_all("tr")
        popis = "Střelci hosté:"
    else:
        raise DomaciHosteError("Domaci/hoste error")

    data_strelci = []
    data_strelci_hlavicka = ["Pořadí", "Příjmení a jméno", "Typ", "ID", "Minuta"]
    data_strelci.append(data_strelci_hlavicka)

    for idx, tr in enumerate(strelci):
        if idx == 0:
            continue
        else:
            tds = tr.find_all("td")
            # print(tds)
            jeden_strelec = []
            for td in tds:
                temp = td.text.strip("\n ")
                jeden_strelec.append(temp)
            data_strelci.append(jeden_strelec)

    # print(f"{popis} {data_strelci}")

    return data_strelci


def vygeneruj_csv_soubor(nazev_csv_souboru: str, data_pro_csv_tabulku: list[list]) -> None:
    """
    Funkce vytvori .csv soubor.

    :param nazev_csv_souboru: "nazev_csv_souboru.csv"
    :param data_pro_csv_tabulku: [[], [], [], [], ...]
    :return: None
    """
    print(f"Ukladam stazena data do souboru: {nazev_csv_souboru}")
    # Nastaveni oddelovace na středník
    csv.register_dialect('myDialect', delimiter=';', quoting=csv.QUOTE_ALL)
    # Nachystani noveho souboru na zapis
    nove_csv = open(nazev_csv_souboru, mode="w", newline='', encoding='utf-8')
    # Vytvoreni noveho csv souboru
    zapisovac = csv.writer(nove_csv, dialect='myDialect')
    # Zaspis stazenych dat do csv souboru
    for idx in range(len(data_pro_csv_tabulku)):
        zapisovac.writerow(data_pro_csv_tabulku[idx])
    # Uzavreni csv souboru
    nove_csv.close()


def main():
    sitekey = "6LdleRoUAAAAAFPzy5u9zlmtLy4qKT_Jb8EItoad"
    url_s_capcha = "https://is.fotbal.cz/security-valid.aspx?hidemenu=1&ret=%2fzapasy%2fzapis-o-utkani-report.aspx%3fzapas%3d18c8bd4f-cff6-40be-a67a-c30428d3e027%26zapis%3d1%26noprint%3d1%26btnprint%3d1%26.htm"
    prvni_cast_url = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=cb0b2f5b-07ac-4d51-8064-64336b349e40&zapis=1&noprint=1&btnprint=1&.htm"
    url_soutez = "https://is.fotbal.cz/souteze/detail-souteze.aspx?req=ae9809e0-5712-4abd-b99a-997cf9d3d8c6&fbclid=IwAR3NizZ2RB1Ffj8fObluwhR9wlFEeCYRB7ihXm8mCwy308cDMMzQMfMKuaU"

    url_prvni_zapis = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=cb0b2f5b-07ac-4d51-8064-64336b349e40&zapis=1&noprint=1&btnprint=1&.htm"
    url_druhy_zapis = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=2427a903-53a5-4b1b-b245-e53521038f7d&zapis=1&noprint=1&btnprint=1&.htm"
    url_treti_zapis = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=a31f61d1-53c0-4daf-9121-765a1e6ad2ee&zapis=1&noprint=1&btnprint=1&.htm"
    url_technicky_doprovod = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=5ca6a76a-5561-4aeb-807a-9b57c700a209&zapis=1&noprint=1&btnprint=1&.htm"

    url_kostelec_sezona_2022 = "https://is.fotbal.cz/souteze/detail-souteze.aspx?req=4d854270-1b9d-4434-b8d8-dc9a9ac1d9fe"
    url_kostelec_sezona_2021 = "https://is.fotbal.cz/souteze/detail-souteze.aspx?req=c3bd1317-a331-4dda-a7ec-785bab482331"
    url_kostelec_sezona_2020 = "https://is.fotbal.cz/souteze/detail-souteze.aspx?req=3b4717df-3130-4146-bff2-b79c31cf5209"

    url_nusle_sezona_2022 = "https://is.fotbal.cz/souteze/detail-souteze.aspx?req=ae9809e0-5712-4abd-b99a-997cf9d3d8c6"
    url_nusle_sezona_2021 = "https://is.fotbal.cz/souteze/detail-souteze.aspx?req=fd1c5978-eaa9-4a28-8daf-70bbe8e6fffb"
    url_nusle_sezona_2020 = "https://is.fotbal.cz/souteze/detail-souteze.aspx?req=c4556c06-706e-419e-a6dd-911f6776e19d"

    # Otevri url s capcha
    # browser = webdriver.Chrome()
    # odkazy_na_zapisy = stahni_odkazy_na_zapisy(browser, url_soutez)

    # browser.get(url_s_capcha)

    # capcha_solver(browser, sitekey, url_s_capcha)

    # browser = ""

    # vsechny_zapisy_v_soutezi_html = stahni_html_a_naparsuj_vsechny_zapisy_v_soutezi(browser, odkazy_na_zapisy)

    # # Nacteni z jsonu - zatim nefunguje
    # hodnoty_z_jsonu = nacti_zapisy_z_jsonu()
    # vsechny_zapisy_v_soutezi_html = naparsuj_vsechny_zapisy_ze_stringu_v_listu(hodnoty_z_jsonu)

    # Zpracuje vsechny rucne stazene zapisy
    vsechny_zapisy_v_soutezi_html_str = [ht.prvni_zapis, ht.druhy_zapis, ht.treti_zapis]
    vsechny_zapisy_v_soutezi_html = naparsuj_vsechny_zapisy_ze_stringu_v_listu(vsechny_zapisy_v_soutezi_html_str)

    slovnik_se_zapisy = {}
    # Zpracuje data ze vsech zapisu a ulozi je do csv souboru
    for str_jeden_zapis, naparsovany_jeden_zapis in vsechny_zapisy_v_soutezi_html:
        zpracovany_jeden_zapis = ziskej_data_ze_zapisu(naparsovany_jeden_zapis)
        cislo_utkani = zpracovany_jeden_zapis[0]
        vygeneruj_csv_soubor_z_jednoho_zapisu(zpracovany_jeden_zapis)
        slovnik_se_zapisy[cislo_utkani] = str_jeden_zapis

    # uloz_vsechny_stazene_html_kody_ve_stringu_do_jsonu(slovnik_se_zapisy)



    # bs_obj = stahni_html_kod(prvni_cast_url)
    # print(bs_obj)

    # temp_zkusebni_stazeni_zapisu(browser, url_technicky_doprovod)

    # #
    # naparsovany_zapis = naparsuj_zapis(ht.druhy_zapis)
    # # naparsovany_zapis = naparsuj_zapis(ht.zapis_s_osobnimi_tresty)
    # data_vysledky = stahni_tabulku_vysledky(naparsovany_zapis)
    # vygeneruj_csv_soubor(f"000_vysledky.csv", data_vysledky)

    # Cas, po ktery zustane prohlizec otevreny po vsech akcich
    # time.sleep(1000)


if __name__ == "__main__":
    main()
