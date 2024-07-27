from selenium import webdriver

#for keeping chrome browser open
chrome=webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

#creating driver
driver=webdriver.Chrome(options=chrome)
driver.get("https://python.org")

d=driver.find_element(By.CLASS_NAME, value="a-price-whole")
c=driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {d.text}.{c.text}") 

search=driver.find_element(By.NAME, value="q")
print(search.get_attribute("placeholder"))
button=driver.find_element(By.ID, value="submit")
print(button.size) 
link=driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(link.text)
path=driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(path.text)

t=driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
n=driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events={}
for i in range(len(t)):
    events[i]={
        "time": t[i].text,
        "name": n[i].text
    }
print(events) 

driver.close() 
