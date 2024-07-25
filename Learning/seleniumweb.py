from selenium import webdriver

#for keeping chrome browser open
chrome=webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

#creating driver
driver=webdriver.Chrome(options=chrome)
driver.get("https://www.amazon.com") 

driver.close()