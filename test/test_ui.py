import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

@allure.title("Проверка поиска книги")
def test_search_book():
    driver = webdriver.Chrome()
    driver.maximize_window()

    with allure.step("Открываем сайт"):
        driver.get("https://www.chitai-gorod.ru/")

    with allure.step("Находим строку поиска и вводим запрос"):
        search_input = driver.find_element(By.CSS_SELECTOR, input_name="search"type="text">)
        search_input.send_keys("Гарри Поттер")
        search_input.send_keys(Keys.RETURN)

    with allure.step("Проверяем, что результаты поиска отображаются"):
        results = driver.find_elements(By.CSS_SELECTOR, ".product-card")
        assert len(results) > 0, "Результаты поиска не отображаются."

    driver.quit()



    import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title("Добавление книги в корзину")
def test_add_book_to_cart():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    try:
        with allure.step("Открываем сайт"):
            driver.get("https://www.chitai-gorod.ru/")

        with allure.step("Ищем книгу по названию"):
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, input_name="search"type="text">)))
            search_input.send_keys("Гарри Поттер")
            search_input.send_keys(Keys.RETURN)

        with allure.step("Выбираем первый результат из поиска"):
            first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-card")))
            first_result.click()

        with allure.step("Ждем страницу книги и нажимаем 'Добавить в корзину'"):
            add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-to-cart']")))
            add_button.click()

        with allure.step("Проверяем, что книга добавилась в корзину"):
            # Открываем корзину по необходимости или проверяем сообщение
            cart_count = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-count")))
            count_text = cart_count.text
            assert int(count_text) > 0, "Корзина пуста после добавления книги."

        # Опционально, можно проверить содержимое корзины или сообщение подтверждения

    finally:
        driver.quit()



        import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title("Оформление заказа на сайте")
def test_checkout():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    try:
        with allure.step("Открываем сайт"):
            driver.get("https://www.chitai-gorod.ru/")
        
        # Предварительно: добавляем товар в корзину (можно использовать предыдущий тест или вставить сюда)
        with allure.step("Ищем книгу и добавляем в корзину"):
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, input_name="search"type="text">)))
            search_input.send_keys("Гарри Поттер")
            search_input.send_keys(Keys.RETURN)
            first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-card")))
            first_result.click()
            add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-to-cart']")))
            add_button.click()

        # Открытие корзины
        with allure.step("Открываем корзину"):
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-basket")))
            cart_icon.click()

        # Переход к оформлению заказа
        with allure.step("Переходим к оформлению заказа"):
            checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='checkout']")))
            checkout_button.click()

        # Заполнение данных заказа
        with allure.step("Заполняем данные доставки"):
            name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='name']")))
            name_input.send_keys("Иванов Иван")
            phone_input = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
            phone_input.send_keys("+79001234567")
            email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
            email_input.send_keys("test@example.com")
            address_input = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
            address_input.send_keys("Москва, Тверская, д.1")
            # Выберите способ оплаты и другие параметры по необходимости

        # Подтверждаем заказ
        with allure.step("Подтверждаем заказ"):
            confirm_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='confirm-order']")
            confirm_button.click()

        # Проверка успешного оформления
        with allure.step("Проверяем, что заказ оформлен успешно"):
            success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Спасибо за заказ')]") ))
            assert success_message.is_displayed(), "Сообщение о подтверждении заказа не найдено."

    finally:
        driver.quit()



import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title("Регистрация нового пользователя")
def test_registration():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    try:
        with allure.step("Открываем сайт"):
            driver.get("https://www.chitai-gorod.ru/")

        with allure.step("Переходим к форме регистрации"):
            # Найти кнопку или ссылку "Войти / Регистрация"
            <button class="header-controls_btn" aria -label="Меню профиля">
            <span class="header-controls_icon-wrapper"> </span>
            <span class="header-controls_text">Войти</span>
            </button>
            button.click()

        with allure.step("Выбираем регистрацию"):
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Регистрация")))
            register_link.click()

        with allure.step("Заполняем форму регистрации"):
            name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='name']")))
            name_input.send_keys("Тестовый Пользователь")
            email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
            email_input.send_keys("testuser123@example.com")
            password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
            password_input.send_keys("StrongPassword123")
            confirm_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='confirm_password']")
            confirm_password_input.send_keys("StrongPassword123")
        
        with allure.step("Отправляем форму регистрации"):
            register_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            register_submit.click()

        with allure.step("Проверка успешной регистрации"):
            # Ожидаем появления сообщения или перехода в личный кабинет
            success_message = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Вы успешно зарегистрировались') or contains(text(), 'Личный кабинет')]")
            ))
            assert success_message.is_displayed(), "Регистрация не прошла успешно"

    finally:
        driver.quit()



        import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title("Редактирование товара в корзине")
def test_edit_product_in_cart():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    try:
        with allure.step("Открываем сайт"):
            driver.get("https://www.chitai-gorod.ru/")

        # Предварительно: добавляем товар в корзину
        with allure.step("Ищем книгу и добавляем в корзину"):
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, input_name="search"type="text">)))
            search_input.send_keys("Гарри Поттер")
            search_input.send_keys(Keys.RETURN)
            first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-card")))
            first_result.click()
            add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-to-cart']")))
            add_button.click()

        # Переходим в корзину
        with allure.step("Переходим в корзину"):
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-basket")))
            cart_icon.click()

        # Редактируем количество товара
        with allure.step("Редактируем количество товара"):
            quantity_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='cart-quantity']")))
            # Например, увеличить на 1
            quantity_input.clear()
            quantity_input.send_keys("2")
            # Нажимаем кнопку обновления или сразу уходим из поля (зависит от реализации сайта)
            quantity_input.send_keys(Keys.ENTER)

        # Проверяем, что количество обновилось
        with allure.step("Проверяем обновление количества"):
            updated_quantity = wait.until(EC.text_to_be_present_in_element_value(
                (By.CSS_SELECTOR, "input[data-testid='cart-quantity']"), "2"))
            assert updated_quantity, "Количество товара не обновилось"

    finally:
        driver.quit()
        