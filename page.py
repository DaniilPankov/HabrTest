import time
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



def check_negative_search(driver):
    search_bar = driver.find_element(By.CLASS_NAME, 'tm-input-text-decorated__input')
    search_bar.send_keys('hdfjdjskcjdenhcjudjcikdjjvjdjhjcjdjcjd')
    search_bar.send_keys(Keys.ENTER)
    time.sleep(3)
    txt = driver.find_element(By.CLASS_NAME, 'tm-empty-placeholder__text').text
    time.sleep(3)
    return txt == 'К сожалению, здесь пока нет ни одной публикации'


def check_positive_search(driver):
    search_bar = driver.find_element(By.CLASS_NAME, 'tm-input-text-decorated__input')
    search_bar.send_keys('Структура Flutter-приложения: feature-first или layer-first')
    search_bar.send_keys(Keys.ENTER)
    time.sleep(3)
    txt = driver.find_element(By.CLASS_NAME, 'searched-item').text
    time.sleep(3)
    return txt == 'Структура Flutter-приложения: feature-first'


def check_user(driver):
    driver.find_element(By.LINK_TEXT, 'Хабр').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Авторы').click()
    time.sleep(3)
    search = driver.find_element(By.CLASS_NAME, 'tm-input-text-decorated__input')
    search.send_keys('@divolko3')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'tm-user-snippet__nickname').click()
    time.sleep(3)
    try:
        inf = driver.find_element(By.CLASS_NAME, 'tm-badges__badge').text
        time.sleep(3)
    except NoSuchElementException:
        return False
    return inf == 'Захабренный'


def check_company(driver):
    driver.find_element(By.LINK_TEXT, 'Хабр').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Компании').click()
    time.sleep(3)
    search = driver.find_element(By.CLASS_NAME, 'tm-input-text-decorated__input')
    search.send_keys('Домклик')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'searched-item').click()
    time.sleep(3)
    try:
        inf = driver.find_element(By.CLASS_NAME, 'tm-company-profile__categories-text').text
        time.sleep(3)
    except NoSuchElementException:
        return False
    return inf == 'Веб-разработка'


def check_authorization(driver):
    driver.get('https://account.habr.com/login/?state=c5b3b7d5f77a37a7893e4d2c9ada2f8c&consumer=habr&host=habr.com&hl=ru_RU')
    time.sleep(3)
    user = driver.find_element(By.ID, 'email_field')
    user.send_keys('test@gmail.com')
    password = driver.find_element(By.ID, 'password_field')
    password.send_keys('teeeeesttttt')
    driver.find_element(By.NAME, 'go').click()
    time.sleep(3)
    try:
        driver.find_element(By.NAME, 'go')
        return True
    except NoSuchElementException:
        return False
