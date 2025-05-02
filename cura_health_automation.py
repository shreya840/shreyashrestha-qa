from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This line tells the program to use the Microsoft Edge browser for automation.
driver = webdriver.Edge()
url = "https://katalon-demo-cura.herokuapp.com/"
driver.get(url)
#These lines store the username and password that we will use to log in.
username = "John Doe"
password = "ThisIsNotAPassword"

#This line stores the initial comment we want to add to the appointment.
cmt = "make an appointment for ent"

#This line finds the button with the ID "menu-toggle" which is the menu button and clicks it.
menu_button = driver.find_element(By.ID, "menu-toggle")
menu_button.click()
time.sleep(1)

#This line finds the link  that has the text "Login" and clicks it to go to the login page.
login_button = driver.find_element(By.XPATH, "//a[text()='Login']")
login_button.click()
time.sleep(1)

#These lines find the input fields for username and password, and the login button using their XPATH.
username_field = driver.find_element(By.XPATH, "//input[@id='txt-username']")
password_field = driver.find_element(By.XPATH, "//input[@name='password']")
login_field = driver.find_element(By.XPATH, "//button[@id= 'btn-login']")

#These lines type the stored username and password into their fields.
username_field.send_keys(username)
password_field.send_keys(password)
# This line clicks the login button to submit the login information.
login_field.click()

#This section waits for up to 10 seconds until a specific dropdown option is present on the page.
wait = WebDriverWait(driver, 10)
dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='combo_facility']")))
dropdown_list = Select(dropdown_element)
dropdown_list.select_by_visible_text("Hongkong CURA Healthcare Center")

#This line finds the checkbox with the ID "chk_hospotal_readmission" and clicks it.
apply_box = driver.find_element(By.XPATH, "//input[@id='chk_hospotal_readmission']")
time.sleep(1)
apply_box.click()

#This line finds the radio button with the ID "radio_program_medicaid" and clicks it.
radio_button = driver.find_element(By.XPATH,"//input[@id='radio_program_medicaid']")
radio_button.click()
time.sleep(2)

#This section waits for up to 10 seconds until the visit date input field becomes clickable.
wait = WebDriverWait(driver,10)
visit_date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='txt_visit_date']")))
visit_date_input.click()

#This line types the comment  in the text area.
time.sleep(7)
comment = driver.find_element(By.XPATH,"//textarea[@id='txt_comment']")
comment.send_keys(cmt)

#This line finds the button with the ID "btn-book-appointment" and clicks it to book the appointment.
book_button = driver.find_element(By.XPATH,"//button[@id='btn-book-appointment']")
book_button.click()

time.sleep(5)
#This line finds the link with the class "btn btn-default" and clicks it.
back_to_home_button = driver.find_element(By.XPATH,"//a[@class='btn btn-default']")
back_to_home_button.click()

time.sleep(4)
driver.quit()