import tkinter as tk
window = tk.Tk()

frame = tk.Frame()

greeting = tk.Label(
    master = frame,
    text   = "YouTube to MP4 Downloader")
greeting.pack()

frame.pack()



window.mainloop()
