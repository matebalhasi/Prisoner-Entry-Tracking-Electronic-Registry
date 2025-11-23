import customtkinter as ctk
from frontend.interface.BaseUI import BaseWindow


class PrisonerAddUI(BaseWindow):
    def __init__(self, backend_url, prisoner_request):
        super().__init__("Új fogvatartott felvétele")

        self.req = prisoner_request
        self.backend_url = backend_url

        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(padx=30, pady=30, fill="both", expand=True)

        ctk.CTkLabel(
            frame, text="Új fogvatartott felvétele",
            font=ctk.CTkFont(size=26, weight="bold")
        ).pack(pady=20)

        # INPUT MEZŐK
        self.f_name = self._input(frame, "Keresztnév")
        self.l_name = self._input(frame, "Vezetéknév")
        self.birth = self._input(frame, "Születési dátum (YYYY-MM-DD)")
        self.danger = self._input(frame, "Veszélyességi szint")
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
            "F_Name": self.f_name.get(),
            "L_Name": self.l_name.get(),
            "Birth_Date": self.birth.get(),
            "Danger_Level": self.danger.get(),
            "Cell_Number": self.cell.get()
        }

        response = self.req.add_prisoner(data)
        print("Backend válasz:", response)
