from pytube import YouTube
#pytube is a library for downloading YouTube Videos.

link = input('Enter a YouTube link to be downloaded: ')
yt = YouTube(link)

#Video Title
print('Title: ' + yt.title)

#Number of views
print ('Viewcount: ' + yt.views)

#Length of the Video
print('Video is ' + yt.length + 'seconds long.')

question = input('Is this the correct video? Enter y or n: ')
if question == 'y':
    # Filtering out the streams that are audio only and downloading the first in the list
    print('Your download will begin shortly')
    yt_dload = yt.streams.filter(audio_only=True).first()
    location = input('Enter the file path of where you want the audio to be saved: ')
    yt_dload.download(location)
    print('Your download is now complete!')
elif question == 'n':
    print('Enter another link when prompted')
else:
    print('Incorrect character!')
    
