import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime


class GuardListUI:
    def __init__(self, guard_request, master=None):
        # Ha van master, akkor Toplevel, különben saját root
        if master:
            self.root = ctk.CTkToplevel(master)
            self.root.transient(master)
            self.root.grab_set()
        else:
            self.root = ctk.CTk()
        
        self.root.title("Őrök listája")
        self.root.geometry("1024x600")

        self.guard_request = guard_request

        # Fő frame
        self.frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame.pack(padx=30, pady=30, fill="both", expand=True)

        # Cím
        ctk.CTkLabel(
            self.frame,
            text="Őrök listája",
            font=ctk.CTkFont(size=26, weight="bold")
        ).pack(pady=20)

        # Scrollable lista
        self.list_frame = ctk.CTkScrollableFrame(self.frame, width=700, height=400)
        self.list_frame.pack(expand=True, fill="both")

        # Frissítés gomb
        self.refresh_btn = ctk.CTkButton(
            self.frame,
            text="Frissítés",
            command=self.load_guards
        )
        self.refresh_btn.pack(pady=(15, 0))

        # Vissza gomb
        self.back_btn = ctk.CTkButton(
            self.frame,
            text="Vissza a főmenübe",
            fg_color="#444444",
            hover_color="#333333",
            command=self.root.destroy
        )
        self.back_btn.pack(pady=15)

        # Első adatbetöltés
        self.load_guards()

    def load_guards(self):
        # Régi widgetek törlése
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        try:
            guards = self.guard_request.get_all_guards()
        except Exception as e:
            messagebox.showerror(
                "Backend Error",
                f"A backend nem elérhető: {str(e)}"
            )
            guards = []

            print ("DEBUG JSON:" , guards)

        if not guards:
            ctk.CTkLabel(
                self.list_frame,
                text="Nincs megjeleníthető adat.",
                text_color="gray",
                font=ctk.CTkFont(size=16)
            ).pack(pady=10)
            return

        for g in guards:
            if not isinstance(g, dict):
                continue  # Ha valamiért string, átugorjuk

            # Dátum formázása YYYY-MM-DD formátumban
            birth_raw = g.get('Birth_Date', '?')
            try:
                birth_date = datetime.strptime(birth_raw, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d')
            except:
                birth_date = birth_raw

            item_text = f"ID: {g.get('Guard_ID', '?')} | {g.get('F_Name', '?')} {g.get('L_Name', '?')} | " \
                        f"Rang: {g.get('Rank', '?')} | Block: {g.get('Block_ID', '?')} | " \
                        f"Prison: {g.get('Prison_ID', '?')} | Birth date: {birth_date}"

            item = ctk.CTkLabel(
                self.list_frame,
                text=item_text,
                font=ctk.CTkFont(size=16),
                text_color="white",
                anchor="w"
            )
            item.pack(anchor="w", padx=10, pady=5)