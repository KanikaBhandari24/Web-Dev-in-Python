from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

#for keeping chrome browser open
chrome=webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

#creating driver
driver=webdriver.Chrome(options=chrome)
driver.get("http://secure-retreat-92358.herokuapp.com/")

name=driver.find_element(By.NAME, value="fname")
name2=driver.find_element(By.NAME, value="lname")
mail=driver.find_element(By.NAME, value="email")

name.send_keys("Kanika")
name2.send_keys("Bhandari") 
mail.send_keys("k.anikabhandari2417@gmail.com")

submit=driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click() 