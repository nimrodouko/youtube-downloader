from pytube import YouTube

link=input("copy and paste your youtube link here: ")
video=YouTube(link)
high_res= video.streams.get_highest_resolution()
high_res.download('E:\series')















