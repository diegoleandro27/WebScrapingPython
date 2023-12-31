from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
opts = Options()

# Use ChromeDriverManager to automatically download and manage Chromedriver
driver = webdriver.Edge()
driver.get('https://crm.zoho.com/')
driver.maximize_window()

results = driver.find_elements(By.XPATH, '/html/body/main/div/div/div[1]/div/div[1]/p')

for result in results:
    text = result.text
    print(text)

sleep(10)   

