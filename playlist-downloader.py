from pytube import Playlist
playlist = Playlist("https://www.youtube.com/playlist?list=PLUgpDpw4mkkuElgQuxhqCloX2Jrc0nNxb")
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos:
    stream = video.streams.filter(only_audio=True).first()
    print(stream.title)
    stream.download(filename=f"{video.title}.mp3", output_path="./Downloaded")