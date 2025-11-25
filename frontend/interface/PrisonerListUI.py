import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

class PrisonerListUI:
    def __init__(self, prisoner_request, master=None):
     
        # Létrehozunk egy Toplevel ablakot a főmenü felett
        if master:
            self.root = ctk.CTkToplevel(master)
            self.root.transient(master) 
            self.root.grab_set() 
        else:
            self.root = ctk.CTk()

        self.root.title("Fogvatartottak listája")
        self.root.geometry("1024x600")

        self.prisoner_request = prisoner_request

        # Fő keret
        self.frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Cím
        ctk.CTkLabel(
            self.frame,
            text="Fogvatartottak listája",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        ).pack(pady=20)

        # Scrollable frame
        self.list_frame = ctk.CTkScrollableFrame(self.frame, width=700, height=400)
        self.list_frame.pack(expand=True, fill="both")

        # Frissítés gomb
        self.refresh_btn = ctk.CTkButton(
            self.frame,
            text="Frissítés",
            command=self.load_prisoner_list
        )
        self.refresh_btn.pack(pady=(15, 0))

        # Első adatbetöltés
        self.load_prisoner_list()

    def load_prisoner_list(self):
        # Régi widgetek törlése
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        try:
            data = self.prisoner_request.get_all_prisoners()
        except Exception as e:
            messagebox.showerror(
                "Backend Error",
                f"A backend nem elérhető: {str(e)}"
            )
            data = []

        # Debug: kiírjuk a kapott adatot
        print("DEBUG JSON:", data)

        # JSON feldolgozása
        if isinstance(data, list):
            prisoners = data
        else:
            prisoners = data.get("data", [])

        # Ha nincs adat
        if not prisoners:
            ctk.CTkLabel(
                self.list_frame,
                text="Nincs megjeleníthető adat.",
                text_color="gray",
                font=ctk.CTkFont(size=16)
            ).pack(pady=10)
            return

        # Megjelenítés
         # Megjelenítés
        for p in prisoners:
                # Dátum formázása
                birth_raw = p.get('Birth_Date', '?')
                try:
                    birth_date = datetime.strptime(birth_raw[:16], '%a, %d %b %Y').date()
                except:
                    birth_date = birth_raw

                item_text = f"ID: {p.get('ID', '?')} | {p.get('F_Name', '?')} {p.get('L_Name', '?')} | " \
                            f"Cell: {p.get('Cell_Number', '?')} | " \
                            f"Danger: {p.get('Danger_Level', '?')} | " \
                            f"Birth date: {birth_date}"


                item = ctk.CTkLabel(
                    self.list_frame,
                    text=item_text,
                    font=ctk.CTkFont(size=16),
                    text_color="white",
                    anchor="w"
                )
                item.pack(anchor="w", padx=10, pady=5)

