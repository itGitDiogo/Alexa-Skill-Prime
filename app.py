from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#open browser
driver  = webdriver.Chrome() 
driver.get("https://gaming.amazon.com/gp/amzn1.adg.product.7fd6496e-5072-405f-a417-02d9236102f6?ingress=amzn&ref_=SM_LOL13_P4_CRWN")
sleep(3)

#first click "sign button"
button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/nav/div/div/div/div/div[2]/div/div[1]/button/span/div' )
button.click()

#second click "email"
sleep(3)
email = driver.find_element(By.ID, 'ap_email' )
email.click()
email.send_keys("abc@gmail.com")

#tertiary click
password = driver.find_element(By.ID, 'ap_password')
password.click()
password.send_keys("oii")

#four click
sign = driver.find_element(By.ID, 'signInSubmit')
sign.click()
driver.quit()