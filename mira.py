#!/usr/bin/env python3

# File: mira.py
# Author: walvie
# Date: January 9, 2024
# Description: This script is the main entry point for the program MIRA

import tkinter
import customtkinter

app = customtkinter.CTk()


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
    app.geometry("854x480")
    app.wm_iconbitmap("miraLogo.ico")
    app.title("MIRA")

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