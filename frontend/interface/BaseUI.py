import customtkinter as ctk


class BaseWindow:
    def __init__(self, title="Ablak", size="900x550"):
        self.root = ctk.CTk()
        self.root.title(title)
        self.root.geometry(size)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    def run(self):
        self.root.mainloop()
