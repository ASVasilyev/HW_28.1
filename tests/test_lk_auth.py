from selenium.webdriver.common.by import By
from settings import valid_email, valid_password, valid_phone
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from class_for_wait import element_has_css_class
import pytest


# Авторизация по валидным почтовому адресу и паролю
def test_auth_with_email(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    # Нажимаем на таб Почта
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # проверяем что таб Почта активен
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
    # Вводим почту
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Ждем когда окажемся на главной странице пользователя
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Скиллфактори\nТестер')
    )
    assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Скиллфактори"
    assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Тестер"


# Авторизация по валидным номеру телефона и паролю
def test_auth_with_phone(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-phone')))
    # проверяем что таб Телефон активен по умолчанию
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-phone'), "rt-tab--active"))
    # Вводим телефон
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Ждем когда окажемся на главной странице пользователя
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Скиллфактори\nТестер')
    )
    assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Скиллфактори"
    assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Тестер"


# Авторизация по почтовому адресу некорректного формата
@pytest.mark.parametrize("mail", ['kalice7865@cdeter', '7865@cdeter.com', 'kalice7865@@cdeter.com'],
                         ids=['wrong mail', 'invalid mail', 'double@'])
def test_auth_mail_wrong_user_name(driver, mail):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    # Нажимаем на таб Почта
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # проверяем что таб Почта активен
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
    # Вводим почту
    driver.find_element(By.ID, 'username').send_keys(mail)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Ждем когда окажемся на главной странице пользователя
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
    )
    # проверяем ссылка Забыл пароль оранжевая
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))


# Авторизация по пустому почтовому адресу или адресу, который состоит из пробелов
@pytest.mark.parametrize("mail", ['', '          '], ids=['empty', 'only blanks'])
def test_auth_mail_empty_mail(driver, mail):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    # Нажимаем на таб Почта
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # проверяем что таб Почта активен
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
    # Вводим адрес
    driver.find_element(By.ID, 'username').send_keys(mail)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Ждем когда окажемся на главной странице пользователя
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'rt-input-container__meta--error'),
                                         'Введите адрес, указанный при регистрации')
    )


# Проверка ввода пустого пароля или пароля из пробелов
@pytest.mark.parametrize("passw", ['', '          '], ids=['empty', 'only blanks'])
def test_auth_phone_empty_pass(driver, passw):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    # Нажимаем на таб Почта
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # проверяем что таб Почта активен
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
    # Вводим почту
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(passw)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Ждем когда окажемся на главной странице пользователя
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'rt-input-container__meta--error'), 'Введите пароль')
    )


# Авторизация по неправильному паролю
@pytest.mark.parametrize("passw", ['9999999999', 'invalidpass'],
                         ids=['wrong password number', 'invalid password letters'])
def test_auth_phone_wrong_pass(driver, passw):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    # Нажимаем на таб Почта
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # проверяем что таб Почта активен
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
    # Вводим почту
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(passw)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Ждем когда окажемся на главной странице пользователя
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
    )
    # проверяем ссылка Забыл пароль оранжевая
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))


# Авторизация по номеру некорректного формата
@pytest.mark.parametrize("phone", ['9', '+9999999'], ids=['one digit', 'invalid format'])
def test_auth_phone_invalid_format(driver, phone):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-phone')))
    # Вводим телефон
    driver.find_element(By.ID, 'username').send_keys(phone)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Проверяем текст ошибки
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'rt-input-container__meta--error'),
                                                                     'Неверный формат телефона'))


# Авторизация по незарегистрированному номеру
@pytest.mark.parametrize("phone", ['+79105552211', '555555555555'], ids=['wrong phone', 'invalid phone 11 number'])
def test_auth_phone_wrong_user_name(driver, phone):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-phone')))
    # Вводим телефон
    driver.find_element(By.ID, 'username').send_keys(phone)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Ждем когда окажемся на главной странице пользователя
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
    )
    # проверяем ссылка Забыл пароль оранжевая
    wait = WebDriverWait(driver, 10)
    wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))
