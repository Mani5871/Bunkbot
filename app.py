import streamlit as st
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta

st.write("""

# Welcome to BunkBot
## Developed by Mani Deepak (Y18IT104) and Balaji (Y18IT078)
""")


mail_id = st.text_input("Email")
password1 = st.text_input("Password", type = "password")
total_classes = st.text_input("Enter total classses")
class_num = st.text_input("Enter class number")
start_time = st.time_input("Enter starting time of break")
end_time = st.time_input("Enter ending time of break")

if st.button("Start class"):
    st.write("""
    # Entering your class
    """)

    start_time = str(start_time)
    end_time = str(end_time)

    start_time_hrs = start_time[0 : 2]
    start_time_min = start_time[3 : 5]

    end_time_hrs = end_time[0 : 2]
    end_time_min = end_time[3 : 5]

    class_num = int(class_num)
    total_classes = int(total_classes)

    while class_num <= total_classes:
   
        driver = webdriver.Chrome(executable_path=r"C:\Users\ratna\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
        driver.maximize_window() 
        driver.get('https://rvrjcce.codetantra.com/login.jsp')

        user_name = driver.find_element_by_name("loginId")
        password = driver.find_element_by_name("password")
        login = driver.find_element_by_id("loginBtn")

        user_name.send_keys(mail_id)
        password.send_keys(password1)
        login.click()

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
                flag = 0
                classes = driver.find_elements_by_class_name("fc-time-grid-event")
                classes[class_num - 1].click()
                break
            except:
                time.sleep(2)


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

        time.sleep(20)
            
        iframe = driver.find_element_by_xpath("//iframe[@id='frame']")
        driver.switch_to.frame(iframe)
        listen = driver.find_elements_by_tag_name("button")
        for item in listen:
            attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
            if 'aria-label' in attrs:
                if attrs['aria-label'] == 'Listen only':
                    item.click()
                    break

        time.sleep(3600)
        driver.quit()
        class_num += 1
        
        now1 = datetime.now()
        lunch_time_start = now1.replace(hour = int(start_time_hrs), minute = int(start_time_min), second = 0, microsecond =0)
        lunch_time_end = now1.replace(hour = int(end_time_hrs), minute = int(end_time_min), second = 0, microsecond = 0)

        if now1 >= lunch_time_start and now1 <= lunch_time_end:
            while now1 <= lunch_time_end:
                now1 = datetime.now()
                time.sleep(60)