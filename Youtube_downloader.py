from pytube import YouTube
import os
from decimal import Decimal
# pytube is a library for downloading YouTube Videos.
# os will be useful for specifying a file path on any computer as i want the file to go into the downloads folder for any user
# decimal allows the filesize to be easily rounded to two decimal places

home = os.path.expanduser('~')
# specifies the users home directory
download_folder = os.path.join(home, 'Downloads')
# finds the 'downloads' folder in the home directory so file will go there for every user

def downloader():
    link = input('Enter a YouTube link to be downloaded: ')
    yt = YouTube(link)
    #Video Title
    print('\nTitle: ' + yt.title)
    #Number of views
    #change yt.views to a string as it can't concatenate an integer
    print ('Viewcount: ' + str(yt.views))
    #Length of the Video
    print('Length: ' + str(yt.length) + ' seconds')
    #Size of the file to be downloaded 
    bytes = yt.streams.filter(only_audio=True, file_extension='mp4').first().filesize
    kilobytes = Decimal(bytes/1024)
    # divide the bytes by 1024 to get the kilobytes
    two_dp = round(kilobytes, 2)
    # shows the kilobytes to two decimal places
    print('Filesize: ' + str(two_dp) + ' kilobytes')

    # determines whether link is correct so they can enter another if needs be
    question = input('\nIs this the correct video? Enter Y or N: ')
    if question == 'y' or question == 'Y':
        # getting the audio only streams, with mp4 file formats so they'll play on most music players
        # first stream is usually the highest quality so using .first()
        yt_dload = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        print('\nYour download will now begin!')
        yt_dload.download(download_folder)
        print('\nYour download is now complete!')
    elif question == 'n' or question == 'N':
        print('\nEnter another link when prompted. \n')
        downloader()
    else:
        print('\nIncorrect character! \nEnter either Y or N.')

    
begin = downloader()

# https://www.youtube.com/watch?v=p0x6FEDV-ig
# young thug - check

# wasn't working previously, yt.streams would show an empty list
# had to run 'python -m pip install git+https://github.com/nficano/pytube' in the command line to get up to date pytube version
