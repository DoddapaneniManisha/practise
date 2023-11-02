from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")
driver.save_screenshot("screenshot.png")
driver.quit()
