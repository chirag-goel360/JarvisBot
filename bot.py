import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import requests
import subprocess
import ctypes
import json
import pyjokes
from urllib.request import urlopen
from tkinter import *

window = Tk()
window.title('Jarvis')

global var 
global var1

var = StringVar()
var1 = StringVar()

emailTo = {
	"key": "emailid@gmail.com",
	"key": "emailid@gmail.com",
	"key": "emailid@gmail.com",
	"key": "emailid@gmail.com",
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def update(ind):
	frame = frames[(ind) % 100]
	ind += 1
	label.configure(image = frame)
	window.after(100, update ,ind)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		var.set("Good Morning!")
		window.update()
		speak("Good Morning!")
	elif hour>=12 and hour<18:
		var.set("Good Afternoon!")
		window.update()
		speak("Good Afternoon!")
	else:
		var.set("Good Evening!")
		window.update()
		speak("Good Evening!")
	speak("I am Jarvis, Sir. Please tell me how may I help you")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		var.set("Listening...")
		window.update()
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		var.set("Recognizing...")
		window.update()
		print("Recognizing...")
		query = r.recognize_google(audio,language='en-in')
		print(f"User said: {query}\n")
	except Exception as e:
		print("say that again please...")
		return "None"
		var1.set(query)
		window.update()
	return query

def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com')
	server.ehlo()
	server.starttls()
	server.login('Your Email Id','Your Password')
	server.sendmail('Your Email Id',emailTo[to],content)
	server.close()

def playBot():
	wishMe()
	while True:
		query = takeCommand().lower()
		if 'wikipedia' in query:
			speak('Searching Wikipedia......')
			query = query.replace("wikipedia","")
			results = wikipedia.summary(query, sentences=2)
			speak('According to wikipedia')
			print(results)
			speak(results)
		elif 'youtube' in query:
			speak("Here you go to Youtube")
			webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('https://www.youtube.com/')
		elif 'google' in query:
			speak("Here you go to Google ")
			webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('https://www.google.com/')
		elif 'coding blocks' in query:
			speak("Here you go to Coding Blocks")
			webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('https://online.codingblocks.com/')
		elif 'open code' in query:
			codePath = "Path for visual studio code in your PC"
			os.startfile(codePath)
		elif 'open java' in query:
			codeJava = "Path for Ecllipse in your PC"
			os.startfile(codeJava)
		elif 'play music' in query:
			music_dir = 'Song Directory'
			songs = os.listdir(music_dir)
			print(songs)
			play_rand = random.choice(songs)
			print("playing "+play_rand)
			os.startfile(os.path.join(music_dir,play_rand))
		elif 'the time' in query or 'current time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(strTime)
			var.set(strTime)
			window.update()
			speak(f"Sir, the time is {strTime}")
		elif 'send email' in query:
			try:
				var.set(emailTo.keys())
				window.update()
				print(emailTo.keys())
				speak("Whom to send? ")
				to = takeCommand()
				var.set("What should I say? ")
				window.update()
				speak("What should I say?")
				content = takeCommand()
				sendEmail(to,content)
				var.set("Email has been sent! ")
				window.update()
				print("Email has been sent! \n")
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				var.set("Sorry I can't send")
				window.update()
				speak("sorry I can't send")
		elif 'write a note' in query:
			var.set("what should I write, sir")
			window.update()
			speak("what should I write, sir")
			note = takeCommand()
			file = open('File.txt','w')
			var.set("Sir, should I include date and time?")
			window.update()
			speak("Sir, should I include date and time? ")
			sureity = takeCommand()
			if 'yes' in sureity or 'sure' in sureity:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")
				file.write(strTime)
				file.write(":-")
				file.write(note)
				var.set("File created successfully with date and time")
				window.update()
				speak("File created successfully with date and time")
			else: 
				file.write(note)
		elif 'show note' in query:
			var.set("showing notes")
			window.update()
			speak("showing notes")
			file = open('File.txt','r')
			var.set(file.read())
			window.update()
			print(file.read())
			speak(file.read(10))
		elif 'weather' in query:
			api_key = "API KEY"
			base_url = "http://api.openweathermap.org/data/2.5/weather?"
			speak("Please tell City name to check weather")
			city_name = takeCommand()
			complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
			response = requests.get(complete_url)
			x = response.json()
			if x["cod"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				var.set(" Temperature (in celcius unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
				window.update()
				print(" Temperature (in celcius unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			else:
				speak(" City Not Found ")
		elif 'news' in query:
			api_news_key = "API KEY"
			try:
				jsonObj = urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey='+api_news_key)
				data = json.load(jsonObj)
				i = 1
				var.set("Here are some top news from times of india")
				window.update()
				speak("Here are some top news from times of india")
				print('''===============TIMES OF INDIA===============''')
				for item in data['articles']:
					print(str(i)+ '. '+item['title']+'\n')
					print(item['description']+'\n')
					speak(str(i)+'. '+item['title']+'\n')
					i += 1
			except Exception as e:
				print(str(e))
		elif 'joke' in query:
			p = pyjokes.get_joke()
			print(p)
			speak(p)
		elif 'search' in query or 'give' in query:
			query = query.replace("search", "")
			query = query.replace("give","")
			webbrowser.open(query)
		elif 'where is' in query:
			query = query.replace('where is','')
			location = query
			speak('locating on google maps'+location)
			webbrowser.open('https://www.google.com/maps/place/'+location)
		elif 'find' in query:
			query = query.replace('find','')
			findVideo = query
			speak('Finding '+findVideo + 'on Youtube')
			webbrowser.open('https://www.youtube.com/results?search_query='+findVideo)
		elif 'amazon' in query:
			query = query.replace('amazon','')
			query = query.replace('flipkart','')
			comodity = query
			speak('Finding '+comodity + 'on Amazon')
			webbrowser.open('https://www.amazon.in/s?k='+comodity+'&ref=nb_sb_noss_2')
		elif 'how are you' in query:
			var.set("I'm fine Thank you")
			window.update()
			speak("I'm fine Thank you")
			var.set("What about you?")
			window.update()
			speak('What about you?')
		elif 'fine' in query or 'good' in query:
			var.set("Ohh great, Tell what can I do for you?")
			window.update()
			speak("Ohh great, Tell what can I do for you?")
		elif 'will you be my gf' in query or 'will you be my bf' in query:
			var.set("Ohh Yes I was waiting when you will say this!!!")
			window.update()
			speak("Ohh Yes I was waiting when you will say this!!!")
		elif 'i love you' in query:
			var.set("Awwwwwwww...... I love You Too")
			window.update()
			speak("Awwwwwwww...... I love You Too")
		elif 'lock windows' in query:
			speak('Sir, are you sure')
			x = takeCommand().lower()
			if x == 'yes':
				speak('locking the device')
				ctypes.windll.user32.LockWorkStation()
			elif x == 'No':
				exit()
			else: 
				speak("Sorry Sir, I did'nt get it")
		elif 'restart' in query:
			subprocess.call(["shutdown", "/r"])
		elif 'shutdown system' in query:
			speak('Sir, are you sure')
			o = takeCommand().lower()
			if o == 'yes':
				speak('Hold a sec!! starting process of shuting down system')
				subprocess.call('shutdown /p /f')
			elif o == 'No':
				exit()
			else: 
				speak("Sorry Sir, I did'nt get it")
		elif 'exit' in query or "i am done" in query or " leave" in query:
			var.set("Bye Sir")
			window.update()
			speak("I hope you had a good experience")
			speak("Thank You!")
			break

def exitBot():
	query = 'exit'.lower()
	if 'exit' in query or "i am done" in query or " leave" in query:
		var.set("Bye Sir")
		bt1.configure(bg = '#5C85FB')
		bt0['state'] = 'normal'
		bt2['state'] = 'normal'
		window.update()
		speak("I hope you had a good experience")
		speak("Thank You!")
		exit()

label2 = Label(window,textvariable = var1,bg = '#FAB60C')
label2.configure(font = ('Courier',20))
var1.set('User Said:')
label2.pack()

label1 = Label(window,textvariable=var,bg='#ADD8E6')
label1.configure(font = ('Courier',20))
var.set(' Welcome! ')
label1.pack()

frames = [PhotoImage(file = 'robo.gif',format = 'gif -index %i' %(i))
for i in range(200)]

label = Label(window,width = 350,height = 300)
label.pack()
window.after(0,update,0)

Label(window,text = " Jarvis ", font = ("Arial Bold",20)).pack()
bt0 = Button(window,text = "WISH_ME", bg = "Blue",fg = "Black", command = wishMe, width = 20).pack()
bt1 = Button(window,text = "PLAY", bg = "green",fg = "Black",command = playBot,  width = 20).pack()
bt2 = Button(window,text = "EXIT", bg = "Red",fg = "White",command = window.destroy,  width = 20).pack()

window.geometry('400x600')
window.mainloop()