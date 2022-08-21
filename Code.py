import speech_recognition as sr
import pyttsx3
import math

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#function for audio output--------------------
def say(audio):                               #
    engine.say(audio)                         #
    engine.runAndWait()                       #
#---------------------------------------------
print("SAY")
print("ADD or ADDITION to add two numbers")
print("DIFFERENCE or SUBTRACT to subtract")
print("DIVIDE or DIVISION to divide")
print("MULTIPY or PRODUCT to multipy")
print("REMAINDER or LEFT to find the remainder")
print("COS or COSINE to find cosine value of an angle")
print("SIN or SINE to find sin value of an angle")
print("TAN or TANGENT to find tan value of angle")
print("SQUARE root or ROOT to find square of a positive integer")
print("POWER OF or RAISED TO POWER to find the eponantial value ")
print("LOG to determine the logrithemic value first tell the number and then base")          


#function for audio input-----------------------------------------
def takeCommand():                                                #
    r = sr.Recognizer()                                           #
    with sr.Microphone() as source:                               #
        print("Listening...")                                     #
        r.pause_threshold = 1                                     #
        audio = r.listen(source)                                  #
                                                                  #
    try:                                                          #
        print("Recognizing...")                                   #
        quary = r.recognize_google(audio, language='en-in')       #
        print(f"User said: {quary}\n")                            #
                                                                  #
    except Exception as e:                                        #
        print("Please say that again...")                         #
        return "None"                                             #
    return quary                                                  #
#------------------------------------------------------------------

st='Yes'
while(st.upper()=='YES'):
    #code for calculator
    say("Hello! Tell me the operation to do!")
    print("Hello! Tell me the operation to do!")  
    quary=takeCommand().lower()#Command to take any mathmatical function as an input
    if quary== 'ad' or quary=='addition':
            say("Tell me the first number!")
            x=takeCommand()
            x=float(x)
            print("The first number is: ",x)
            say("Tell me the second number!")
            y=takeCommand()
            y=float(y)
            print("The second number is: ",y)
            s=0.0
            s=s+x+y
            say("The sum is ")
            print("The sum is: ",s)    
##########################################################################
    elif  quary=='difference' or quary=='subtract':
            say("Tell me the first number!")
            x=takeCommand()
            x=float(x)
            print("The first number is: ",x)
            say("Tell me the second number")
            y=takeCommand()
            y=float(y)
            print("The second number is: ",y)
            s=0.0
            s=s+x-y
            say("The difference is ")
            print("The difference is: ",s)
##########################################################################
    elif quary=='divide' or quary=='division':
            say("What's the numerator")
            x=takeCommand()
            x=float(x)
            print("The numerator is: ",x)
            say("Tell me the denomenator")
            y=takeCommand()
            y=float(y)
            print("The denomenator is: ",y)
            s=x/y
            say("The questiont is ")
            print("The questiont is: ",s)
#########################################################################
    elif quary=='multiply' or quary=='product':
            say("Tell me the first number!")
            x=takeCommand()
            x=float(x)
            print("The first number is: ",x)
            say("Tell me the second number!")
            y=takeCommand()
            y=float(y)
            print("The second number is: ",y)
            s=x*y
            say("The product is ")
            print("The product is: ",s)
##########################################################################
    elif quary=='remainder' or quary=='left':
            say("Tell me the numenotor!")
            x=takeCommand()
            x=float(x)
            print("Numinator is: ",x)
            say("Tell me the denomenator!")
            y=takeCommand()
            y=float(y)
            print("Denominator is: ",y)
            s=x%y
            say("The remainder is ")
            print("The remainder is: ",s)
##########################################################################
    elif quary=='cos' or quary=='cosine':
            say("What's tha value of x?")
            x=takeCommand()
            x=int(x)
            s=math.cos(x)
            say("The angle is")
            print("The angle is: ",s)
##########################################################################
    elif quary== 'tan' or quary=='tangent':
            say("What's the value of x?")
            x=takeCommand()
            x=int(x)
            s=math.tan(x)
            say("The angle is ")
            print("The angle is: ",s)
##########################################################################
    elif quary=='sine' or quary=='sin':
            say("What's the value of x?")
            x=takeCommand()
            x=int(x)
            s=math.sin(x)
            say("The angle is ")
            print("The angle is: ",s)
##########################################################################
    elif quary=='square root' or  quary=='root':
            say("Tell me the number!")
            x=takeCommand()
            x=int(x)
            s=math.sqrt(x)
            say("The root of number is ")
            print("The root of the number is: ",s)
##########################################################################
    elif quary=='power' or quary=='raised to power':
            say("Tell me the number")
            x=takeCommand()
            x=float(x)
            say("Tell me the power")
            y=takeCommand()
            y=int(y)
            s=math.pow(x,y)
            say("The answer is ")
            print("The answer is: ",s)
###########################################################################
    elif quary=='log':
            say("What's the number!")
            x=takeCommand()
            x=float(x)
            say("What's the base!")
            y=takeCommand()
            y=float(y)
            if y==10:
                s=math.log10(x)
                say("The answer is: ")
                print("The answer is: ",s)
            elif y==2:
                s=math.log2(x)
                say("The answer is: ")
                print("The answer is: ",s)
            else:
                s=math.log(x,y)
                say("The answer is: ")
                print("The answer is: ",s)
##########################################################################
########################################################################
    else:
        print("Invalid command!")
        say("Invalid command!")
        say("Say Yes if you want to do more calculations")
        print("Say Yes if you want to do more calculations")
        st=takeCommand()
        print(st)


print("The program ended! We welcome your feedbacks: ")
say("The program ended! We welcome your feedbacks: ")
x=takeCommand()
print(x)
say("Thank You")
print("Thank You")