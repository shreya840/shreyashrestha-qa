#importing various python statements,classes from selenium library
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Firstly I choose  Edge as a web browser.
driver = webdriver.Edge()
# This is the website address I want to go to.
url ="https://www.saucedemo.com/v1/index.html"
#These are the username and password which we use to login.
username = "standard_user"
password = "secret_sauce"

#Here I am telling the web browser to go to the web address
driver.get(url)

#In this I am finding the input field where you type your username by using the XPATH.
username_field = driver.find_element(By.XPATH,"//input[@id='user-name']")
password_field = driver.find_element(By.XPATH,"//input[@id='password']")
login_field = driver.find_element(By.XPATH,"//input[@id='login-button']")

#Here it types the username into the username box.
username_field.send_keys(username)
password_field.send_keys(password)
# Click the login button.
login_field.click()

#Find the dropdown menu that sorts the products.Choose the option "Price (low to high)" from the dropdown menu.
#Wait for 3 seconds to let the page update
dropdown_list =Select(driver.find_element(By.XPATH,"//select[contains(@class,'product_sort_container')]"))
dropdown_list.select_by_visible_text("Price (low to high)")
time.sleep(3)

#finding the product and adding it to cart
product_id1 = driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
product_id1.click()
time.sleep(3)
addtocart = driver.find_element(By.XPATH,"//button[contains(@class,'btn_primary btn_inventory')]")
addtocart.click()
time.sleep(2)
#Going back to the product page
back_button = driver.find_element(By.XPATH,"//button[contains(@class,'inventory_details_back_button')]")
back_button.click()

#finding the second product and adding it to cart
product_id2 = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
product_id2.click()
time.sleep(4)
addtocart2 = driver.find_element(By.XPATH,"//button[contains(@class,'btn_primary btn_inventory')]")
addtocart2.click()
#Back to product page
back_button2 = driver.find_element(By.XPATH,"//button[contains(@class,'inventory_details_back_button')]")
back_button2.click()

#Clicking on shopping cart icon
shopping_cart = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link fa-layers fa-fw']")
shopping_cart.click()
time.sleep(3)
#removing the first product
erase_btn = driver.find_element(By.XPATH,"//button[@class='btn_secondary cart_button']")
erase_btn.click()

#Clicking on a continue button by finding its Xpath
con_btn = driver.find_element(By.XPATH,"//a[@class='btn_action checkout_button']")
con_btn.click()

#Assigning the variables with proper input data.
first_name = "shreya"
last_name = "shrestha"
postal_code = "44802"
#locating the Xpaths of the input fields
first_field = driver.find_element(By.XPATH,"//input[@id='first-name']")
last_field = driver.find_element(By.XPATH,"//input[@id='last-name']")
postal_field = driver.find_element(By.XPATH,"//input[@id='postal-code']")
#sending input data into input fields
first_field.send_keys(first_name)
last_field.send_keys(last_name)
postal_field.send_keys(postal_code)
time.sleep(3)
cont_btn = driver.find_element(By.XPATH,"//input[@class='btn_primary cart_button']")
cont_btn.click()

finish_btn = driver.find_element(By.XPATH,"//a[@class='btn_action cart_button' and text()='FINISH']")
finish_btn.click()

menu_btn = driver.find_element(By.XPATH,"//button[text()='Open Menu']")
menu_btn.click()
time.sleep(3)
about_button= driver.find_element(By.XPATH,"//a[@id='about_sidebar_link']")
about_button.click()

driver.back()

logout_btn = driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']")
logout_btn.click()


time.sleep(3)
driver.quit()