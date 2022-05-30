from gtts import gTTS
import os
Text = input("Masukan text: ")

myText = Text
file = ".mp3"

language = "en"

output = gTTS(text=myText, lang=language, slow=False)

output.save(Text + file)