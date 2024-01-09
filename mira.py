import tkinter
import customtkinter

# Initialise the default color theme for our program
def initCustomTkinterColorTheme():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

def main():
    initCustomTkinterColorTheme()

    app = customtkinter.CTk()
    app.geometry("854x480")
    app.title("MIRA")

    app.mainloop()




if __name__ == "__main__":
    main()