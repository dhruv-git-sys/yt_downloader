from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
def download_video(url,save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream=streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selected folder:{folder}")
    return folder

if __name__=="__main__":
    root=tk.Tk()
    root.withdraw()
    def get_url():
        url_window=tk.Toplevel(root)
        url_window.title("YouTube URL Input")
        url_window.geometry("400x120")
        tk.Label(url_window, text="Enter the YouTube video URL").pack(pady=10)
        url_var = tk.StringVar()
        entry=tk.Entry(url_window,textvariable=url_var,width=50)
        entry.pack(pady=5)
        entry.focus()
        result={'url':None}
        def submit():
            result['url']=url_var.get()
            url_window.destroy()
        tk.Button(url_window,text="OK",command=submit).pack(pady=10)
        url_window.grab_set()
        root.wait_window(url_window)
        return result['url']
    video_url=get_url()
    if not video_url:
        print("No URL entered. Exiting...")
    else:
        save_dir=open_file_dialog()
        if save_dir:
            print("Starting download...")
            download_video(video_url, save_dir)
            print("Download completed!")
        else:
            print("No folder selected. Exiting...")

