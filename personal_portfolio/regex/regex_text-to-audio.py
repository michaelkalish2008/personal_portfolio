# TEXT-AUDIO TRANSCRIPTION USING THE GTTS LIBRARY

# STEP 1: Download/import transcription package
from gtts import gTTS
import os
import re

# STEP 2: Select file and open file and save content to variable
# fpath = './gdpr_part1_preamble_to_art17.txt'
# fpath = './gdpr_part2_art18_to_art52.txt'
fpath = './gdpr_part3_art53_to_end.txt'
f = open(fpath, 'r')
content = f.read()
content = re.sub(r'\s+',' ',content)

# STEP 4: Convert content to audio file and select language
myobj = gTTS(text=content,
             lang='en',
             slow=False)

# STEP 5: Save mp3 to director and close txt file
# myobj.save('gdpr_part1_start_to_art17.mp3')
# myobj.save('gdpr_part2_art18_to_art52.mp3')
myobj.save('gdpr_part3_art53_to_end.mp3')
f.close()

# FIN

# NOTES
# Documentation for gtts: https://gtts.readthedocs.io/en/latest/module.html
# Using conda? conda install gtts
# Want to compress the file? "Check out Simple Audio Compression With Python"
# Medium, url 'https://medium.com/@jmpion/simple-audio-compression-with-python-70bdd7535b0a'
# python3 text_to_audio.py