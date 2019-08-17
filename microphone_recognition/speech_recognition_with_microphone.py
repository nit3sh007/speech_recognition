# import speech_recognition as sr
# r = sr.Recognizer()
# mic = sr.Microphone()
# #print(sr.Microphone.list_microphone_names())
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# print(r.recognize_google(audio))
#
import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
print("You said: " + r.recognize_google(audio))


