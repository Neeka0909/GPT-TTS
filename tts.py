import pyttsx3
engine = pyttsx3.init()

# Speed percent (can go over 100)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)
# changing index, changes voices. 1 for female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say("I will speak this text")
engine.runAndWait()




