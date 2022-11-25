from ast import While
import datetime
import random
from secrets import choice

print("Welcome to HOMO chat")
name=input("Enter your name:")
print("Hello",name)
while True:
    message =str(input("message:"))
    if message == "Hi": 
        print("Hello")
    elif message == "How are you" :
        print("Fine")
    elif message == "I want to study":
        print("That's nice , do more research  , good luck")
    elif message == "What is your name":
         print("My name is HOMO ")
    elif message == "Who made you":
        print(" Advaith made me") 
    elif message == "Where do you live":
        print("with you")
    elif message == "What is the news":
        print("here is the link - https://www.msn.com/en-in/")
    elif message == "Open maps":
        print("here is the link - https://www.google.com/maps")
    elif message == "Open google":
      print("here is the link - https://www.google.co.in/")
    elif message == "What is the weather today":
        print("here is the link - https://weather.com/")
    elif message == "Open outlook":
        print("here is the link - https://outlook.live.com/")
    elif message == "Set alaram":
        print(" here is the link -https://www.online-stopwatch.com/full-screen-stopwatch/")
    elif message == "Open amazon":
        print("here is the link - https://www.amazon.com/")
    elif message == "Play music":
        print("here is the link - https://play.google.com/music")
    elif message == "Open youtube":
        print("here is the link - https://www.youtube.com/")
    elif message == "Open netflix":
        print("here is the link - https://www.netflix.com/in/")
    elif message == "What is the time now":
        x = datetime.datetime.now()
        print(x)
    elif message == "Open world clock":
        print("here is the link - https://www.timeanddate.com/worldclock/full.html")
    elif message ==" What  can you do":
        print("I can do: tell today's date , open google, open netflix,set alaram ect")
    elif message == "What is my name":
        print("your name is", name)
    elif message == "I love you":
        print("I love you too", name)
    elif message == "Tell me a joke":
       choice=["What do you call a rose that want to go to the moon Ans: Gulab Jamun", "Why is Cinderella so bad at soccer? Ans: Because she always runs away from the ball!","What do you call it when a dinosaur crashes his car? Ans:Tyrannosaurus wrecks"] 
       joke = random.choice(choice)
       print (joke)
    elif message == "How old are you":
        print("I am 8years old")
    elif message == "When is your birthday":
        print("My birthday is at 1/6/2022")
    elif message == "Feedback":
        input("Enter your feedback")
        print("Thank you", name ,"for the feedback")
    elif message == "Teach me english":
        print("Read everything you can get your hands on. ..Actively take note of new vocabulary. ...Talk with real live humans. ...Subscribe to podcasts or Youtube channels (in English) ...Go abroad. ...Use your friends. ...Ask a lot of questions. ...Take a lead from the stars.")
    elif message == "Tell me a story":
        print("here is the link - https://learnenglishkids.britishcouncil.org/short-stories")
    elif message == "Do you know alexa":
        print("Yes she is my best friend")
    elif message == "Do you know google":
        print("yes she is so prety")
    elif message == "Do you know siri":
        print("Yes , my wish is I want to be in next iphone")
    elif message == "What is the date today":
        l = datetime.datetime.now()
        print(l.strftime("%x"))
    elif message == "What is the year":
        a = datetime.datetime.now()
        print(a.year)
    elif message == "Which century is this":
        m = datetime.datetime.now()
        print(m.strftime("%C"))
    elif message=="Open settings":
        print("Sorry Homo don't have a settings")   
    else: 
      print("sorry,",name,"could not find , check if the spelling is correct and check if the frist letter is capital or it will be not in my code") 