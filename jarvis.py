from tkinter import *
import pygame 
import speech_recognition as  sr
import pyttsx3  #this is text to speech library
import pygame
import webbrowser
import random
import os, sys, subprocess, datetime
import  time 
from PIL import  ImageTk, Image
import requests
import json
import cv2
#import PyAudio

#import PyInstaller
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

#Music Loader....

#pygame.mixer.init()
#pygame.mixer.music.load('Jarvis.mp3')
#pygame.mixer.music.set_volume(1)
#pygame.mixer.music.play(1)


#time.sleep(18)


#Making  Engine Property.....

engine=pyttsx3.init()
voices=engine.getProperty('voices')

#Speak Function...

def speak(audio):
	engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')
	engine.say(audio)
	engine.runAndWait()



def myCommand():
	
	try:
		r=sr.Recognizer()
		# use the microphone as source for input.
		with sr.Microphone() as source:

			# wait for a second to let the recognizer 
			# adjust the energy threshold based on 
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source, duration=0.5)

			audio=r.listen(source)
		try:
			query1=r.recognize_google(audio,  language='en-in')

		except sr.UnknownValueError:
			speak("Try Again, Please")
			pass
		return  query1

	except sr.RequestError as e: 
		print("Could not request results; {0}".format(e)) 
		speak("I think your internet connection is down")

#..........................developed by gyanesh kumar on 24/07/20..............................

def greetMe():
	currentH = int(datetime.datetime.now().hour)
	if currentH >= 0 and currentH < 12:
		speak('Good Morning!, sir')

	if currentH >= 12 and currentH < 18:
		speak('Good Afternoon! sir')

	if currentH >= 18 and currentH !=0:
		speak('Good Evening! sir')



canvasImgList=[]
class Widget():
	def __init__(self):
		global root
		root=Tk()
		root.title("Personal assistant")
		root.config(background='#F0F0F0')
		root.iconbitmap("micIcon.ico")
		root.geometry("700x650")
		root.resizable(0,0)
		global icon01
		global icon03
		icon01=PhotoImage(file=r"JarvisOffsmall.png")
		icon03=PhotoImage(file=r"JarvisOnsmall.png")
		icon02=PhotoImage(file="roundspeak.png").subsample(3,3)
		canvasImgList.append(icon01)
		global canvas
		canvas=Canvas(root,width=700,height=650)
		canvas.create_image(0,0,anchor=NW, image=canvasImgList[0])
		


		def getTime():
			timeString=time.strftime("%I: %M: %S : %p")
			clock.config(text=timeString)
			clock.after(200,getTime)

		#label=Label(root,text="Your personal assistant",bg='deepSkyBlue',fg='#391C11',font=('Agency FB', 30, 'bold')).pack(fill='both',expand='no')

	

		clock=Label(canvas,background="black",font=('FFF Tusj', 20,'bold'),fg='gold')
		#clock.pack()
		clock.place(relx=0.05, rely=0.06)
		global btn
		btn=Button(canvas,image=icon02,background='black',command=self.clickedbtn)
		#btn.pack(side='bottom',expand='no')
		btn.place(relx=0.45, rely=0.85)

		myNameLabel = Label(canvas, background= "black",text= "Created by:David Cohen",font=('ariel', 10,'bold'),fg="sky blue")
		myNameLabel.place(relx= 0.77, rely=0.95)

		global tog_btn
		tog_btn= Button(canvas, text='Continuous listening mode', background='black',fg='blue',font=('ariel', 10,'bold'),command=self.clickedTogbtn)
		tog_btn.place(relx=0.70, rely=0.07)

		
		speak("Hello sir , I am your P A")
		speak("What can I Do For You.....")

#..........................developed by gyanesh kumar on 24/07/20..............................
		
		canvas.pack()
		getTime()
		
		root.mainloop()

	def clickedbtn(self):
		#print(btn['state'])
		canvasImgList.clear()
		canvasImgList.append(icon03)
		canvas.create_image(0,0,anchor=NW, image=canvasImgList[0])
		#time.sleep(1)
		global query
		query1=myCommand()
		query1=query1.lower()

		google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which','how':'how','where':'where'}

		def is_valid_search(phrase):
			if(google_searches_dict.get(phrase.split(' ')[0])==phrase.split(' ')[0]):
				return True

		if 'open youtube' in query1:
			speak("opening youtube")
			webbrowser.open("www.youtube.com")
		elif 'show my day' in query1:
			speak("opening calendar")
			webbrowser.open("https://calendar.google.com/calendar/u/0/r")
		elif 'open gmail' in query1:
			speak("opening gmail")
			webbrowser.open("www.gmail.com")
		elif 'open facebook' in query1:
			speak("opening facebook")
			webbrowser.open("www.facebook.com")
		elif 'password' in query1:
			speak("Okay")
			speak("Here is Your Saved Connected Wifi Password")
			Collect_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
			#print(Collect_data)
			Collect_profiles = [i.split(":")[1][1:-1] for i in Collect_data if "All User Profile" in i]
			#print(Collect_profiles)
			for i in Collect_profiles:
				results=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
				#print(results)
				results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
				#print(results)
				try:
					print("Wifi name: {:<20}|  Password: {:<}".format(i, results[0]))
				except:
					print("Wifi name: {:<20}|  Password:  {:<}".format(i, ""))
		elif 'tell me about yourself' in query1:
			speak("Hello i am your personal assistant")
		# elif 'play music' in query1:
		# 	os.startfile('D:\\Songs\\kalhonaho.mp3')
		# 	speak("ENJOY!")
		elif 'location' in query1:
			res = requests.get('https://ipinfo.io/')
			data = res.json()

			city = data['city']

			location = data['loc'].split(',')
			latitude = location[0]
			longitude = location[1]
			address=data['country']

			print("Latitude value :", latitude)
			speak("Latitude value is {}".format(latitude))
			print("Longitude value: ", longitude)
			speak("Longitude value is {}".format(longitude))
			print("Captial City : ", city)
			speak("Captial City Name is {}".format(city))
			print("Country :",address)
			speak("Country name is {}".format(address))
		elif is_valid_search(query1):
			speak("Opening Searching Google..")
			taburl="https://google.com/search?q="
			question=query1
			webbrowser.open(taburl+question)
		


		elif 'webcam' in query1:
			speak("Opening Web Camera...")
			faceDetected= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
			video=cv2.VideoCapture(0)
			while True:
				ret,frame=video.read()
				faces=faceDetected.detectMultiScale(frame, 1.3,5)
				for x,y,w,h in faces:
					cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
				cv2.imshow("Frame", frame)
				k=cv2.waitKey(1)
				if k==ord('q'):
					break
			video.release()
			cv2.destroyAllWindows()

		elif 'open jarvis photo' in query1:  #################################
					speak("opening picture")  ##################################
					os.startfile(r'JarvisOn.png')
		elif 'play music' in query1:
					speak("playing your favourite song")
					os.startfile(r'lehnga.mp3')
		elif 'open music video' in query1:
					speak("playing your favourite song video")
					os.startfile(r'C:\Users\Gyanesh.Kumar\Desktop\jarvis download\Arijit Singh.mp4')
					

		elif 'write text' in query1:
			speak('activating writing mode')
		
			speak("Tell me what to write sir")
			while(1):
				r=sr.Recognizer()
				with sr.Microphone() as source:
					r.adjust_for_ambient_noise(source, duration=1)
					audio=r.listen(source)
					try:
						query1=r.recognize_google(audio,  language='en-in')

					except sr.UnknownValueError:
						query1 ="*"
				if 'exit writing' in query1:
					speak("quitting writing mode")
					f=open(r'demo.doc','r')
					f.seek(0)
					content = f.read()
					print("length of content in text file:- ",len(content))
					f.close()
					if len(content) !=0:
						os.startfile(r'demo.doc')
						speak('Opening the text file. Please save it')
					break

				

				elif 'clear all data' in query1:
					file = open(r'demo.doc',"r+")
					file.truncate(0)
					file.close()
					speak('deleted all data ')
				
				elif 'delete last word' in query1:
					f=open(r'demo.doc','r')
					f.seek(0)
					content = f.read()
					contentNew=content.rsplit(' ',1)[0] 
					#print(contentNew)
					f=open(r'demo.doc','w+')
					f.write(contentNew)
					f.seek(0)
					con = f.read()
					print(con)
					f.close()
					speak('deleted last word')
					#..........................developed by gyanesh kumar on 24/07/20.............................
				elif 'delete last sentence' in query1:
					f=open(r'demo.doc','r')
					f.seek(0)
					content = f.read()
					contentNew=content.rsplit('.',2)[0] 
					#print(contentNew)
					f=open(r'demo.doc','w+')
					f.write(contentNew+'.')
					f.seek(0)
					con = f.read()
					print(con)
					f.close()
					speak('deleted last sentence')

				


				elif "*"  not in query1:
					query1 = query1+"."
					#os.startfile(r'C:\Users\Gyanesh.Kumar\Desktop\demo.doc')
					f=open(r'demo.doc','a+')
					f.seek(0) #for changing the cursor position to start
					old_content = f.read()
					#print("len of old content=",len(old_content))
					f.write(" "+query1)
					f.seek(0)
					new_content = f.read()
					if len(old_content) != len(new_content):
						print(new_content)
						#text_box.insert("1.0",new_content)
					f.close()

					# top.mainloop()

		elif 'time' in query1:
			timeString=time.strftime("%I: %M: %p")
			speak("its {} now".format(timeString))
			
		# elif 'exit' or 'quit' in query1:
		# 	speak("Good bye sir")
		# 	exit()	

		else:
			speak("sorry i didnt get you. Please speak again.")

		canvasImgList.clear()
		canvasImgList.append(icon03)
		canvas.create_image(0,0,anchor=NW, image=canvasImgList[0])


	def clickedTogbtn(self):     #for continuous listening mode
		speak("continuous listening mode activated")
		root.wm_withdraw()
		
		google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which','how':'how'}
		def is_valid_search(phrase):
			if(google_searches_dict.get(phrase.split(' ')[0])==phrase.split(' ')[0]):
				return True


		while(1):
				try:
					r=sr.Recognizer()
					# use the microphone as source for input.
					with sr.Microphone() as source:

						# wait for a second to let the recognizer 
						# adjust the energy threshold based on 
						# the surrounding noise level 
						r.adjust_for_ambient_noise(source, duration=0.5)

						audio=r.listen(source)
					try:
						query1=r.recognize_google(audio,  language='en-in')

					except sr.UnknownValueError:
						query1 = "*"
			

				except sr.RequestError as e: 
					print("Could not request results; {0}".format(e)) 
					speak("I think your internet connection is down")
				query1= query1.lower()

				if 'open youtube' in query1:
					speak("opening youtube")
					webbrowser.open("www.youtube.com")
				elif 'show my day' in query1:
					speak("opening calendar")
					webbrowser.open("www.calendar.google.com/calendar/u/0/r")
				elif 'open gmail' in query1:
					speak("opening gmail")
					webbrowser.open("www.gmail.com")
				elif 'open facebook' in query1:
					speak("opening facebook")
					webbrowser.open("www.facebook.com")
				elif 'password' in query1:
					speak("Okay")
					speak("Here is Your Saved Connected Wifi Password")
					Collect_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
					#print(Collect_data)
					Collect_profiles = [i.split(":")[1][1:-1] for i in Collect_data if "All User Profile" in i]
					#print(Collect_profiles)
					for i in Collect_profiles:
						results=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
						#print(results)
						results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
						#print(results)
						try:
							print("Wifi name: {:<20}|  Password: {:<}".format(i, results[0]))
						except:
							print("Wifi name: {:<20}|  Password:  {:<}".format(i, ""))
				elif 'tell me about yourself' in query1:
					speak("Hello i am your personal assistant")
				# elif 'play music' in query1:
				# 	os.startfile('D:\\Songs\\kalhonaho.mp3')
				# 	speak("ENJOY!")
				elif 'location' in query1:
					res = requests.get('https://ipinfo.io/')
					data = res.json()

					city = data['city']

					location = data['loc'].split(',')
					latitude = location[0]
					longitude = location[1]
					address=data['country']

					print("Latitude value :", latitude)
					speak("Latitude value is {}".format(latitude))
					print("Longitude value: ", longitude)
					speak("Longitude value is {}".format(longitude))
					print("Captial City : ", city)
					speak("Captial City Name is {}".format(city))
					print("Country :",address)
					speak("Country name is {}".format(address))
				elif is_valid_search(query1):
					speak("Opening Searching Google..")
					taburl="https://google.com/search?q=" 
					question=query1
					webbrowser.open(taburl+question)
				


				elif 'webcam' in query1:
					speak("Opening Web Camera...")
					faceDetected= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
					video=cv2.VideoCapture(0)
					while True:
						ret,frame=video.read()
						faces=faceDetected.detectMultiScale(frame, 1.3,5)
						for x,y,w,h in faces:
							cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
						cv2.imshow("Frame", frame)
						k=cv2.waitKey(1)
						if k==ord('q'):
							break
					video.release()
					cv2.destroyAllWindows()

				elif 'open jarvis photo' in query1:  #################################
							speak("opening picture")  ##################################
							os.startfile(r'JarvisOn.png')
				elif 'play music' in query1:
							speak("playing your favourite song")
							os.startfile(r'lehnga.mp3')
				elif 'open music video' in query1:
							speak("playing your favourite song video")
							os.startfile(r'C:\Users\Gyanesh.Kumar\Desktop\jarvis download\Arijit Singh.mp4')
							

				elif 'write text' in query1:
					speak('activating writing mode')
				
					speak("Tell me what to write sir")
					while(1):
						r=sr.Recognizer()
						with sr.Microphone() as source:
							r.adjust_for_ambient_noise(source, duration=1)
							audio=r.listen(source)
							try:
								query1=r.recognize_google(audio,  language='en-in')

							except sr.UnknownValueError:
								query1 ="*"
						if 'exit writing' in query1:
							speak("quitting writing mode")
							f=open(r'demo.doc','r')
							f.seek(0)
							content = f.read()
							print("length of content in text file:- ",len(content))
							f.close()
							if len(content) !=0:
								os.startfile(r'demo.doc')
								speak('Opening the text file. Please save it')
							break

						

						elif 'clear all data' in query1:
							file = open(r'demo.doc',"r+")
							file.truncate(0)
							file.close()
							speak('deleted all data ')
						
						elif 'delete last word' in query1:
							f=open(r'demo.doc','r')
							f.seek(0)
							content = f.read()
							contentNew=content.rsplit(' ',1)[0] 
							#print(contentNew)
							f=open(r'demo.doc','w+')
							f.write(contentNew)
							f.seek(0)
							con = f.read()
							print(con)
							f.close()
							speak('deleted last word')
							#..........................developed by gyanesh kumar on 24/07/20.............................
						elif 'delete last sentence' in query1:
							f=open(r'demo.doc','r')
							f.seek(0)
							content = f.read()
							contentNew=content.rsplit('.',2)[0] 
							#print(contentNew)
							f=open(r'demo.doc','w+')
							f.write(contentNew+'.')
							f.seek(0)
							con = f.read()
							print(con)
							f.close()
							speak('deleted last sentence')

						


						elif "*"  not in query1:
							query1 = query1+"."
							#os.startfile(r'C:\Users\Gyanesh.Kumar\Desktop\demo.doc')
							f=open(r'demo.doc','a+')
							f.seek(0) #for changing the cursor position to start
							old_content = f.read()
							#print("len of old content=",len(old_content))
							f.write(" "+query1)
							f.seek(0)
							new_content = f.read()
							if len(old_content) != len(new_content):
								print(new_content)
								#text_box.insert("1.0",new_content)
							f.close()

							# top.mainloop()

				elif 'time' in query1:
					timeString=time.strftime("%I: %M: %p")
					speak("its {} now".format(timeString))
					
				# elif 'exit' or 'quit' in query1:
				# 	speak("Good bye sir")
				# 	exit()	

				elif '*' in query1:
					pass
						
				elif 'exit listening mode' in query1:
					speak("quitting listening mode")
					root.wm_deiconify()
					break
				
				else:
					speak("sorry i didnt get you. Please speak again.")

if __name__ == '__main__':
	#greetMe()
	widget = Widget() 
	speak("Good bye sir")       




