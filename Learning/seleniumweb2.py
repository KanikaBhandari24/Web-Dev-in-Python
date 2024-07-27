from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#for keeping chrome browser open
chrome=webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

#creating driver
driver=webdriver.Chrome(options=chrome)
driver.get("https://en.wikipedia.org/wiki/Main_Page") 

link=driver.find_element(By.CSS_SELECTOR, value="articlecount a")
link.click()

all=driver.find_element(By.LINK_TEXT, value="Content portals")
all.click()

search=driver.find_element(By.NAME, value="search") 
search.send_keys("Python", Keys.ENTER)  