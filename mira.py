#!/usr/bin/env python3

# File: mira.py
# Author: walvie
# Date: January 9, 2024
# Description: This script is the main entry point for the program MIRA

import tkinter
import customtkinter
import os

def get_midi_files(directory):
    midi_files = []
    
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter MIDI files based on their extensions
    midi_files = [file for file in files if file.lower().endswith(".midi") or file.lower().endswith(".mid")]
    
    return midi_files

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        directory_path = "C:/Users/arthu/Desktop/MIRP/MIDI_FILES"

        midi_files = get_midi_files(directory_path)

        self.MidiFileListLabel = customtkinter.CTkLabel(self, text="Midi Files:")
        self.MidiFileListLabel.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        loopCounter = 1
        for midi_file in midi_files:
            self.MidiFileEntry = customtkinter.CTkLabel(self, text=midi_file)
            self.MidiFileEntry.grid(row=loopCounter, column=0, padx=10, pady=(10, 0), sticky="w")
            loopCounter += 1

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("MIRA")
        self.geometry("854x480")
        self.wm_iconbitmap("miraLogo.ico")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")

app = App()


def initCustomTkinterColorTheme():
    """
    Initializes the custom Tkinter color theme for the window.
    """
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")


def initAppFrameParameters():
    """
    Initializes the parameters for the main application frame.

    Returns:
    CTK: The top level widget for this program with the defined parameters
    """

    return app


def addUiElements():
    """
    Initializes and packs the multiple UI elements for the main program.
    """
    label = customtkinter.CTkLabel(app, text="CTkLabel")


def initializeApp():
    initCustomTkinterColorTheme()
    initAppFrameParameters()
    addUiElements()


def main():
    initializeApp()
    addUiElements()

    app.mainloop()


if __name__ == "__main__":
    main()