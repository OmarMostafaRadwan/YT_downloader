import tkinter
from pytube import YouTube
import customtkinter as ctk


def startDownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink)
        video = ytobject.streams.get_highest_resolution()
        video.download()
    except:
        print("YouTube link is invalid")
    print("Download complete")



# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System")	
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("720x480")
app.title("ytd")

title = ctk.CTkLabel(app, text="insert a Youtube link ")
title.pack(padx=10, pady=10)


url_var = tkinter.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()


download = ctk.CTkButton(app, text="download", command=startDownload)
download.pack(padx=20, pady=20)



app.mainloop()
