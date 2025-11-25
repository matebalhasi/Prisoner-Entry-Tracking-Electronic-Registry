import customtkinter as ctk
from tkinter import messagebox

class PrisonerAddUI:
    def __init__(self, prisoner_request, master=None):
   
        if master:
            self.root = ctk.CTkToplevel(master)
            self.root.transient(master) 
            self.root.grab_set() 
        else:
            self.root = ctk.CTk()

        self.root.title("Új fogvatartott felvétele")
        self.root.geometry("600x500")

        self.req = prisoner_request

        # Fő frame
        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(padx=30, pady=30, fill="both", expand=True)

        # Cím
        ctk.CTkLabel(
            frame,
            text="Új fogvatartott felvétele",
            font=ctk.CTkFont(size=26, weight="bold")
        ).pack(pady=20)

        # INPUT MEZŐK
        self.f_name = self._input(frame, "Keresztnév")
        self.l_name = self._input(frame, "Vezetéknév")
        self.birth = self._input(frame, "Születési dátum (YYYY-MM-DD)")
        self.danger = self._input(frame, "Veszélyességi szint (Low/Medium/High)")
        self.cell = self._input(frame, "Cellaszám")

        # GOMB
        ctk.CTkButton(
            frame,
            text="Hozzáadás",
            width=300,
            fg_color="#2A8AC0",
            hover_color="#1F6AA5",
            command=self.add_prisoner
        ).pack(pady=25)

    def _input(self, parent, placeholder):
        entry = ctk.CTkEntry(parent, placeholder_text=placeholder, width=350)
        entry.pack(pady=8)
        return entry

    def add_prisoner(self):
        data = {
            "F_Name": self.f_name.get().strip(),
            "L_Name": self.l_name.get().strip(),
            "Birth_Date": self.birth.get().strip(),
            "Danger_Level": self.danger.get().strip(),
            "Cell_Number": self.cell.get().strip()
        }

        # Validálás egyszerűen
        if not all(data.values()):
            messagebox.showwarning("Hiányzó adatok", "Kérlek tölts ki minden mezőt!")
            return

        response = self.req.add_prisoner(data)
        print("Backend válasz:", response)

        # Siker / hiba kezelése
        if response.get("error"):
            messagebox.showerror("Hiba", f"Nem sikerült hozzáadni: {response['error']}")
        else:
            messagebox.showinfo("Siker", "A fogvatartott sikeresen felvéve!")
            # Az ablak bezárása siker után
            self.root.destroy()
