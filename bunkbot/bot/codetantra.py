from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyttsx3
import speech_recognition as sr
import pyaudio
import wave
from django.shortcuts import render, HttpResponse, redirect
import datetime



def attend(request):

	engine = pyttsx3.init()
	print('attend')
	text = 'I will attend your online classes. Have a nice day'
	engine.say(text)
	engine.runAndWait()

	ind = request.POST.get('count')
	print(ind)

	driver = webdriver.Firefox(executable_path=r"C:\\Users\\GILMA\\Desktop\\selenium\\geckodriver.exe")
	driver.maximize_window() 
	driver.get('https://rvrjcce.codetantra.com/login.jsp')
	print(driver.title)

	user_name = driver.find_element_by_name("loginId")
	password = driver.find_element_by_name("password")
	login = driver.find_element_by_id("loginBtn")

	user_name.send_keys("manideepak650@gmail.com")
	password.send_keys("Deepak@104")
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
			flag = 0
			classes = driver.find_elements_by_class_name("fc-time-grid-event")
			print(len(classess))
			classes[0].click()
			print(ind - 1)
			break
			for item in classes:
				attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
				if 'background' in attrs:
					print('g')
					if attrs['background'] == 'green':
						print(item)
						flag = 1
						item.click()
						print('green')
						break
			print(len(classes))
			if flag == 1:
				break
			break
		except:
			time.sleep(2)


	# classes[0].click()
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
		
	print("Waiting for listen")

	iframe = driver.find_element_by_xpath("//iframe[@id='frame']")
	driver.switch_to.frame(iframe)
	listen = driver.find_elements_by_tag_name("button")
	for item in listen:
		attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
		if 'aria-label' in attrs:
			if attrs['aria-label'] == 'Listen only':
				item.click()
				break

	time.sleep(20)
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 25
	WAVE_OUTPUT_FILENAME = "output.wav"

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

	driver.quit()

	r = sr.Recognizer()

	hellow=sr.AudioFile('output.wav')
	with hellow as source:
	    audio = r.record(source)
	try:
	    s = r.recognize_google(audio)
	    file = open('class.txt', 'w')
	    file.write(s)
	    file.close()

	except Exception as e:
	    print("Exception: "+str(e))

	context = {'text' : request.session['user']}

	return redirect('/')
