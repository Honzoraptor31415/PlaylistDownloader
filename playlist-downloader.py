from pytube import Playlist
import ttkbootstrap as ttk
import tkinter as tk

window = ttk.Window(title="YouTube playlist downloader (made by Honzoraptor)", themename="darkly")
window.geometry("1200x700")
window.minsize(1000, 500)

ctrlsPadding = 10

def download():
  for video in Playlist(inputStr.get()).videos:
    text["text"] = f"Downloading {video.title}"
    stream = video.streams.filter(only_audio=True).first()
    print(stream.title)
    stream.download(filename=f"{video.title}.mp3", output_path="./Downloaded")

main = ttk.Frame(window)
main.pack(expand=True)

heading = ttk.Label(main, text="YouTube playlist downloader", font="Calibri, 17 bold")
heading.pack(pady=30)

controlls = ttk.Frame(main)
controlls.pack()

inputStr = tk.StringVar(value="Playlist link")
inp = ttk.Entry(controlls, textvariable=inputStr)
inp.pack(pady=30, side="left", ipadx=ctrlsPadding, ipady=ctrlsPadding)

dwnButton = ttk.Button(controlls, text="Download", cursor="hand2", command=download)
dwnButton.pack(side="right", ipadx=ctrlsPadding, ipady=ctrlsPadding)

vidInfo = ttk.Frame(main)
vidInfo.pack()

text = ttk.Label(vidInfo, font="Calibri 12", justify="center")
text.pack()

window.mainloop()