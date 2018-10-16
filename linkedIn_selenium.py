import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('')
driver.get('http://www.linkedin.com')

username = driver.find_element_by_class_name('login-email')
username.send_keys(parameters.linkedin_username)
sleep(0.5)

password = driver.find_element_by_id('login-password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(5)

driver.get("https://www.google.com")
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls = driver.find_element_by_tag_name('cite')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)


