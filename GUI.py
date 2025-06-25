import tkinter as tk
from tkinter import *
import threading
import time, datetime
from bhElixerbot import StartBot

class BotGui(tk.Tk):
    def __init__(self):
        super().__init__()
        # Bot Thread
        self.botThread = None
        # Stop Event
        self.stopEvent = threading.Event()
        # Window name
        self.title("CoC Bot -- WorreBozz")

        # Window size
        self.geometry("600x400")
        
        # Window icon
        icon = PhotoImage(file="Images/ClashOfClansLogo.png")
        self.iconphoto(True, icon)

        # Window Colour
        self.config(background="#4E4E4E")

        # Start Bot Button
        self.StartButton = tk.Button(self, text="Start Bot")
        self.StartButton.pack()
        self.StartButton.config(command=self.Start_Bot_In_New_Thread)

        # Stop Bot Button
        self.StopButton = tk.Button(self, text="Stop Bot")
        self.StopButton.pack()
        self.StopButton.config(command=self.Stop_Bot_Thread)

    

    # Methods
    def Start_Bot_In_New_Thread(self): 
        self.botThread = threading.Thread(target=StartBot, args=(6, self.stopEvent)) # MAKE DYNAMIC
        self.botThread.daemon = True
        self.botThread.start()
    
    def Stop_Bot_Thread(self):
        if self.botThread and self.botThread.is_alive():
            self.stopEvent.set()

if __name__ == "__main__":
    gui = BotGui()
    gui.mainloop()

