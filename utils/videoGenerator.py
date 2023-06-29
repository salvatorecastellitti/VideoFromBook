from moviepy.editor import *
import os
import random
from moviepy.video.fx.all import crop

PATH_VIDEOBG = 'tmpVideos/'
PATH_SAVED_VIDEO = 'Videos/'

listVideos = os.listdir(PATH_VIDEOBG)
listVideos = [ x for x in listVideos if ".mp4" in x ]
video_name = random.choice(listVideos)

def get_cutted_video(length: int):
    clip = VideoFileClip(PATH_VIDEOBG + video_name)

    duration = clip.duration

    rand_point_video = random.uniform(0,float(duration)-float(length))

    clip = clip.subclip(rand_point_video, rand_point_video+length)

    (w, h) = clip.size
    crop_width = h * 9/16
    x1, x2 = (w - crop_width)//2, (w+crop_width)//2
    y1, y2 = 0, h
    clip = crop(clip, x1=x1, y1=y1, x2=x2, y2=y2)

    clip.write_videofile(PATH_SAVED_VIDEO + 'tmpCutEdited.mp4',codec='libx264')

    return PATH_SAVED_VIDEO + 'tmpCutEdited.mp4'

def create_final_video(path_image: str, path_audio: str, path_video: str, path_audio_final:str):

    final_audio_duration = AudioFileClip(path_audio_final).duration
    path_cutted_video = get_cutted_video(int(final_audio_duration))

    clip = VideoFileClip(path_cutted_video)
    audioclip = AudioFileClip(path_audio_final)

    audio_list = sorted(os.listdir(path_audio))
    audio_list = [path_image + audio for audio in audio_list]

    final_clip = clip.set_audio(audioclip)
    image_list = sorted(os.listdir(path_image))
    image_list = [path_image + image for image in image_list]
    start = 0

    for x in range(0, len(image_list)):
        duration = audio_list[x][audio_list[x].index('_')+1:audio_list[x].rfind('.')]
        title = ImageClip(image_list[x]).set_start(start).set_duration(duration).set_pos((0,0))
        start = float(start) + float(duration)
        final_clip = CompositeVideoClip([final_clip, title])

    final_clip.write_videofile("Videos/TikTok.mp4")

    os.remove(path_cutted_video)



#create_final_video("Images/2/",'tmpAudios/2/',PATH_SAVED_VIDEO + 'tmpCutEdited.mp4',"tmpAudios/2/test.mp3")
