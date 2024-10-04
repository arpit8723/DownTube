from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import sys

#progress bar
def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    progress = total_size - bytes_remaining
    percent = (progress / total_size) * 100
    sys.stdout.write(f"\rDownload progress: {percent:.2f}%")
    sys.stdout.flush()

def download_video(url,save_dir):
    try:
        yt=YouTube(url,on_progress_callback=progress_callback)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest_resol=streams.get_highest_resolution()
        highest_resol.download(output_path=save_dir)
        print("Download Successfull!")

    except Exception as e:
        print(e)  

def download_audio(url,save_dir):
    try:
          yt=YouTube(url)
          streams=yt.streams.filter(progressive=True,file_extension="mp3")
          highest_qual=streams.get_audio_only()
          highest_qual.download(output_path=save_dir)
          print("Download Successfull!")

    except Exception as e:
        Choice=input("Sorry :( no audio stream available for this song Would you like to download video(v) instead ?") 
        if Choice=='v':
             download_video(video_url,save_dir) 
        else:exit    

def open_file_dialog():
    folder= filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

        return folder

if __name__== "__main__":
        root=tk.Tk()
        root.withdraw()
        
        video_url= input("please enter a YouTube url: ")
        save_dir=open_file_dialog()

        if save_dir:
             download_type=input("Do you want to download Video(v)or Audio(a)?")
             if download_type=='v':
                print("Started Downloading...")
                download_video(video_url,save_dir)
             elif download_type == 'a':
                  print("Started Downloading Audio...")
                  download_audio(video_url, save_dir)
            
        else:
              print("Invalid file location")