
import periodictable
from django.shortcuts import render
from pytube import YouTube
# Create your views here.
from moviepy.video.io.VideoFileClip import VideoFileClip

def get_highest_resolution(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        yt =YouTube(video_url)
        stream = yt.streams.first()
        h = stream.Download()
        
        return stream
    else:
        return render(request, 'home.html')


def converter(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        audio = video_url.audio
        audio.write_audiofile("video_url.mp3")
        response['Content-Type'] = 'audio.mp3'
        response['Content-Disposition']='attachment;filename="{}.mp3"'.format(yt.title)
        return response

    else:
        return render(request,'converter.html')


Atomic_number = int(input("Enter Element Atomic Number: "))
Element = periodictable.elements[Atomic_number]
print('Atomic number: ',Element.number)
print('Symbol: ', Element.symbol)
print('Name: ', Element.name)
print('Atomic Mass :', Element.mass)
print('Density: ', Element.density)


def chemistry(request):
    if request.method == 'POST':
        Atomic_number = request.POST.get('atomic_number')
        