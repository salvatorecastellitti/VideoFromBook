import random
from TTs.TikTok import TikTok, eng_voices
from moviepy.editor import AudioFileClip
tiktok = TikTok()
from utils.audioTrackGenerator import generate_voice, create_single_audio
from utils.videoGenerator import get_cutted_video, create_final_video

voice = random.choice(eng_voices)
PATH = "./Books/booksLatexVersion.txt"

print('[*] Generating voices & images')
length,path_audio,path_images = generate_voice(path=PATH, choosen='en_au_002', voice_random=False)
print('[*] Voices & images generated')

print('[*] Generating single audio')
path_final_audio = create_single_audio(path_audio=path_audio)
print('[*] Single audio generated')

print('[*] Generating cutted video')
path_cutted_video = get_cutted_video(length=length)
print('[*] cutted video generated')

create_final_video(path_image=path_images, path_audio=path_audio,path_video=path_cutted_video,path_audio_final=path_final_audio)

#print(length,path_audio,path_images)


