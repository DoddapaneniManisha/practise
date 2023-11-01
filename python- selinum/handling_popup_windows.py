from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")
driver.find_element_by_link_text("Open Pop-up").click()

# Switch to the pop-up window
driver.switch_to.window(driver.window_handles[1])
print(driver.title)

# Close the pop-up window
driver.close()

# Switch back to the main window
driver.switch_to.window(driver.window_handles[0])

driver.quit()
