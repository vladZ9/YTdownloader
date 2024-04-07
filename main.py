import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("The YouTube link is invalid")
    print("Downloade complete!")

# System Settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10,pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350,height=40, textvariable=url_var)
link.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10,pady=10)

# Run app
app.mainloop()