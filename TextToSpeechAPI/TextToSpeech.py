import pyttsx3

def playResponce(responce):
    x = pyttsx3.init()
    x.setProperty( 'rate', 200 )
    x.setProperty( 'volume', 100 )
    x.say(responce)
    x.runAndWait()
    print( "Played Successfully......" )