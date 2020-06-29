from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
username = 'your_username'
password = 'your_password'

url = 'https://mis.nita.ac.in'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
#time.sleep(3) # decrease or increase as per your convenience
driver.find_element_by_id('txt_username').send_keys(username)
driver.find_element_by_id('txt_password').send_keys(password)

captcha = str(input("Enter captcha"))
driver.find_element_by_id('txt_captchalgn').send_keys(captcha)
time.sleep(0.05)
driver.find_element_by_id('btnSubmit').click()
driver.maximize_window()
time.sleep(6)
result = driver.execute_script('return chart20["series"][0]["processedYData"];')

i = len(result)
a = 0
for x in result:
	a+=x

a = a/i

driver.execute_script('alert("Your cgpa is {:.2f} ")'.format(round(a,2)))

