from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
username = 'Your_username'
password = 'Your_password'
url = 'https://mis.nita.ac.in'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

driver.find_element_by_id('txt_username').send_keys(username)
driver.find_element_by_id('txt_password').send_keys(password)
captcha = str(input("Enter captcha"))
driver.find_element_by_id('txt_captchalgn').send_keys(captcha)
time.sleep(0.001)
driver.find_element_by_id('btnSubmit').click()
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"Div6\"]/div/div[2]/div/script")))

result = driver.execute_script('return chart20["series"][0]["processedYData"];')

i = len(result)
a = 0
for x in result:
	a+=x
a = a/i

driver.execute_script('alert("Your cgpa is {:.2f} ")'.format(round(a,2)))

