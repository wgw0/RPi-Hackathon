import tkinter
import customtkinter
from pytube import YouTube
from list import *

# print(link_array)

def startDownload():
    try:

        for ytLink in link_array:
            ytObj = YouTube(ytLink)
            ytVideo = ytObj.streams.get_highest_resolution()
            ytVideo.download()


        # ytLink = linkEntry.get()


        # ytObj = YouTube(ytLink) ## could just be the scraped data in an array
        # ytVideo = ytObj.streams.get_highest_resolution()
        # ytVideo.download()
            ## after download


        
    except:
        for link in link_array:
            print(f"this {link} is invalid!")
        finishedLabel.configure(text='Error Downloading, Invalid link!',)

    print('Download complete!')
    
    finishedLabel.configure(text='Downloaded')

# sys settings 

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("operation recover ascomps videos")




title = customtkinter.CTkLabel(app, text='insert a youtube Link')
title.pack(padx=10, pady=10)


#link 
url_var = tkinter.StringVar()
linkEntry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
linkEntry.pack()

# finished label
finishedLabel = customtkinter.CTkLabel(app, text='')
finishedLabel.pack()

## download button 
button = customtkinter.CTkButton(app, text='download', command=startDownload)
button.pack(padx=10, pady=10)
linkEntry.pack()
app.mainloop()