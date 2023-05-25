
import pyttsx3
import openai

OPENAI_API_KEY = 'API_KEY_HERE'
openai.organization = "ADD ORGANIZATION KEY HERE"
openai.api_key = OPENAI_API_KEY
engine = pyttsx3.init()

# Speed percent (can go over 100)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 200)
# changing index, changes voices. 1 for female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


while True:
    message = input("User: ")
    if message == "stop":
        break
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": message}
            ],
        )
        answer = completion.choices[0].message.content.strip()
        print('bot:'+answer + "\n")
        engine.say(answer)
        engine.runAndWait()
