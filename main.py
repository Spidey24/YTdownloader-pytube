from pytube import YouTube
from pytube.cli import on_progress
def main():
    def download_video(url,audio_only=False,video_only=False,resolution=None,path=None):
        yt = YouTube(url,on_progress_callback=on_progress)
        if audio_only:
            stream = yt.streams.filter(only_audio=True).first()
        elif video_only:
            if resolution:
                stream = yt.streams.filter(res=resolution,only_video=True).first()
            else:
                stream = yt.streams.filter(only_video=True).first()
        else:
            if resolution:
                stream = yt.streams.filter(res=resolution).first()
            else:
                stream = yt.streams.first()
        if path:
            stream.download(output_path=path)
        else:
            stream.download()

    if __name__ == "__main__":
        url = input("\nEnter the URL of the video:\n ")
        print("------------------------------------------")
        download_option = input("\nEnter from below choices only :\n 1 for audio only \t 2 for video only \t 3 for both audio and video : \n")
        print("------------------------------------------")
        if download_option in ['1','2','3']:
            print('\n Resolution options are as follows :\n 1080p \t 720p \t360p \t144p \n Please give a value from above choices only :))')
            print("------------------------------------------")
            resolution = input("\nEnter resolution for video download: \n")
            print("------------------------------------------")
            file_path = input("\nEnter the file path to download the video:\n")
            if download_option == "1":
                download_video(url,audio_only=True,path=file_path)
            elif download_option == "2":
                download_video(url,video_only=True,resolution=resolution,path=file_path)
            else:
                download_video(url,resolution=resolution,path=file_path)
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()

