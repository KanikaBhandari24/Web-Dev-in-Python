from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

mail="kanikacodes2@gmail.com"
pw="Kanika@k2405"
ph=8595858671

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3981450661&f_WT=2&geoId=106187582&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

time.sleep(2)
reject=driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY]')
reject.click()
time.sleep(2)
sign=driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign.click()

time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(mail)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(pw)
password_field.send_keys(Keys.ENTER)
input("Press Enter when you have solved the Captcha")

time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(ph)

#Submit the application
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()


#driver.quit()