from moviepy.video.io.VideoFileClip import VideoFileClip
import os
video = VideoFileClip("youtube downloader\mp4s\coolio.mp4")
audio = video.audio
audio.write_audiofile("coolio.mp3")
