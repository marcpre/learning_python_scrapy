from selenium import webdriver

driver = webdriver.Chrome('')
driver.get('http://www.linkedin.com')

username = driver.find_element_by_class_name('login-email')
username.send_keys('foo@gmail.com')

password = driver.find_element_by_id('login-password')
password.send_keys('somepass')

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()

