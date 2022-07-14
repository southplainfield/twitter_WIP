from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get("https://floodflash.co")
print(driver.title)
search_bar = driver.find_element(By.ID, "postcode-input")
search_bar.clear()
search_bar.send_keys("hp91rw")
search_bar.send_keys(Keys.RETURN)
print ('0')
driver.implicitly_wait(5)
search_bar = driver.find_element(By.ID,"address-form-field")
search_bar.click()
print ('1')
# search_bar.send_keys(Keys.RETURN)
search_bar = driver.find_element(By.ID,"mat-option-0")
search_bar.send_keys(Keys.RETURN)
search_bar = driver.find_element(By.ID,"mat-radio-12")
search_bar.click()
search_bar = driver.find_element(By.ID,"mat-radio-3")
search_bar.click()
search_bar = driver.find_element(By.ID,"mat-radio-6")
search_bar.click()
search_bar = driver.find_element(By.ID,"mat-checkbox-3")
search_bar.click()
search_bar = driver.find_element(By.ID,"mat-radio-9")
search_bar.click()
search_bar = driver.find_element(By.ID,"final-confirmation-checkbox")
search_bar.click()
search_bar = driver.find_element(By.ID,"cta-btn")
search_bar.click()
search_bar.click()
driver.implicitly_wait(20)


