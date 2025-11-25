import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

from frontend.interface.PrisonerListUI import PrisonerListUI
from frontend.interface.PrisonerAddUI import PrisonerAddUI
from frontend.interface.PrisonerMoveUI import PrisonerMoveUI
from frontend.interface.GuardListUI import GuardListUI
from frontend.interface.GuardScheduleUI import GuardScheduleUI

from api_requests.PrisonerRequest import PrisonerRequest
from api_requests.GuardRequest import GuardRequest

class MainMenuUI:
    def __init__(self, user=None):
        self.user = user
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.prisoner_request = PrisonerRequest("http://127.0.0.1:5000")
        self.guard_request = GuardRequest("http://127.0.0.1:5000")

        # Ablak
        self.root = ctk.CTk()
        self.root.title("Főmenü")
        # Érdemes a canvas méretével egyező ablakméretet használni
        self.root.geometry("1024x600")

        # Háttér canvas (ha később képet szeretnél, ide lehet betenni)
        self.bg_canvas = tk.Canvas(self.root, width=1024, height=600,
                                   highlightthickness=0, bd=0)
        self.bg_canvas.place(relwidth=1, relheight=1)

        # Középső doboz (main frame)
        self.main_frame = ctk.CTkFrame(
            self.bg_canvas,
            width=800,
            height=500,
            fg_color="#2a2a2a",
            bg_color="transparent"
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.create_main_menu()

    # MAIN MENU LÉTREHOZÁSA
    def create_main_menu(self):
        # Belső tartalom frame (ez lesz a menü tartalma)
        self.menu_content = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        self.menu_content.pack(padx=80, pady=60, fill="both", expand=True)

        title = ctk.CTkLabel(
            self.menu_content,
            text="Főmenü",
            font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
            text_color="white"
        )
        title.pack(pady=(0, 30))
        
        # GOMBOK
        self.create_menu_button("Fogvatartottak", lambda: self.open_window("Fogvatartottak", self.prisoner_window))
        self.create_menu_button("Őrök", lambda: self.open_window("Személyzet", self.guard_window))
        self.create_menu_button("Térkép", lambda: self.open_window("Térkép", self.map_window))

        self.create_menu_button("Kilépés", self.logout)

    # Metódus — helyesen az osztály szintjén (nem create_main_menu belsejében!)
    def create_menu_button(self, text, command):
        btn = ctk.CTkButton(
            self.menu_content,
            text=text,
            width=400,
            height=50,
            corner_radius=10,
            fg_color="#2A8AC0",
            hover_color="#1F6AA5",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=command
        )
        btn.pack(pady=12)

    # ABLAK MEGNYITÁS
    def open_window(self, title, callback):
        # Elrejtjük a főmenüt
        self.menu_content.pack_forget()

        # Új tartalmi frame a main_frame-en belül
        self.win = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        self.win.pack(padx=80, pady=60, fill="both", expand=True)

        ctk.CTkLabel(
            self.win,
            text=title,
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        ).pack(pady=(0, 30))

        # kitölti saját tartalommal a callback
        callback(self.win)

        # Vissza gomb
        ctk.CTkButton(
            self.win,
            text="Vissza a főmenübe",
            width=400,
            height=40,
            corner_radius=10,
            fg_color="#444444",
            hover_color="#333333",
            command=self.back_to_menu
        ).pack(pady=35)

    # ABLAKOK TARTALMA
    def prisoner_window(self, frame):
        self.create_sub_button(frame, "Lista megnyitása", self.open_prisoner_list)
        self.create_sub_button(frame, "Új fogvatartott felvétele", self.open_prisoner_add)
        self.create_sub_button(frame, "Áthelyezés", self.open_prisoner_move)

    def guard_window(self, frame):
        self.create_sub_button(frame, "Őrök listája", self.open_guard_list)
        self.create_sub_button(frame, "Beosztások", self.open_guard_schedule)

    def map_window(self, frame):
        self.create_sub_button(frame, "Térkép")

    def create_sub_button(self, frame, text, command=None):
        ctk.CTkButton(
            frame,
            text=text,
            width=350,
            height=45,
            corner_radius=10,
            fg_color="#2A8AC0",
            hover_color="#1F6AA5",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=command if command else lambda: self.open_subfeature(text)
        ).pack(pady=10)

    # FUNKCIÓK
    def open_subfeature(self, feature_name):
        """Ide jön majd a backend funkció."""
        print("Megnyitott subfeature:", feature_name)

    def open_prisoner_add(self):
        PrisonerAddUI(
            prisoner_request=self.prisoner_request,
            master=self.root
        )


    def open_prisoner_move(self):
        PrisonerMoveUI(
            prisoner_request=self.prisoner_request,
            master=self.root
        )


    def open_guard_list(self):
        win = GuardListUI(
          
            guard_request=self.guard_request
        )
        win.run()


    def open_guard_schedule(self):
        win = GuardScheduleUI(
    
            guard_request=self.guard_request
        )
        win.run()

    def back_to_menu(self):
        # eltüntetjük az aktuális win-t, visszaállítjuk a menüt
        if hasattr(self, "win"):
            self.win.pack_forget()
        self.menu_content.pack(padx=80, pady=60, fill="both", expand=True)

    def open_prisoner_list(self):
        PrisonerListUI(prisoner_request=self.prisoner_request, master=self.root)


        
    def logout(self):
        self.root.destroy()

    # FUTTATÁS
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ui = MainMenuUI()
    ui.run()