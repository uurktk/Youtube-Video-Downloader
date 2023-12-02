import tkinter as tk
from tkinter import messagebox, filedialog
import pytube as yt

# Creating window
window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry("500x125")

# Creating entry field to display selected directory
entry_directory = tk.Entry(window)
entry_directory.pack(ipadx=100, ipady=5)

# Creating directory selection button
def select_directory():
    download_directory = filedialog.askdirectory(title="Select Download Directory")
    if download_directory:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, download_directory)

directory_button = tk.Button(window, text="Select Directory", command=select_directory)
directory_button.pack()

# Creating link input
link_input = tk.Entry(window)
link_input.pack(ipadx=100, ipady=5)  # Adjust internal padding for size

# Defining the download function
def download():
    try:
        link = link_input.get()
        video = yt.YouTube(link)
        download_directory = entry_directory.get()

        if download_directory:
            video.streams[0].download(download_directory)
            messagebox.showinfo("Download finished.", "Video downloaded successfully.")
        else:
            messagebox.showinfo("Error", "Please select a download directory.")
    except Exception as e:
        messagebox.showinfo("Error", f"Unexpected error:, {str(e)}.")

# Creating download button
download_button = tk.Button(window, text="DOWNLOAD", command=download)
download_button.pack()

# Making window visible
window.mainloop()
