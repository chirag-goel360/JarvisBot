# JarvisBot
A Python based voice assistant which performs various tasks based on user's voice instructions.
This bot provides the facilities to control computer using voice instructions only
i.e no need of user to work on keyboard even to write an email.

### Getting Started

For learning ChatBot development you can take help from these sites and videos.

A few resources to get you started are:

- [Lab: Learn Python Basics](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3)
- [Cookbook: Site for learning Assistant development](https://www.geeksforgeeks.org/personal-voice-assistant-in-python/) 
- [Place to Learn: ChatBot Development](https://www.youtube.com/watch?v=Lp9Ftuq2sVI&t=3s)
- [Place to Learn: GUI Development](https://www.tutorialspoint.com/python/python_gui_programming.htm)

For help getting started with Python, view
[online documentation](https://www.python.org/about/gettingstarted/), which offers tutorials,
samples, guidance on Python.

Technologies|
-----------|
Python |
tkinter |

### Developers
- Ritik Miglani -Student of Amity School of Engineering and Technology(B.Tech. CSE)

        Email Address - 'miglaniritik20@gmail.com'
        
- Varun Prakash Tiwari -Student of Dr. Akhilesh Das Gupta Institute of Technology & Management(B.Tech. CSE)

        Email Address - 'varunprakash652@gmail.com'

- Chirag Goel -Student of Amity School of Engineering and Technology(B.Tech. CSE)

        Email Address - 'chirag.goel360@gmail.com'
        
Sample Code for JarvisBot
```
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
		#print(e)
		print("say that again please...")
		return "None"
		var1.set(query)
		window.update()
	return query
```
![Image ](https://i.ibb.co/cNbm8JH/main2.jpg)
![Image ](https://i.ibb.co/gwSs0zZ/main.jpg)
