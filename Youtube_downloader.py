from pytube import YouTube
# pytube is a library for downloading YouTube Videos.
import os
# os will be useful for specifying a file path on any computer as i want the file to go into the downloads folder for any user
from decimal import Decimal
# decimal allows the filesize to be easily rounded to two decimal places
from pytube.cli import on_progress
# on_progress is a built in progress bar that shows the percentage of the download 

home = os.path.expanduser('~')
# specifies the users home directory
download_folder = os.path.join(home, 'Downloads')
# finds the 'downloads' folder in the home directory so file will go there for every user


def downloader():
    link = input('Enter a YouTube link to be downloaded: ')
    # called on_progress function inside the yt variable so it will show progress bar when the download begins
    try:
        yt = YouTube(link, on_progress_callback=on_progress)
    except:
        print("Invalid link entered.")
    #Video Title
    print('\nTitle: ' + yt.title)
    #Number of views
    #change yt.views to a string as it can't concatenate an integer
    print ('Viewcount: ' + str(yt.views))
    #Length of the Video
    # divide length by 60 to find the minutes as default output is in seconds
    print('Length: ' + str(yt.length/60) + ' minutes')
    #Size of the file to be downloaded 
    bytes = yt.streams.filter(only_audio=True, file_extension='mp4').first().filesize
    kilobytes = Decimal(bytes/1024)
    # call Decimal so output is rounded to two decimal places, makes it easier to read
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

downloader()
# call the function to start the process

# https://www.youtube.com/watch?v=l7DVd3nwdaw
# example url - disney music
