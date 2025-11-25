import customtkinter as ctk
from tkinter import messagebox

class PrisonerMoveUI:
    def __init__(self, prisoner_request, master=None):

        # Ablak
        if master:
            self.root = ctk.CTkToplevel(master)
            self.root.transient(master) 
            self.root.grab_set() 
        else:
            self.root = ctk.CTk()

        self.root.title("Fogvatartott áthelyezése")
        self.root.geometry("1024x600")

        # Backend kérés
        self.req = prisoner_request

        # Központi frame
        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(padx=30, pady=30, fill="both", expand=True)

        # Cím
        ctk.CTkLabel(
            frame,
            text="Fogvatartott áthelyezése",
            font=ctk.CTkFont(size=26, weight="bold")
        ).pack(pady=20)

        # Bemenetek
        self.pid = self._input(frame, "Fogvatartott ID")
        self.new_cell = self._input(frame, "Új cellaszám")

        # Gomb
        ctk.CTkButton(
            frame,
            text="Áthelyezés",
            width=300,
            fg_color="#2A8AC0",
            hover_color="#1F6AA5",
            command=self.move_prisoner
        ).pack(pady=25)

    # Mezők generálása
    def _input(self, parent, placeholder):
        entry = ctk.CTkEntry(parent, placeholder_text=placeholder, width=350)
        entry.pack(pady=8)
        return entry

    # Backend hívás
    def move_prisoner(self):
        try:
            pid = int(self.pid.get())
            new_cell = int(self.new_cell.get())
        except ValueError:
            messagebox.showerror("Hiba", "Az ID és cellaszám csak szám lehet!")
            return

        try:
            response = self.req.move_prisoner(pid, new_cell)
            print("Backend válasz:", response)

            messagebox.showinfo("Siker", "A fogvatartott áthelyezése megtörtént.")
        except Exception as e:
            messagebox.showerror("Backend hiba", f"Hiba történt:\n{str(e)}")
