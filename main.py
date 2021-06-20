from selenium import webdriver
from selenium.webdriver.common.by import By
import time

i = 1
while i <= 2:

	driver = webdriver.Firefox(executable_path=r"C:\\Users\\GILMA\\Desktop\\selenium\\geckodriver.exe")
	driver.maximize_window() 
	driver.get('https://rvrjcce.codetantra.com/login.jsp')
	print(driver.title)

	user_name = driver.find_element_by_name("loginId")
	password = driver.find_element_by_name("password")
	login = driver.find_element_by_id("loginBtn")

	user_name.send_keys("manideepak650@gmail.com")
	password.send_keys("1")
	login.click()
	print("Login Successful")

	time.sleep(1)
	while True:
		try:
			meetings = driver.find_element(By.XPATH,"//a[@title = 'Click here to view Meetings']")
			meetings.click()
			break
		except:
			time.sleep(2)

	time.sleep(1)
	while True:
		try:
			classes = driver.find_elements_by_class_name("fc-time-grid-event")
			print(len(classes))
			# classes = driver.find_element(By.XPATH, "//a[@style='color: white; background: green none repeat scroll 0% 0%; inset: 450.397px 0% -480.397px; z-index: 1;']")
			break
		except:
			time.sleep(2)

	
	classes[3].click()
	while True:
		try:
			close = driver.find_element(By.XPATH, "//a[@href = '/secure/tla/m.jsp']")
			try:
				join = driver.find_element(By.XPATH, "//a[@role = 'button']")
				join.click()
			except:
				break
		except:
			time.sleep(2)

	while True:
		try:
			print("Waiting for listen")
			listen = driver.find_elements_by_tag_name("button")
			print(listen, len(listen))
			listen[2].click()
			break
		except:
			time.sleep(5)


	time.sleep(60)
	driver.quit()
	i += 1
	time.sleep(10)
