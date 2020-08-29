import os
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 220)     # setting up new voice rate


#"""VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

pyttsx3.speak("Hello connections")
print("Hello Connections".center(150))
pyttsx3.speak("WELCOME TO  THE WORLD OF TECH")
print("WELCOME TO THE WORLD  OF TECH".center(150))                    
engine.runAndWait()
pyttsx3.speak("I am Avoca,your new virtual assistant")
print("I am Avoca,your new virtual assistant ".center(150))
pyttsx3.speak("How may i help you...?")
print("How may i help you...?".center (150))
while True:
  
  p = input("what you want me to  run: ")





  if ("date" in p): 
    pyttsx3.speak("showing todays date")
    os.system("date")
  elif ("time" in p): 
    pyttsx3.speak("showing current time")
    os.system("time")
  elif ("chrome" in p): 
    pyttsx3.speak("opening chrome")
    os.system("chrome")
  elif (("spotify" in p) or ("music" in p)):
    pyttsx3.speak("opening spotify")
    os.system("chrome www.spotify.com")
  elif ("Hello" in p) or ("hy" in p) or ("hey" in p):
    pyttsx3.speak("Hello buddy")
  elif ("tell" in p) or ("about" in p) or ("yourself" in p):
    pyttsx3.speak("My name is Avoca , I am your virtual assistant ,  i am always there to help you")
  elif ("azure" in p) or ("ms cloud" in p):
    pyttsx3.speak("opening azure cloud")
    os.system("chrome azure.microsoft.com")
  elif ("google" in p) or ("gcp" in p):
    pyttsx3.speak("opening google cloud")
    os.system("chrome cloud.google.com")
  elif ("aws" in p) or ("aws cloud services" in p):
    pyttsx3.speak("opening amazon web services")
    os.system("chrome aws.amazon.com")
  elif ("gmail" in p):
    pyttsx3.speak("opening G mail")
    os.system("chrome www.gmail.com")
  elif ("youtube" in p):
    pyttsx3.speak("opening youtube")
    os.system("chrome www.youtube.com")
  elif ("twitter" in p):
    pyttsx3.speak("opening twitter")
    os.system("chrome www.twitter.com")
  elif ("whatsapp" in p):
    pyttsx3.speak("opening whatsapp")
    os.system("chrome web.whatsapp.com")
  elif ("facebook" in p):
    pyttsx3.speak("opening facebook")
    os.system("chrome www.facebook.com")
  elif ("linkedin" in p):
    pyttsx3.speak("opening linkedin")
    os.system("chrome www.linkedin.com")
  elif ("amazon" in p):
    pyttsx3.speak("opening amazon")
    os.system("chrome www.amazon.in")  
  elif ("flipkart" in p):
    pyttsx3.speak("opening flipkart")
    os.system("chrome www.flipkart.com")
  elif ("notepad" in p) or ("editor" in p):
    pyttsx3.speak("opening notepad")
    os.system("notepad")
  elif ("puttygen" in p): 
    pyttsx3.speak("opening putty")
    os.system("puttygen")
  elif ("putty" in p): 
    pyttsx3.speak("opening putty")
    os.system("putty")
  elif ("virtualbox" in p) or ("virtual box" in p) or ("VM" in p) or ("vbox" in p) or ("vm" in p): 
    pyttsx3.speak("opening Vbox")
    os.system("virtualbox")
  elif ("stackoverflow" in p): 
    pyttsx3.speak("searching query")
    os.system("chrome www.stackoverflow.com")
  elif ("teamviewer" in p): 
    pyttsx3.speak("opening teamvier")
    os.system("teamviewer")
  elif ("ms-word" in p) or ("word" in p):
    pyttsx3.speak("opening ms-word")
    os.system("word")
  elif ("anydesk" in p): 
    pyttsx3.speak("opening anydesk")
    os.system("anydesk")
  
  elif ("facebook" in p): 
    pyttsx3.speak("launching facebook")
    os.system("chrome www.facebook.com")
  elif ("calculator" in p): 
    pyttsx3.speak("opening calculator")
    os.system("start calculator:")  
  elif ("paint" in p): 
    pyttsx3.speak("opening paint")
    os.system("start mspaint")

  elif (("programs" in p) or ("Avoca" in p) or ("avoca" in p) or("Menu"in p)):
    pyttsx3.speak("Programs i can help u with are")
    print()
    print("Programs i can help u with are:-".center(125))
    pyttsx3.speak("such as window based commands")
    print()
    print(" * Window Based Commands".center(125))
    pyttsx3.speak("Entertainment")
    print()
    print(" * Entertainment".center(125))
    pyttsx3.speak("Public clouds")
    print()
    print(" * Public Clouds".center(125))
    pyttsx3.speak("emails")
    print()
    print(" * Emails".center(125))
    pyttsx3.speak("Social media")
    print()
    print(" * Social Media".center(125))
    pyttsx3.speak("Shopping")
    print()
    print(" * Shopping".center(125))
    pyttsx3.speak("Workflows")
    print()
    print(" * WorkFlows".center(125))
    pyttsx3.speak("Virtualization")
    print()
    print(" * Virtualization".center(126))
    
  elif ("exit" in p) or ("quit" in p) or ("bye" in p):
    pyttsx3.speak("Thanku for using Avoca your virtual assistant")
    print("Thanku for using Avoca your virtual assistant".centre(125))
    pyttsx3.speak("See u soon")
    print("See u soon".center(125))
    break
  else: 
    print("Sorry can't do,Still on a Learning track".center(125))
    pyttsx3.speak("\t \t \t \t Sorry can't do that,Still on a Learning track ")

