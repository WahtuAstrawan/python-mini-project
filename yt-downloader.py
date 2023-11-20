from pytube import YouTube

def downloadVideo(link):
    yt = YouTube(link)
    ytDownload = yt.streams.get_highest_resolution()
    print(f"Video dengan judul {yt.title} sedang didownload...")
    ytDownload.download("./")
    print("Video berhasil didownload")

def downloadAudio(link):
    yt = YouTube(link)
    ytDownload = yt.streams.filter(only_audio=True).first()
    print(f"Audio dengan judul {yt.title} sedang didownload...")
    ytDownload.download("./")
    print("Audio berhasil didownload")

link = input("Masukkan link video youtube : ")

print("1. Download Video Youtube")
print("2. Download Audio Youtube")

choice = int(input("Pilih opsi : "))

if choice == 1:
    downloadVideo(link)
elif choice == 2:
    downloadAudio(link)
