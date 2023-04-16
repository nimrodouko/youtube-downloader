
import periodictable
from django.shortcuts import render
from pytube import YouTube
# Create your views here.
from moviepy.video.io.VideoFileClip import VideoFileClip
from django.http import HttpResponse,FileResponse,HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def download_video(request):
    if request.method == 'POST':
        video= request.POST.get('video_url')
        yt = YouTube('video')
        stream = yt.streams.get_highest_resolution()
        response = FileResponse(stream.download())
        response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
    
    return  render(request, 'home.html')


def chemistry(request):
    if request.method == 'POST':
        Atomic_number = int(request.POST.get('atomic_number'))
        element = periodictable.elements[Atomic_number]
        return render(request,'chemistry.html',{'element':element})
    return render(request, 'chemistry.html')

