from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com/login")
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("login_button")

username.send_keys("my_username")
password.send_keys("my_password")
login_button.click()

print("Login successful")
driver.quit()
