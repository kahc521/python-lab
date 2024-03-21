from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys                        

#open Google Chrome browser  
driver=webdriver.Chrome()
time.sleep(3)

print(f"The test case started")
#maximize the window size
driver.maximize_window()
time.sleep(5)
#delete the cookies  
driver.delete_all_cookies()

#navigate to the url  
driver.get("http://198.58.119.40:8087/showMyLoginPage")

# get the browser's title
title1= driver.title
print(f"Connecting to {title1} page of Geolocation app")

# identify the username box and enter the value  
elem1 = driver.find_element(by=By.NAME, value="username")
elem1.send_keys("root@utrains.test")
time.sleep(2)

# identify the password box and enter the value  
elem2 = driver.find_element(by=By.NAME, value="password")
elem2.send_keys("root_pass")
time.sleep(2)

# Click on the Log in button
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()
title2= driver.title

if title1 == title2:
    print("Wrong credentials please try again !!")
    driver.quit()
    sys.exit(99)
else:
    print("Connected to website")

time.sleep(5)

# navigate to About us page
elem3= driver.find_element(By.LINK_TEXT, "About")
elem3.click()
time.sleep(5)

# navigate to Departments' page
elem4= driver.find_element(By.LINK_TEXT, "Departments")
elem4.click()
time.sleep(5)

# navigate to Doctors' page
elem5= driver.find_element(By.LINK_TEXT, "Doctors")
elem5.click()
time.sleep(5)

# navigate to Blog page
elem6= driver.find_element(By.LINK_TEXT, "Blog")
elem6.click()
time.sleep(5)

# navigate to Contact page
elem7= driver.find_element(By.LINK_TEXT, "Contact")
elem7.click()
time.sleep(5)


# close the driver
driver.quit()
print("Test to Geolocation app is completed please check the output")
sys.exit()