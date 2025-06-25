import tkinter as tk
from tkinter import *
import threading
import time, datetime
from bhElixerbot import Battle, collectElixir, StartBot

class BotGui(tk.Tk):
    def __init__(self):
        super().__init__()

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

    

    # Methods
    def Start_Bot_In_New_Thread(self): 
        botThread = threading.Thread(target=StartBot, args=(6,)) # MAKE DYNAMIC
        botThread.daemon = True
        botThread.start()

gui = BotGui()
gui.mainloop()

