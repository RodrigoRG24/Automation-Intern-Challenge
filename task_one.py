import time

import selenium
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_data = {
    'email': 'rodrigoray2@example.com',
    'password': 'Password123',
    'first_name': 'Rodrigo',
    'last_name': 'Raymundo',
    'cellphone': '987654321',
    'address': 'Av. La Marina 123',
    'city': 'Lima',
    'postcode': '12345',
}

url = 'https://demo.evershop.io/'
path_driver = os.getenv('PATH_DRIVER')
service = Service(executable_path=path_driver)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get(url)

login = driver.find_element(By.XPATH, '//a[@href="/account/login"]')
login.click()

#Register
create_account_link = driver.find_element(By.XPATH, '//a[@href="/account/register"]')
create_account_link.click()

full_name_input_register = driver.find_element(By.XPATH, '//input[@name="full_name"]')
full_name = f"{user_data['first_name']} {user_data['last_name']}"
full_name_input_register.send_keys(full_name)

email_input_register = driver.find_element(By.XPATH, '//input[@name="email"]')
email_input_register.send_keys(user_data['email'])

password_input_register = driver.find_element(By.XPATH, '//input[@name="password"]')
password_input_register.send_keys(user_data['password'])

sign_up_button = driver.find_element(By.XPATH, '//button/span[text()="SIGN UP"]')
sign_up_button.click()

#Log In
element = driver.find_element(By.XPATH, '//a[@href="/account/login"]')
element.click()

email_input_login = driver.find_element(By.XPATH, '//input[@name="email"]')
email_input_login.send_keys(user_data['email'])

password_input_login = driver.find_element(By.XPATH, '//input[@name="password"]')
password_input_login.send_keys(user_data['password'])

sing_in_button = driver.find_element(By.XPATH, '//button/span[text()="SIGN IN"]')
sing_in_button.click()

#Add to Cart
#Kids shoes

shop_kids_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/kids"]'))
)
shop_kids_button.click()

first_shoe_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/kids/coated-glitter-chuck-taylor-all-star-71"]'))
)
first_shoe_button.click()

first_shoe_qty = driver.find_element(By.XPATH, '//input[@name="qty"]')
first_shoe_qty.clear()
first_shoe_qty.send_keys("3")

first_shoe_size = driver.find_element(By.XPATH, '//a[text()="S"]')
first_shoe_size.click()

time.sleep(3)

first_shoe_color = driver.find_element(By.XPATH, '//a[text()="Black"]')
first_shoe_color.click()

time.sleep(3)

first_shoe_add = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button/span[text()="ADD TO CART"]'))
)
first_shoe_add.click()

#Women shoes
shop_women_button = driver.find_element(By.XPATH, '//a[text()="Women"]')
shop_women_button.click()

second_shoe_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/women/nike-air-presto-by-you-138"]'))
)
second_shoe_button.click()

second_shoe_qty = driver.find_element(By.XPATH, '//input[@name="qty"]')
second_shoe_qty.clear()
second_shoe_qty.send_keys("2")

second_shoe_size = driver.find_element(By.XPATH, '//a[text()="L"]')
second_shoe_size.click()

time.sleep(3)

second_shoe_color = driver.find_element(By.XPATH, '//a[text()="White"]')
second_shoe_color.click()

time.sleep(3)

second_shoe_add = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button/span[text()="ADD TO CART"]'))
)
second_shoe_add.click()

#Men shoes
shop_men_button = driver.find_element(By.XPATH, '//a[text()="Men"]')
shop_men_button.click()

third_shoe_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/men/strutter-shoes-45"]'))
)
third_shoe_button.click()

third_shoe_qty = driver.find_element(By.XPATH, '//input[@name="qty"]')
third_shoe_qty.clear()
third_shoe_qty.send_keys("4")

third_shoe_size = driver.find_element(By.XPATH, '//a[text()="XL"]')
third_shoe_size.click()

time.sleep(3)

third_shoe_color = driver.find_element(By.XPATH, '//a[text()="Grey"]')
third_shoe_color.click()

time.sleep(3)

second_shoe_add = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button/span[text()="ADD TO CART"]'))
)
second_shoe_add.click()

#Cart
cart = driver.find_element(By.XPATH, '//a[@href="/cart"]')
cart.click()

coupon_input = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="coupon"]'))
)
coupon_input.send_keys("DISCOUNT20")

apply_button = driver.find_element(By.XPATH, '//button/span[text()="Apply"]')
apply_button.click()

checkout = driver.find_element(By.XPATH, '//a[@href="/checkout"]')
checkout.click()

time.sleep(3)

full_name_input = driver.find_element(By.XPATH, '//input[@name="address[full_name]"]')
full_name_input.send_keys(f"{user_data['first_name']} {user_data['last_name']}")

telephone_input = driver.find_element(By.XPATH, '//input[@name="address[telephone]"]')
telephone_input.send_keys(user_data['cellphone'])

address_input = driver.find_element(By.XPATH, '//input[@name="address[address_1]"]')
address_input.send_keys(user_data['address'])

city_input = driver.find_element(By.XPATH, '//input[@name="address[city]"]')
city_input.send_keys(user_data['city'])

country_select = driver.find_element(By.XPATH, '//select[@name="address[country]"]')
country_select.click()
country_option = driver.find_element(By.XPATH, '//select[@name="address[country]"]/option[@value="CN"]')
country_option.click()

province_select = driver.find_element(By.XPATH, '//select[@name="address[province]"]')
province_select.click()
province_option = driver.find_element(By.XPATH, '//select[@name="address[province]"]/option[@value="CN-50"]')
province_option.click()

postcode_input = driver.find_element(By.XPATH, '//input[@name="address[postcode]"]')
postcode_input.send_keys(user_data['postcode'])

time.sleep(3)

express_delivery_option = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//span[text()="Express Delivery - $15.00"]'))
)
express_delivery_option.click()

continue_payment_button = driver.find_element(By.XPATH, '//button/span[text()="Continue to payment"]')
continue_payment_button.click()

payment_method = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="checkoutPaymentForm"]/div[3]/div[3]/div/div/div/div[1]/a'))
)
payment_method.click()

iframe = driver.find_element(By.XPATH, '//*[@id="card-element"]/div/iframe')
driver.switch_to.frame(iframe)

time.sleep(5)

card_number_input = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')
card_number_input.send_keys('4242 4242 4242 4242')

card_expiry_input = driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[1]/span/span/input')
card_expiry_input.send_keys('0244')

card_cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[2]/span/span/input')
card_cvc_input.send_keys('242')

driver.switch_to.default_content()

place_holder_button = driver.find_element(By.XPATH, '//*[@id="checkoutPaymentForm"]/div[5]/button')
place_holder_button.click()

time.sleep(10)

contact_info = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[1]'))
).text
print("\n" + contact_info)

shipping_address = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[2]').text
print("\n" + shipping_address)

payment_method = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[2]/div[1]').text
print("\n" + payment_method)

billing_address = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[2]/div[2]').text
print("\n" + billing_address)

tbody = driver.find_element(By.XPATH, '//*[@id="summary-items"]/table/tbody').text
print("\n" + tbody)
