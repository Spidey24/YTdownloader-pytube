from pytube import YouTube 
from pytube.cli import on_progress
import pytube.request
import random
import time

def main():
    pytube.request.default_range_size = 500000
    def typewriter(n,m,t):
        for a in t:
            r = random.uniform(n,m)
            time.sleep(r)
            print(a,end='',flush=True)

    def comp(a,b):
        completed = '\nDownload Completed!\n'
        size = 'File Size' + str(stream.filesize/10000000) + 'Mb\n'
        title = 'Title:' +stream.title + '\n'
        author = 'Author :' + yt.author + '\n'
        length = 'Video length\t' + str(yt.length) + 'Seconds\n'

        txt_list = [completed,size,title,author,length]

        for t in txt_list:
            typewriter(0.05,.1,t)
            print('-' * 60)

    url = input('\nPlease Enter the URL:\n')


    try :
        yt = YouTube(url,on_progress_callback=on_progress,on_complete_callback=comp)
        stream = yt.streams.filter(progressive=True,file_extension='mp4').get_highest_resolution()
        typewriter(0.05,.1,'Download is started....\n')
        stream.download()
    except:
        print('something gone wrong :((')

if __name__ == '__main__':
    main()