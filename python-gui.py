import tkinter as tk
window = tk.Tk()

greeting = tk.Label(
    text = "YouTube to MP4 Downloader",
    fg   = "black",
    bg   = "red")
greeting.pack()

entry = tk.Entry()
entry.pack()
path = entry.get



window.mainloop()
