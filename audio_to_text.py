# using audio file to print audio text as a string
import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('harsh.wav')

with harvard as source:
    #r.adjust_for_ambient_noise(source)
    # for noise ambient in audio file

    audio = r.record(source)
print(r.recognize_google(audio))

