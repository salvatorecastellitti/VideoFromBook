import random
from moviepy.editor import AudioFileClip
import os
import sys
from moviepy.editor import *
sys.path.append('/Users/salvatorecastellitti/Documents/code/VideoFromBook')
from TTs.TikTok import TikTok,eng_voices
from utils.imageGenerator import create_image_from_text

PATH_AUDIO = "tmpAudios/"
subfolders = [ f.name for f in os.scandir(PATH_AUDIO) if f.is_dir() ]
subfolders = [eval(i) for i in subfolders]
if(len(subfolders) == 0):
    folder_name = '1'
else:
    folder_name = str(max(subfolders)+1)

os.mkdir(PATH_AUDIO + folder_name)
PATH_AUDIO = PATH_AUDIO + folder_name + '/'

def generate_voice(path:str, choosen:str, voice_random:bool = False):

    tiktok = TikTok()

    if(voice_random is True):
        voice = random.choice(eng_voices)
    else:
        voice = choosen

    print("[*]voice used: " + voice)
    file = open(path)
    num = 0
    length = 0
    for line in file:
        if length > 30:
            break

        if line.isspace():
            continue
        if line.startswith('Chapter'):
            text = line
            filepath = PATH_AUDIO + f"audio{num}.mp3"
            tiktok.run(text=text, filepath=filepath, voiceChosen=voice )

            clip = AudioFileClip(PATH_AUDIO + f"audio{num}.mp3")
            last_clip_length = clip.duration
            length += clip.duration
            os.rename(PATH_AUDIO + f"audio{num}.mp3", PATH_AUDIO + f"audio{num}_{clip.duration}.mp3")
            path_image = create_image_from_text(text=text,num=num)
            num = num +1
        if "|" in line:
            newLine = line.split('|')
            for phrase in newLine:
                text = phrase
                filepath = PATH_AUDIO + f"audio{num}.mp3"
                tiktok.run(text=text, filepath=filepath, voiceChosen=voice )
                clip = AudioFileClip(PATH_AUDIO + f"audio{num}.mp3")
                last_clip_length = clip.duration

                length += clip.duration
                '''
                if(length> 30):
                    os.remove(PATH_AUDIO + f"audio{num}.mp3")
                    print("non ho letto la riga: " + text)
                    break
                '''
                os.rename(PATH_AUDIO + f"audio{num}.mp3", PATH_AUDIO + f"audio{num}_{clip.duration}.mp3")
                path_image = create_image_from_text(text=text,num=num)
                num = num +1

    return length, PATH_AUDIO, path_image

def create_single_audio(path_audio:str):
    audios_list = sorted(os.listdir(path_audio))
    audios_list = [path_audio + audio for audio in audios_list]
    audios = [AudioFileClip(c) for c in audios_list]
    final_audios = concatenate_audioclips(audios)

    final_audios.write_audiofile(path_audio + "test.mp3")

    return path_audio + "test.mp3"

#print(create_single_audio("tmpAudios/2/"))
